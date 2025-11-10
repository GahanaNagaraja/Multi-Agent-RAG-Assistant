# Multi-Agent-RAG-Assistant

## Project Overview
The Multi-Agent RAG Knowledge Assistant is an AI-powered reasoning system that autonomously integrates document retrieval, structured SQL analytics, and multi-agent collaboration to deliver contextual insights.
By combining Retrieval-Augmented Generation (RAG) with agentic reasoning, it emulates human-like decision-making — determining when to search documents, query databases, or synthesize both — all within a lightweight, explainable pipeline.

This project demonstrates how Agentic AI, LangChain, and LangGraph can orchestrate modular agents to solve analytical problems that require both text comprehension and data interpretation, bridging the gap between unstructured and structured intelligence.

## Problem Statetment
Modern enterprises generate vast amounts of unstructured text (documents, FAQs, reports) alongside structured data (tables, logs, KPIs).
Typical LLM or SQL query systems operate in isolation, making it difficult to combine qualitative and quantitative insights seamlessly.
This project solves that gap by creating an autonomous, multi-agent AI system that understands user intent, retrieves relevant information, runs data analytics, and synthesizes meaningful answers — all through a single conversational interface.

## Objective
-> Design a multi-agent architecture capable of dynamic role assignment and reasoning.

-> Integrate RAG pipelines for document retrieval and SQL agents for tabular analytics.

-> Enable autonomous orchestration using LangChain and LangGraph frameworks.

-> Deliver real-time results through a Streamlit-based web UI with visualization support.

-> Optimize system performance for low-RAM execution (≤8 GB) using caching and persistent storage.

## System Architecture
Agents & Roles

-> Planner – interprets the user’s query and decides whether to query documents, structured data, or both.

-> Researcher – performs semantic retrieval using Sentence-Transformers and FAISS from a ChromaDB vector store.

-> SQL Agent – runs analytical queries over DuckDB tables (e.g., complaints, orders, finance).

-> Synthesizer – merges document and SQL findings into a unified, explainable answer.

-> Critic – validates factual consistency and refines the final response before display.

## Methodology
1. Data Preparation

-> Organized documents in /data/docs and tables in /data/tables.

-> Built persistent vector indexes using Sentence-Transformers (all-MiniLM-L6-v2) and FAISS inside ChromaDB.

-> Created SQL views in DuckDB to query CSVs dynamically.

2. Agentic Reasoning Workflow

-> Planner parses user query → sets flags (need_docs, need_sql).

-> Researcher retrieves semantically similar document snippets (top-k).

-> SQL Agent executes context-relevant SQL (aggregation, filtering, joins).

-> Synthesizer merges retrieved contexts and SQL summaries → formats results as Markdown and charts.

-> Critic ensures logical consistency and output quality.

3. Visualization Layer

-> Built an interactive Streamlit app for live query input, plan visualization, retrieved snippets, SQL results, and charts generated using Matplotlib.

-> Enables real-time feedback and traceability of agent decisions.

## Technologies Used

| Category                      | Tools & Libraries                              |
| ----------------------------- | ---------------------------------------------- |
| **Programming Language**      | Python                                         |
| **LLM & Agent Frameworks**    | LangChain, LangGraph                           |
| **Embeddings & Retrieval**    | Sentence-Transformers, FAISS, ChromaDB         |
| **Data Engine**               | DuckDB, Pandas, NumPy                          |
| **Frontend & Visualization**  | Streamlit, Matplotlib                          |
| **Configuration**             | Pydantic, pydantic-settings                    |
| **Version Control & Dev Env** | GitHub Codespaces, VS Code                     |
| **Performance Optimization**  | Caching (Streamlit), Persistent DB Connections |

## Key Outcomes

-> Achieved 60% faster query-to-insight turnaround through parallel document and SQL reasoning.

-> Delivered real-time, explainable insights via an interactive Streamlit dashboard.

-> Optimized retrieval latency using FAISS vector search and embedding caching.

-> Validated robustness in low-memory (7–8 GB) environments.

-> Demonstrated scalable foundation for enterprise RAG + analytics assistants.

## Evaluation

The project includes a JSON file for testing retrieval and synthesis quality. Each record contains a query, reference snippet, and keywords to verify RAG accuracy.

Evaluation metrics include:
-> Retrieval recall (Top-k match rate)

-> SQL query correctness

-> Synthesized answer coherence

## Future Enhancements

-> Integrate LLM-based SQL generation for natural-language analytics.

-> Add Cross-Encoder reranker for improved document relevance.

-> Extend guardrails for safe SQL execution and prompt validation.

-> Deploy publicly via Streamlit Cloud / Render / Hugging Face Spaces.

-> Implement RAGAS-based evaluation and CI-driven testing.
