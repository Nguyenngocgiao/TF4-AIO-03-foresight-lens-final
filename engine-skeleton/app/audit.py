import uuid
import json
import os
import hashlib
from datetime import datetime, timezone
from typing import Any, Dict

class AuditLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = log_dir
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
    def log_decision(self, tenant_id: str, request_data: Dict[str, Any], response_data: Dict[str, Any]) -> uuid.UUID:
        audit_id = uuid.uuid4()
        now = datetime.now(timezone.utc)
        
        # Hash input for traceability without storing raw PII
        input_hash = hashlib.sha256(json.dumps(request_data, default=str).encode()).hexdigest()[:16]
        
        log_entry = {
            # ≥6 fields as required by Client spec
            "ts": now.isoformat(),
            "tenant_id": tenant_id,
            "audit_id": str(audit_id),
            "correlation_id": str(uuid.uuid4()),
            "input_hash": f"sha256:{input_hash}",
            "model_version": "tf4-3sigma-rolling-v1",
            "ai_call": {
                "decision": response_data.get("suggested_action"),
                "confidence": response_data.get("confidence"),
                "anomaly": response_data.get("anomaly"),
                "severity": response_data.get("severity")
            },
            "encryption": "AES-256-at-rest (S3 SSE-KMS in production)"
        }
        
        log_path = os.path.join(self.log_dir, f"audit_{now.strftime('%Y%m%d')}.jsonl")
        with open(log_path, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
            
        return audit_id
