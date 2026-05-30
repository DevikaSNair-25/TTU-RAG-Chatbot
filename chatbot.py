import os
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="vectordb", embedding_function=embedding)
retriever = db.as_retriever()

def ask(question):
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""You are a helpful assistant for TTU (Tatung University of Technology) in Taiwan.
Use the following context to answer the question.
Always answer in English even if the context is in Chinese.
If you cannot find the answer in the context, say "I don't have that information."

Context:
{context}

Question: {question}
Answer:"""

    response = llm.invoke(prompt)
    return response.content
