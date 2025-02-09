from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Lucid Dream Mentor!"

@app.route('/recommend-music', methods=['GET'])
def recommend_music():
    goal = request.args.get('goal', 'sleep')
    if goal == 'lucid':
        return jsonify({"message": "Recommended: Theta Waves Music", "link": "https://www.youtube.com/watch?v=VIDEO_ID"})
    else:
        return jsonify({"message": "Recommended: Delta Waves Music", "link": "https://www.youtube.com/watch?v=VIDEO_ID"})

if __name__ == '__main__':
    app.run(debug=True)