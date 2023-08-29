import os
import logging
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pokenum import Pokenum
from logger import configure_logger
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI()
pokenum = Pokenum()
templates = Jinja2Templates(directory="templates")

# Configure logging using the logger module
log_file = os.path.join("logs", "debug.log")
configure_logger(log_file)

class PokenumRequest(BaseModel):
    """
    A data model class representing a Pokenum request.

    This class defines the structure of a Pokenum request, including the game, hand, board, dead, method, iterations, and histogram attributes.

    Attributes:
        game (str): The game attribute of the Pokenum request.
        hand (List[str]): The hand attribute of the Pokenum request.
        board (Optional[list]): The board attribute of the Pokenum request. Defaults to an empty list.
        dead (Optional[list]): The dead attribute of the Pokenum request. Defaults to an empty list.
        method (Optional[str]): The method attribute of the Pokenum request. Defaults to None.
        iterations (Optional[str]): The iterations attribute of the Pokenum request. Defaults to None.
        histogram (bool): The histogram attribute of the Pokenum request. Defaults to False.

    """

    game: str
    hand: List[str]
    board: Optional[list] = []
    dead: Optional[list] = []
    method: Optional[str] = None
    iterations: Optional[str] = None
    histogram: bool = False


@app.post('/pokenum')
async def run_pokenum_api(request: PokenumRequest):
    """
    Handles the POST request to '/pokenum' endpoint.

    This function receives a PokenumRequest object as input and runs the 'pokenum' program with the specified parameters. It logs the received request and the response, and returns the output in JSON format.

    Args:
        request (PokenumRequest): The PokenumRequest object containing the request parameters.

    Returns:
        JSONResponse: The output of the 'pokenum' program in JSON format.

    """

    game = request.game
    hand = request.hand
    board = request.board
    dead = request.dead
    method = request.method
    iterations = request.iterations
    histogram = request.histogram

    logger = logging.getLogger("pokenum")
    logger.debug(f"Received request with game={game}, hand={hand}, board={board}, dead={dead}, method={method}, iterations={iterations}, histogram={histogram}")

    try:
        output = pokenum.run(
            game,
            *hand,
            *(board or []),
            *(dead or [])
        )



        logger.debug(type(output))
        logger.debug(f"Response: {output}")

        return JSONResponse(content=output)
    except Exception as e:
        logger.error(f"Error: {e}")
        return {'error': str(e)}

if __name__ == "__main__":
    import uvicorn

    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    host = "0.0.0.0"  # Update the host to allow external access
    port = 8000
    uvicorn.run(app, host=host, port=port)

