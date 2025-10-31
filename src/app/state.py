from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class GraphState(BaseModel):
    user_query: str
    plan: Dict[str, Any] | None = None
    rag_results: List[dict] | None = None
    sql_results: Dict[str, Any] | None = None
    final_answer: str | None = None
