from flask import Flask, render_template, request, jsonify

from api import FastAPI

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokenum', methods=['POST'])
def run_pokenum():
    game = request.form['game']
    hand = request.form['hand']
    board = request.form['board']
    dead = request.form['dead']
    method = request.form['method']
    iterations = request.form['iterations']
    histogram = request.form['histogram']

    try:
        response = fastapi.post('/pokenum', json={'game': game, 'hand': hand, 'board': board, 'dead': dead, 'method': method, 'iterations': iterations, 'histogram': histogram})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
