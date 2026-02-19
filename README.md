# Lexicon

A personal vocabulary learning web app powered by the Claude AI API. Learn one word at a time with AI-generated definitions, examples, and instant feedback on your writing.

## Features

- **AI-generated words** — Claude picks an interesting word with its definition, pronunciation, part of speech, example sentences, synonyms, and a common mistake to avoid
- **Sentence checker** — Write your own sentence using the word and get instant AI feedback on whether you used it correctly
- **Save words** — Bookmark words you want to revisit, saved locally in your browser
- **No repeats** — Words you've already seen in a session are tracked and excluded from future requests
- **Minimalist UI** — Clean, Apple-inspired glassmorphism design

## Tech Stack

- **Backend** — Python, Flask
- **AI** — Anthropic Claude API (`claude-haiku`)
- **Frontend** — HTML, CSS, JavaScript (no frameworks)

## Project Structure

```
lexicon/
├── app.py              # Flask backend and Claude API logic
├── .env                # Your API key 
├── .gitignore
├── requirements.txt
└── templates/
    └── index.html      # Frontend UI
```

## Getting Started

### Prerequisites

- Python 3.9+
- An Anthropic API key — get one at [console.anthropic.com](https://console.anthropic.com)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lexicon.git
   cd lexicon
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv lexvenv
   source lexvenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

### Running the App

```bash
flask --app app.py run --port 8080
```

Then open [http://localhost:8080](http://localhost:8080) in your browser.

## Usage

1. Click **Get my word** to fetch a new vocabulary word
2. Read the definition, pronunciation, and example sentences
3. Write your own sentence in the text box and click **Check my sentence** for AI feedback
4. Click **+ Save word** to add the word to your personal list
5. Click **New word** to get another word — already seen words are automatically excluded

## Environment Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |

## Future Ideas

TBD