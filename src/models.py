from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any

@dataclass
class ContentItem:
    id: str
    title: str
    description: str
    source_url: str
    duration: int
    transcript: str
    viral_hooks: List[str]
    variants: List[Dict[str, Any]]
    thumbnail_path: str
    scheduled_time: datetime
    
    def __post_init__(self):
        if not self.id:
            self.id = f"content_{datetime.now().timestamp()}"
        if not self.scheduled_time:
            self.scheduled_time = datetime.now()