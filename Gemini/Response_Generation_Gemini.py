import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import spacy
import os

def extract_topics(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    topics = [token.text for token in doc.ents]  # Extract named entities as topics
    return topics

def fetch_information_from_web(topic):
    search_url = f"https://www.google.com/search?q={topic}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        snippets = [p.get_text() for p in soup.find_all("p")[:3]]  # Extract first 3 paragraphs
        return " ".join(snippets)
    return "No relevant information found."

def chat_with_gemini(api_key, model="gemini-2.0-flash"):
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
        
        # Extract topics from user input
        topics = extract_topics(user_input)
        additional_info = ""
        
        for topic in topics:
            additional_info += fetch_information_from_web(topic) + "\n"
        
        # Include full conversation history in the request
        full_context = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation])
        full_context += "\nAdditional Info:\n" + additional_info
        
        response = model.generate_content(full_context)
        reply = response.text
        
        print("AI:", reply)
        conversation.append({"role": "assistant", "content": reply})

# Replace 'your-api-key' with your actual Gemini API key
api_key = os.environ['API_KEY']
model_name = os.environ['Model_Name']

#Invoke GeminAI 
chat_with_gemini(api_key, model_name)
