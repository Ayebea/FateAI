# FateAI

Welcome to FateAI. This is a project which uses AI to orchestrate an immersive storytelling experience. Users can 
randomly generate a story or make their own customized story. Here are the features and how to use them:

- Quickstart
  - Randomly generates a story for users to interact with.
- Detailed Start
  - Allows users to customize story variables.
- Input "End Story." to end a session and "Save Story." to save your progress.

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Mistral model pulled: `ollama pull mistral`

## How to Run
1. Clone the repository
2. Install dependencies: `pip install ollama`
3. Run: `python funscript.py`

## Storage
Stories are saved locally to a `saves/` folder as JSON files. No data is sent to external servers.