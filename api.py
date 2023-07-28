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
        output = pokenum.run(
            game,
            *hand,
            *(board if board else []),
            *(dead if dead else [])
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

