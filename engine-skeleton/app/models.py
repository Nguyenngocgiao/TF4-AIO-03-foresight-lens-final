from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

class TimeRange(BaseModel):
    start_ts: datetime
    end_ts: datetime

class DetectContext(BaseModel):
    deployment_version: str
    time_range: TimeRange

class SignalDatapoint(BaseModel):
    ts: datetime
    signal_name: str
    value: float
    labels: Optional[Dict[str, Any]] = None

class DetectRequest(BaseModel):
    signal_window: List[SignalDatapoint]
    context: DetectContext

class DetectResponse(BaseModel):
    anomaly: bool
    severity: float = Field(ge=0.0, le=1.0)
    suggested_action: str
    reasoning: str = Field(max_length=300)
    confidence: float = Field(ge=0.0, le=1.0)
    audit_id: uuid.UUID

class ActionTaken(BaseModel):
    type: str
    params: Dict[str, Any]
    ts: datetime

class PostState(BaseModel):
    signal_window: List[SignalDatapoint]

class VerifyRequest(BaseModel):
    action_taken: ActionTaken
    post_state: PostState

class VerifyResponse(BaseModel):
    success: bool
    regression_detected: bool
    next_action: str
