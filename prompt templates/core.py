# Load environment variables from the .env file
from dotenv import load_dotenv

# Import ChatPromptTemplate for chat models
from langchain_core.prompts import ChatPromptTemplate

# Import the Mistral chat model
from langchain_mistralai import ChatMistralAI

# Load API key from .env
load_dotenv()

# Initialize the Mistral model
model = ChatMistralAI(model="mistral-small-latest")

# Create the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert information extraction assistant.

Your job is to extract useful information from the given paragraph.

Extract the following details if available:

- Title
- Type
- Genre
- Creator / Author
- Director
- Main Cast
- Main Characters
- Release Year
- End Year
- Total Seasons
- Total Episodes
- Network / Platform
- Language
- Country
- Runtime
- Awards
- Summary
- Important Facts

Rules:
- Extract only information present in the paragraph.
- Do not guess missing information.
- If a field is missing, write "Not Mentioned".
- Keep the summary short (2-4 sentences).
- Present the output in a clean and readable format.
"""
        ),
        (
            "human",
            """
Extract information from this paragraph:

{paragraph}
"""
        ),
    ]
)

# Take paragraph as input from the user
para = input("Give your paragraph: ")

# Format the prompt by replacing {paragraph} with the user's input
final_prompt = prompt.invoke({"paragraph": para})

# Send the formatted prompt to the model
response = model.invoke(final_prompt)

# Print the extracted information
print(response.content)