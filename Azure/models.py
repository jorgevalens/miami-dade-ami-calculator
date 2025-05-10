from pydantic import BaseModel, Field
from typing import Optional

class AMICalculationRequest(BaseModel):
    family_size: int = Field(..., ge=1, le=10, description="Number of family members (1-10)")
    income: float = Field(..., ge=0, description="Annual household income")

class AMICalculationResponse(BaseModel):
    percentage_of_ami: float
    category: str
    range_info: str
    eligibility: str

class FeeCalculationRequest(BaseModel):
    assessment_amount: float = Field(..., ge=0, description="Special assessment amount")
    closing_cost_percent: float = Field(..., ge=2, le=5, description="Closing cost percentage (2-5%)")
    setup_fee_percent: float = Field(..., ge=0.5, le=1, description="Setup fee percentage (0.5-1%)")

class FeeCalculationResponse(BaseModel):
    closing_cost: float
    setup_fee: float
    total_fees: float

class RecordingFeeRequest(BaseModel):
    page_count: int = Field(..., ge=1, description="Number of pages in loan commitment package")

class RecordingFeeResponse(BaseModel):
    first_page_fee: float
    additional_pages_fee: float
    total_recording_fee: float 