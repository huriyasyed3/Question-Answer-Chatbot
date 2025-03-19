import google.generativeai as genai  # for google genai api
from dotenv import load_dotenv  # for loading environment variables
import os  # for environment variables

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Start Chat Loop
while True:
    user_input = input("\nEnter your question (or 'quit' to exit): ")

    # Correct indentation of if condition
    if user_input.lower() == 'quit':
        print("Thanks for chatting! Goodbye!")
        break  # Exit the loop

    # Fix typo in variable name (response instead of resposne)
    response = model.generate_content(user_input)

    # Print response text
    print(response.text)
