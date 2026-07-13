# this model for Gemini 
# from dotenv import load_dotenv
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
# )

# response = model.invoke("Give me tips for lose weigth?")
# print(response.content)

#this model for groq
# from dotenv import load_dotenv
# import os
# from langchain_groq import ChatGroq
# load_dotenv()
# model=ChatGroq(model="llama-3.3-70b-versatile",temperature=0.9,
# api_key=os.getenv("GROQ_API_KEY"),
# )

# response=model.invoke("Give me tips about lose weight")
# print(response.content)

#this model for mistral

# from dotenv import load_dotenv
# import os
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# model = ChatMistralAI(
#     model="mistral-large-latest",temprature=0.9,
#     api_key=os.getenv("MISTRAL_API_KEY"),
# )

# response = model.invoke("write a poem on AI.")
# print(response.content)


#stream(chunks)
# from dotenv import load_dotenv
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()
# model=ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY"),
# )

# for chunk in model.stream("Why do parrots have colorful feathers?"):
#     print(chunk.text,end="|",flush=True)


#batches
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
responses = model.batch([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
])

for response in responses:
    print(response.content)
    print("-" * 50)
