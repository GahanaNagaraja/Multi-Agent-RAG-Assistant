from src.tools.sql_exec import run_sql

# super simple starter "NL -> SQL" with templates; replace with LC SQL Agent later
def run_sql_agent(query: str):
    ql = query.lower()
    if "complaint" in ql and ("by category" in ql or "top" in ql):
        sql = "SELECT category, COUNT(*) AS n FROM complaints GROUP BY 1 ORDER BY 2 DESC LIMIT 10"
    elif "last" in ql or "q2" in ql:
        sql = "SELECT strftime(date, '%Y-%m') AS month, COUNT(*) AS n FROM complaints GROUP BY 1 ORDER BY 1"
    else:
        sql = "SELECT * FROM complaints LIMIT 10"
    df = run_sql(sql)
    return {"sql": sql, "df": df}
