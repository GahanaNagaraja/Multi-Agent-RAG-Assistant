from textwrap import dedent

def synthesize(user_q: str, rag, sqlres=None):
    bullets = []
    cites = []
    if rag:
        b = f"- From docs: {rag[0]['snippet'][:120].strip()}..."
        bullets.append(b); cites.append(rag[0]['source'])
    if sqlres:
        head = sqlres["df"].head(5).to_markdown(index=False)
        bullets.append(f"- From data (preview):\n{head}")
    answer = dedent(f"""
    ## Answer
    Question: {user_q}

    Key points:
    {chr(10).join(bullets)}

    Sources: {', '.join(sorted(set(cites))) if cites else 'n/a'}
    """).strip()
    return answer 
