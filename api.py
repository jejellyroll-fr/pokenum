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
    game: str
    hand: List[str]
    board: Optional[list] = []
    dead: Optional[list] = []
    method: Optional[str] = None
    iterations: Optional[str] = None
    histogram: bool = False


@app.post('/pokenum')
async def run_pokenum_api(request: PokenumRequest):
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
        if board and not dead and not method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *board)
        elif dead and not board and not method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *dead)
        elif board and dead and not method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *board, *dead)
        elif not board and not dead and method and not iterations and not histogram:
            output = pokenum.run(game, *hand, method=method)
        elif not board and not dead and not method and iterations and not histogram:
            output = pokenum.run(game, *hand, iterations=iterations)
        elif not board and not dead and not method and not iterations and histogram:
            output = pokenum.run(game, *hand, histogram=histogram)
        elif board and not dead and method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *board, method=method)
        elif board and not dead and not method and iterations and not histogram:
            output = pokenum.run(game, *hand, *board, iterations=iterations)
        elif board and not dead and not method and not iterations and histogram:
            output = pokenum.run(game, *hand, *board, histogram=histogram)
        elif dead and not board and method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *dead, method=method)
        elif dead and not board and not method and iterations and not histogram:
            output = pokenum.run(game, *hand, *dead, iterations=iterations)
        elif dead and not board and not method and not iterations and histogram:
            output = pokenum.run(game, *hand, *dead, histogram=histogram)
        elif board and dead and method and not iterations and not histogram:
            output = pokenum.run(game, *hand, *board, *dead, method=method)
        elif board and dead and not method and iterations and not histogram:
            output = pokenum.run(game, *hand, *board, *dead, iterations=iterations)
        elif board and dead and not method and not iterations and histogram:
            output = pokenum.run(game, *hand, *board, *dead, histogram=histogram)
        elif not board and not dead and method and iterations and not histogram:
            output = pokenum.run(game, *hand, method=method, iterations=iterations)
        elif not board and not dead and method and not iterations and histogram:
            output = pokenum.run(game, *hand, method=method, histogram=histogram)
        elif not board and not dead and not method and iterations and histogram:
            output = pokenum.run(game, *hand, iterations=iterations, histogram=histogram)
        elif board and dead and method and iterations and not histogram:
            output = pokenum.run(game, *hand, *board, *dead, method=method, iterations=iterations)
        elif board and dead and method and not iterations and histogram:
            output = pokenum.run(game, *hand, *board, *dead, method=method, histogram=histogram)
        elif board and dead and not method and iterations and histogram:
            output = pokenum.run(game, *hand, *board, *dead, iterations=iterations, histogram=histogram)
        elif not board and not dead and method and iterations and histogram:
            output = pokenum.run(game, *hand, method=method, iterations=iterations, histogram=histogram)
        elif board and not dead and method and iterations and not histogram:
            output = pokenum.run(game, *hand, *board, method=method, iterations=iterations)
        elif board and not dead and method and not iterations and histogram:
            output = pokenum.run(game, *hand, *board, method=method, histogram=histogram)
        elif board and not dead and not method and iterations and histogram:
            output = pokenum.run(game, *hand, *board, iterations=iterations, histogram=histogram)
        elif dead and not board and method and iterations and not histogram:
            output = pokenum.run(game, *hand, *dead, method=method, iterations=iterations)
        elif dead and not board and method and not iterations and histogram:
            output = pokenum.run(game, *hand, *dead, method=method, histogram=histogram)
        elif dead and not board and not method and iterations and histogram:
            output = pokenum.run(game, *hand, *dead, iterations=iterations, histogram=histogram)
        elif not board and not dead and method and iterations and histogram:
            output = pokenum.run(game, *hand, method=method, iterations=iterations, histogram=histogram)
        elif board and dead and method and iterations and histogram:
            output = pokenum.run(game, *hand, *board, *dead, method=method, iterations=iterations, histogram=histogram)
        else:
            output = pokenum.run(game, *hand)

        logger.debug(f"Response: {output}")
        logger.debug(type(output))
        return JSONResponse(content=output)
    except Exception as e:
        logger.error(f"Error: {e}")
        return {'error': str(e)}

if __name__ == "__main__":
    import uvicorn

    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    host = "127.0.0.1"
    port = 8000
    uvicorn.run(app, host=host, port=port)

