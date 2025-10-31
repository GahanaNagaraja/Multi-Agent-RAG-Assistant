import streamlit as st
from src.app.orchestrator import handle_query

st.set_page_config(page_title="Multi-Agent RAG Assistant", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Agent RAG Assistant (MVP)")

q = st.text_input("Ask a question", value="Why did complaints increase in Q2? Include drivers and a data preview.")
if st.button("Run") or q:
    st.write("Running…")
    state = handle_query(q)
    st.subheader("Plan")
    st.json(state.plan)
    if state.rag_results:
        st.subheader("Doc snippets")
        for r in state.rag_results:
            with st.expander(r["source"]):
                st.write(r["snippet"])
    if state.sql_results:
        st.subheader("SQL")
        st.code(state.sql_results["sql"])
        st.dataframe(state.sql_results["df"].head(10))
    st.subheader("Final Answer")
    st.markdown(state.final_answer)
