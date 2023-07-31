from flask import Flask, render_template, jsonify, request, send_from_directory
import requests
from logger import configure_logger
import os
import logging
from api import PokenumRequest
from flask import Flask, render_template, jsonify
import jinja2
import json

app = Flask(__name__)

# Register the json_loads filter
app.jinja_env.filters['json_loads'] = json.loads


log_file = "logs/debug.log"
configure_logger(log_file)

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    """
    Renders the index.html template.

    This function logs the rendering of the index.html template and returns the rendered template.

    Returns:
        str: The rendered index.html template.

    """

    logger.info('Rendering index.html')
    return render_template('index.html')

@app.route('/app/gfx/white/<path:filename>')
def serve_static(filename):
    """
    Serves static files from the 'gfx/white' directory.

    This function serves static files from the 'gfx/white' directory based on the provided filename.

    Args:
        filename (str): The name of the file to be served.

    Returns:
        Response: The response containing the requested file.

    """

    root_dir = os.path.dirname(os.path.abspath(__file__))
    white_gfx_dir = os.path.join(root_dir, 'gfx', 'white')
    return send_from_directory(white_gfx_dir, filename)


@app.route('/pokenum', methods=['POST'])
def run_pokenum_flask():
    """
    Handles the POST request to '/pokenum' endpoint using Flask.

    This function retrieves the request parameters from the form data, sends a POST request to the 'http://localhost:8000/pokenum' endpoint with the parameters in JSON format, and renders the 'pokenum.html' template with the response data.

    Returns:
        Response: The rendered 'pokenum.html' template.

    """

    try:
        game = request.form['game']
        hand = request.form['hand'].split()
        board = request.form['board'].split()
        dead = request.form['dead'].split()
        method = request.form['method']
        iterations = request.form['iterations']
        histogram = request.form.get('histogram', False)

        logger.debug(f"hand: {hand}")
        logger.debug(f"Received parameters: game={game}, hand={hand}, board={board}, dead={dead}, method={method}, iterations={iterations}, histogram={histogram}")

        url = 'http://localhost:8000/pokenum'
        headers = {'Content-Type': 'application/json'}
        payload = PokenumRequest(game=game, hand=hand, board=board, dead=dead, method=method, iterations=iterations, histogram=histogram).dict()
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return render_template('pokenum.html', result=result)
    except KeyError as e:
        logger.error(f"Missing parameter: {str(e)}")
        return jsonify({'error': f'Missing parameter: {str(e)}'})
    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': str(e)})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

