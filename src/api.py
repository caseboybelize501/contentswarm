import asyncio
import logging
from typing import Dict, Any
from datetime import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from .main import main

logger = logging.getLogger(__name__)

app = FastAPI(title="ContentSwarm API")


class ContentRequest(BaseModel):
    url: str
    platform: str = "all"
    

class ContentResponse(BaseModel):
    id: str
    title: str
    status: str
    created_at: datetime
    

@ app.post("/process", response_model=ContentResponse)
async def process_content(request: ContentRequest):
    try:
        logger.info(f"Processing content from {request.url}")
        
        # Run main processing
        content_item = await main()
        
        response = ContentResponse(
            id=content_item.id,
            title=content_item.title,
            status="completed",
            created_at=content_item.scheduled_time
        )
        
        logger.info(f"Content processing completed: {content_item.id}")
        return response
        
    except Exception as e:
        logger.error(f"Error processing content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@ app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)