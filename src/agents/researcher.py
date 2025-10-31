from src.tools.vector_store import retrieve

def run_rag(query: str, k: int = 5):
    hits = retrieve(query, k=k)
    # keep short snippets
    out = []
    for h in hits:
        snippet = h["text"][:500]
        out.append({"snippet": snippet, "source": h["meta"]["path"]})
    return out

