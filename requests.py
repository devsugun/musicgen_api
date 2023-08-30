import requests

# Replace with your API endpoint
API_URL = 'http://127.0.0.1:5000/generate_music'

emotion = 'joyful'  # Replace with the actual user's emotion

data = {'emotion': emotion}
response = requests.post(API_URL, json=data)

if response.status_code == 200:
    generated_music = response.json()
    # Process the generated_music data as needed
    print(generated_music)
else:
    print(f"Error: {response.status_code}")
