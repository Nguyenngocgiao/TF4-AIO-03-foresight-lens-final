import numpy as np
from typing import List, Tuple
from .models import SignalDatapoint

class AnomalyDetector:
    def __init__(self):
        # In a real scenario, baselines would be loaded from a DB per tenant/service.
        pass

    def generate_recommendation(self, metric: str, tenant_id: str) -> Tuple[str, str, float]:
        """Returns (suggested_action, reasoning, confidence)"""
        confidence = 0.85
        if metric == "cpu_pct":
            return "SCALE_UP", f"CPU drift detected. Scale RDS Instance for {tenant_id}.", confidence
        elif metric == "queue_depth":
            return "SCALE_UP", f"Queue backlog detected. Increase worker concurrency for {tenant_id}.", confidence
        elif metric == "mem_pct":
            return "ROLLBACK", f"Memory leak detected for {tenant_id}. Consider rollback.", confidence
        elif metric == "latency_p99_ms" or metric == "api_latency_ms":
            return "INVESTIGATE", f"Latency spike detected for {tenant_id}.", confidence
        else:
            return "INVESTIGATE", f"Anomalous metric {metric} detected for {tenant_id}.", confidence

    def detect_drift(self, tenant_id: str, signals: List[SignalDatapoint]) -> Tuple[bool, float, str, str, float]:
        """
        Runs 3-sigma logic on the signals.
        Returns: (anomaly_bool, severity, suggested_action, reasoning, confidence)
        """
        if not signals:
            return False, 0.0, "ALERT_ONLY", "No signals provided", 1.0

        # Group by signal_name
        signal_dict = {}
        for s in signals:
            if s.signal_name not in signal_dict:
                signal_dict[s.signal_name] = []
            signal_dict[s.signal_name].append(s.value)

        for metric, values in signal_dict.items():
            if len(values) < 3:
                continue # Not enough data to calculate std
            
            baseline_vals = values[:-1]
            last_val = values[-1]
            
            mean_val = np.mean(baseline_vals)
            std_val = np.std(baseline_vals)
            
            if std_val == 0:
                std_val = 1.0 # default small std to allow catching spikes when baseline is perfectly flat

            # Two-tailed: catch both spike UP and drop DOWN
            if last_val > mean_val + 3 * std_val:
                severity = min((last_val - mean_val) / (10 * std_val), 1.0)
                action, reasoning, confidence = self.generate_recommendation(metric, tenant_id)
                return True, round(float(severity), 2), action, reasoning, confidence
            elif last_val < mean_val - 3 * std_val:
                severity = min((mean_val - last_val) / (10 * std_val), 1.0)
                action = "INVESTIGATE"
                reasoning = f"Sudden drop in {metric} for {tenant_id}. Possible service degradation or outage."
                confidence = 0.80
                return True, round(float(severity), 2), action, reasoning, confidence

        return False, 0.0, "ALERT_ONLY", "No anomaly detected within 3-sigma thresholds.", 0.95
