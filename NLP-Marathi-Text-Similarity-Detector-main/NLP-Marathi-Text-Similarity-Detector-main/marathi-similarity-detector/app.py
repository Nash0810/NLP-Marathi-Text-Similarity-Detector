from flask import Flask, render_template, request, jsonify
from model.similarity import calculate_similarity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/similarity', methods=['POST'])
def similarity():
    data = request.json
    text1 = data.get('text1')
    text2 = data.get('text2')

    similarity_score = calculate_similarity(text1, text2)
    return jsonify({'similarity': similarity_score})

if __name__ == '__main__':
    app.run(debug=True)
