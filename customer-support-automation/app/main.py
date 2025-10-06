from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
import logging

from src.crew.support_crew import SupportCrew
from src.config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Customer Support Automation API",
    description="Multi-agent customer support automation system",
    version="1.0.0"
)

class CustomerInquiry(BaseModel):
    customer: str
    person: str
    inquiry: str
    metadata: Optional[Dict[str, Any]] = None

class SupportResponse(BaseModel):
    success: bool
    response: Optional[str] = None
    error: Optional[str] = None
    processing_time: Optional[float] = None

@app.on_event("startup")
async def startup_event():
    """Initialize the support crew on startup"""
    logger.info("Initializing Support Crew...")
    app.state.support_crew = SupportCrew()
    logger.info("Support Crew initialized successfully")

@app.post("/support/inquiry", response_model=SupportResponse)
async def process_support_inquiry(inquiry: CustomerInquiry):
    """Process a customer support inquiry"""
    try:
        import time
        start_time = time.time()
        
        logger.info(f"Processing inquiry from {inquiry.customer}")
        
        # Process the inquiry
        result = app.state.support_crew.process_inquiry(inquiry.dict())
        
        processing_time = time.time() - start_time
        logger.info(f"Inquiry processed in {processing_time:.2f} seconds")
        
        return SupportResponse(
            success=True,
            response=str(result),
            processing_time=processing_time
        )
        
    except Exception as e:
        logger.error(f"Error processing inquiry: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error processing inquiry: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "customer-support-automation"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Set to False in production
    )