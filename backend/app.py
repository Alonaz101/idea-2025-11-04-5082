from flask import Flask, request, jsonify

app = Flask(__name__)

# Data models (in memory for simplicity)
moods = ["happy", "sad", "energetic", "calm"]
recipes = [
    {"id": 1, "name": "Chocolate Cake", "moods": ["happy"]},
    {"id": 2, "name": "Green Smoothie", "moods": ["energetic", "calm"]},
    {"id": 3, "name": "Comfort Soup", "moods": ["sad"]}
]

@app.route('/api/mood', methods=['POST'])
def mood_recommendation():
    data = request.json
    user_mood = data.get('mood')
    if not user_mood or user_mood not in moods:
        return jsonify({"error": "Invalid or missing mood"}), 400
    matched_recipes = [r for r in recipes if user_mood in r["moods"]]
    return jsonify({"recipes": matched_recipes})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
