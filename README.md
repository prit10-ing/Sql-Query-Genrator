# 📊 SQL Generator + Learning Assistant (LangChain)

An AI-powered tool that converts natural language into SQL queries and also provides learning tips to help users understand how to solve similar problems.

---

## 🚀 Features

- Convert English questions → SQL queries
- Supports dynamic database schema input
- Provides learning tips for each query
- Clean and modern Streamlit UI
- Uses open-source LLM via HuggingFace

---

## 🧩 Tech Stack

- LangChain (PromptTemplate + LCEL)
- HuggingFace Endpoint (LLM)
- Streamlit (Frontend)
- Python
- dotenv (for API keys)

---

## 💡 Example

### Input:
**Schema:**

Table: orders
Columns: customer_id, order_date, amount, product_id


**Query:**


---

### Output:

**SQL Query:**
```sql
SELECT customer_id, SUM(amount) AS total_sales
FROM orders
GROUP BY customer_id
ORDER BY total_sales DESC
LIMIT 5;

Tips:

Use GROUP BY for aggregation
Use SUM() to calculate totals
Use ORDER BY with LIMIT for top results

🧠 How it Works
User inputs schema and query
PromptTemplate structures the request
LLM generates SQL + tips
Output is displayed in UI
🎯 Learning Outcome
Prompt engineering
SQL query generation using LLMs
LangChain chaining (prompt | model | parser)
Building real-world GenAI apps
🔮 Future Improvements
Support multiple tables (JOIN queries)
Add chat-based UI
Deploy online
Add query explanation mode
📌 Author

Pritesh
(Data Science & GenAI Enthusiast)