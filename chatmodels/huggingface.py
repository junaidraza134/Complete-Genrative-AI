from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deadbydawn101/gemma-4-E4B-Agentic-Opus-Reasoning-GeminiCLI-GGUF",
    temperature=0.7,
    max_new_tokens=1024,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)