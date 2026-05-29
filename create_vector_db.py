from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load text files from data folder
loader = DirectoryLoader("data", glob="*.txt", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})

documents = loader.load()

# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

# Create embeddings model
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store embeddings in ChromaDB
db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="vectordb"
)

db.persist()

print("Vector database created successfully")