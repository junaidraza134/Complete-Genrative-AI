from langchain_community.document_loaders import TextLoader

data = TextLoader("RAG/document_loaders/notes.txt")
docs = data.load()

# print(docs[0])

print(len(docs))