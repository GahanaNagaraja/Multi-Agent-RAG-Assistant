from src.app.state import GraphState
from src.agents.planner import plan_query
from src.agents.researcher import run_rag
from src.agents.sql_agent import run_sql_agent
from src.agents.synthesizer import synthesize
from src.agents.critic import critic

def handle_query(user_q: str) -> GraphState:
    st = GraphState(user_query=user_q)

    st.plan = plan_query(user_q)

    rag = run_rag(user_q, k=3) if st.plan["need_docs"] else None
    sqlres = run_sql_agent(user_q) if st.plan["need_sql"] else None

    st.rag_results = rag
    st.sql_results = sqlres

    st.final_answer = synthesize(user_q, rag or [], sqlres)
    _ = critic(st.final_answer)  # simple pass-through for now

    return st
