
# for query
# from dotenv import load_dotenv
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# load_dotenv()

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/gemini-embedding-001"
# )

# vector = embeddings.embed_query("You are going to learn Gen AI")

# print(vector)
# print(len(vector))



# for docoument
# Import load_dotenv() to load environment variables from the .env file
from dotenv import load_dotenv

# Import Google's Embedding model from LangChain
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load the GOOGLE_API_KEY from the .env file
load_dotenv()

# Create an Embedding Model object
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Sentence that we want to convert into an embedding vector
text = "You are going to learn Gen AI"

# Convert the sentence into a vector (embedding)
vector = embeddings.embed_query(text)

# Print the original sentence
print("Original Text:")
print(text)

print("\n" + "=" * 60)

# Print the embedding vector
print("Embedding Vector:")
print(vector)

print("\n" + "=" * 60)

# Print the dimension (length) of the vector
print("Vector Dimension:")
print(len(vector))
