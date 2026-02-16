import pandas as pd
from dotenv import load_dotenv
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# Load env
load_dotenv()


# =========================
# LLM
# =========================

llm = ChatGroq(

    temperature=0.3,
    model="llama-3.3-70b-versatile"

)


# =========================
# Load Portfolio CSV
# =========================

@st.cache_resource
def load_portfolio():

    df = pd.read_csv("portfolio.csv")

    texts = []

    for _, row in df.iterrows():

        text = f"""

Tech Stack: {row['Tech Stack']}

Use Case: {row['Use Case']}

Results: {row['Results']}

Link: {row['Link']}

"""

        texts.append(text)

    return texts


# =========================
# Create Vector DB
# =========================

@st.cache_resource
def create_vector_db():

    texts = load_portfolio()

    embeddings = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    db = FAISS.from_texts(texts, embeddings)

    return db


# =========================
# Generate Email
# =========================

def generate_email(job_description):

    db = create_vector_db()

    docs = db.similarity_search(job_description, k=1)

    case_study = docs[0].page_content


    prompt = PromptTemplate.from_template(

"""
You are an elite Sales Executive at AtliQ Technologies.

Write a HIGH-CONVERTING cold email.

GOAL:
Get reply from client.

STRICT RULES:

• Include SUBJECT LINE
• Start email with Hi,
• Mention client requirement clearly
• Mention matching case study
• Mention measurable results
• Sound human, confident, premium
• No placeholders
• No fake info
• Under 150 words
• Clean formatting


Job Description:
{job_description}


Case Study:
{case_study}


Output format:

Subject: ...

Hi,

Email body...

Best regards,
AtliQ Technologies

"""

    )


    chain = prompt | llm


    result = chain.invoke({

        "job_description": job_description,

        "case_study": case_study

    })


    return result.content
