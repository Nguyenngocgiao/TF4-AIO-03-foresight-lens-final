from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Optional

from .models import DetectRequest, DetectResponse, VerifyRequest, VerifyResponse
from .engine import AnomalyDetector
from .audit import AuditLogger

app = FastAPI(title="Foresight Lens AI Engine", version="v1.0")
detector = AnomalyDetector()
audit_logger = AuditLogger()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.post("/v1/detect", response_model=DetectResponse)
async def detect_anomaly(
    request: DetectRequest,
    x_tenant_id: str = Header(..., alias="X-Tenant-Id"),
    authorization: str = Header(..., alias="Authorization")
):
    # Detect drift using 3-sigma engine
    anomaly, severity, suggested_action, reasoning, confidence = detector.detect_drift(
        tenant_id=x_tenant_id,
        signals=request.signal_window
    )
    
    # Audit log
    response_data = {
        "anomaly": anomaly,
        "severity": severity,
        "suggested_action": suggested_action,
        "reasoning": reasoning,
        "confidence": confidence
    }
    
    audit_id = audit_logger.log_decision(x_tenant_id, request.model_dump(), response_data)
    
    return DetectResponse(
        anomaly=anomaly,
        severity=severity,
        suggested_action=suggested_action,
        reasoning=reasoning,
        confidence=confidence,
        audit_id=audit_id
    )

@app.post("/v1/verify", response_model=VerifyResponse)
async def verify_state(
    request: VerifyRequest,
    x_tenant_id: str = Header(..., alias="X-Tenant-Id")
):
    # Run 3-sigma on post_state to check if metrics returned to normal
    anomaly, severity, _, _, _ = detector.detect_drift(
        tenant_id=x_tenant_id,
        signals=request.post_state.signal_window
    )
    
    if anomaly:
        return VerifyResponse(
            success=False,
            regression_detected=True,
            next_action="ESCALATE"
        )
    
    return VerifyResponse(
        success=True,
        regression_detected=False,
        next_action="DONE"
    )
