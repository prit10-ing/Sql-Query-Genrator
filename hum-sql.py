import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="SQL AI Assistant", page_icon="📊", layout="wide")

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}
.stTextInput input, .stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
}
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>📊 SQL Generator + Learning Tips</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Turn natural language into SQL & learn how to solve it 🚀</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    schema = st.text_area("📂 Enter Table Schema", height=200, placeholder="""
Table: orders
Columns:
- customer_id
- order_date
- amount
- product_id
""")

with col2:
    question = st.text_area("❓ Enter Your Question", height=200, placeholder="e.g. Get top 5 customers by total sales")

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b:groq",
    task="text-generation",
    max_new_tokens=400,
    temperature=0.3
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt = PromptTemplate(
    input_variables=["question", "schema"],
    template="""
You are an expert SQL developer and teacher.

Schema:
{schema}

User Question:
{question}

Generate:
1. SQL Query
2. 2-3 learning tips

Format:

SQL Query:
<query>

Tips:
- tip 1
- tip 2
- tip 3
"""
)

chain = prompt | model | parser

if st.button("🚀 Generate SQL"):
    if schema and question:
        with st.spinner("Generating..."):
            result = chain.invoke({
                "question": question,
                "schema": schema
            })

            if "Tips:" in result:
                sql_part, tips_part = result.split("Tips:")

                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader("🧾 SQL Query")
                st.code(sql_part.replace("SQL Query:", "").strip(), language="sql")
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.subheader("💡 Learning Tips")
                st.write(tips_part.strip())
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.write(result)
    else:
        st.warning("⚠️ Please fill both Schema and Question")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Built with ❤️ using LangChain</p>", unsafe_allow_html=True)