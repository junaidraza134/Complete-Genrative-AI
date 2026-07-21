# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# model = ChatMistralAI(
#     model="mistral-small-latest",   # or "mistral-large-latest"
#     temperature=0.9
# )
# messages=[]        #its list which story the conversation basically it is temporarly
# while(True):
#     print("--------Welcome type 0 to exit the application-----")
#     prompt=input("You: ")
#     messages.append(prompt)
#     if(prompt=="0"):
#         break
#     response = model.invoke(messages) 
#     messages.append(response.content)
#     print("Bot: ",response.content)


# # this chatbot store the conversation in permenent by langchain library
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# # Load all environment variables from the .env file
# load_dotenv()

# # Create the Mistral AI model
# model = ChatMistralAI(
#     model="mistral-small-latest",   # Model name
#     temperature=0.9                 # Controls the creativity of the model
# )
# print("Chose your AI mode")
# print("press 1 for Angry mode")
# print("press 2 for funny mode")
# print("press 3 for sad mode")

# choice=int(input("tell your response:- "))
# if choice==1:
#     mode="You are an angry AI agnet. You respond agressively and impatiently."
# elif choice==2:
#     mode="You are very funny AI agent. You respond with humor and jokes."
# elif choice==3:
#     mode="You are an Sad AI agent. You respond in sad way"
# # Store the conversation history
# messages = [
#     # System message defines the AI's behavior
#     SystemMessage(content=mode)
# ]

# # Infinite loop for continuous conversation
# while(True):

#     # Display the welcome message
#     print("--------Welcome type 0 to exit the application-----")

#     # Take input from the user
#     prompt = input("You: ")

#     # Add the user's message to the conversation history
#     messages.append(HumanMessage(content=prompt))

#     # Exit the application if the user enters 0
#     if(prompt == "0"):
#         break

#     # Send all previous messages to the model
#     response = model.invoke(messages)

#     # Store the AI's response in the conversation history
#     messages.append(AIMessage(content=response.content))

#     # Display the AI's response
#     print("Bot: ", response.content)

# # Print the complete conversation history
# print(messages)