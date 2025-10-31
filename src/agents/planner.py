import re

def plan_query(q: str) -> dict:
    ql = q.lower()
    need_sql = any(w in ql for w in ["count", "trend", "last", "q1", "q2", "q3", "q4", "increase", "decrease"])
    need_docs = any(w in ql for w in ["policy", "returns", "support", "why", "change"])
    if not (need_sql or need_docs):
        # default: try both; small queries still fine
        need_docs = True; need_sql = True
    return {"need_docs": need_docs, "need_sql": need_sql}

