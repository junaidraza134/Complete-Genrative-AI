from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("RAG/document_loaders/notes.pdf")
docs = data.load()

print(docs[0])