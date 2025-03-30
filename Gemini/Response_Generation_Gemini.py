import google.generativeai as genai
import os

def chat_with_gemini(api_key, model):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model)
    
    print("Chat with Gemini AI! Type 'exit' to stop.")
    conversation = []  # Store conversation history
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        conversation.append({"role": "user", "content": user_input})
        response = model.generate_content(user_input)
        reply = response.text
        
        print("AI:", reply)
        conversation.append({"role": "assistant", "content": reply})

# Replace 'your-api-key' with your actual Gemini API key
api_key = os.environ['API_KEY']
model_name = os.environ['Model_Name']

#Invoke to Chat
chat_with_gemini(api_key, model_name)
