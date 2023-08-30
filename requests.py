from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate_music', methods=['POST'])
def generate_music():
    try:
        data = request.json

        # Extract emotion from the request data
        emotion = data.get('emotion')

        # Replace this with your MusicGen integration logic
        generated_music = {'emotion': emotion, 'music': 'Generated music data'}

        return jsonify(generated_music), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
