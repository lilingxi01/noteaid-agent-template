import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env'))

from flask import Flask
from flask_cors import CORS
from handler import MyAgent
from notebridge import make_executor

app = Flask(__name__)
agent = MyAgent()
executor = make_executor(agent=agent)

allowed_origins = [
    "http://localhost:3000",  # Local development
    r"https://\w+\.noteaid\.app"  # Regex for subdomains of NoteAid official domain.
]
CORS(app, origins=allowed_origins)


@app.route('/', methods=['POST', 'OPTIONS'])
def home():
    return executor()


if __name__ == "__main__":
    app.run(debug=True, port=4680)
