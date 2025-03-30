# Chat with Gemini AI

This project allows users to chat with Google's Gemini AI while also fetching relevant web information based on extracted topics from user input. It uses `spacy` for Named Entity Recognition (NER), `BeautifulSoup` for web scraping, and Google's `generativeai` package to interact with Gemini AI.

## Features
- Extracts topics from user input using `spaCy`.
- Fetches additional information from the web related to the extracted topics.
- Maintains conversation history for better AI responses.
- Uses Google's Gemini AI (`gemini-2.0-flash`) for generating responses.

## Prerequisites
Before running the project, ensure you have the following:
- Python 3.7 or later installed.
- Required dependencies installed:

```bash
pip install google-generativeai requests beautifulsoup4 spacy
python -m spacy download en_core_web_sm
```

- A valid Google Gemini AI API key.
- Set up environment variables:

```bash
export API_KEY='your-google-gemini-api-key'
export Model_Name='gemini-2.0-flash'
```

## Installation & Usage
1. Clone this repository:

```bash
git clone https://github.com/yourusername/chat-with-gemini.git
cd chat-with-gemini
```

2. Run the script:

```bash
python chat_with_gemini.py
```

3. Start chatting! Type your messages, and the AI will respond with relevant information.

4. To exit, type `exit`.

## Code Overview
- `extract_topics(text)`: Uses `spaCy` to extract named entities from the user input.
- `fetch_information_from_web(topic)`: Uses `BeautifulSoup` to scrape Google search results for additional topic information.
- `chat_with_gemini(api_key, model)`: Manages the chat interface, sending messages to Gemini AI with the conversation history and fetched information.

## Notes
- Web scraping results may vary based on Google's restrictions.
- Ensure compliance with Google's scraping policies when using `BeautifulSoup`.
- This script is for educational purposes and should not be used for extensive automated web scraping.
- 
## Contributions
Feel free to fork this repository and submit pull requests with improvements or bug fixes!
