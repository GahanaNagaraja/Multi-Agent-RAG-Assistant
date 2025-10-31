def critic(answer_text: str) -> dict:
    ok = len(answer_text) > 0
    return {"ok": ok, "notes": None if ok else "No answer generated."}
