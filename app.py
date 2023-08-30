#pip install flask requests
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your MusicGen API endpoint
MUSICGEN_API_URL = 'https://api.musicgen.com/generate'

@app.route('/generate_music', methods=['POST'])
def generate_music():
    try:
        data = request.json

        # Extract emotion from the request data
        emotion = data.get('emotion')

        # Make a request to MusicGen API
        response = requests.post(MUSICGEN_API_URL, json={'emotion': emotion})

        # Return the generated music data
        return jsonify(response.json()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
