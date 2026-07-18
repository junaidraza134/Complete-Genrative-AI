from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser

# Load environment variables
load_dotenv()

# Initialize the Mistral model
model = ChatMistralAI(
    model="mistral-small-latest"
)

# Define the structure of the output
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


# Create Pydantic output parser
parser = PydanticOutputParser(
    pydantic_object=Movie
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the given paragraph.

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])

# Take paragraph from user
para = input("Give your paragraph: ")

# Fill dynamic values in the prompt
final_prompt = prompt.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})

# Send final prompt to the model
response = model.invoke(final_prompt)

# Convert LLM output into a validated Movie object
result = parser.parse(response.content)

# Print structured output
print(result)

