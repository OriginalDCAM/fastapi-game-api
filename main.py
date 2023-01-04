from fastapi import FastAPI

import games

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/game/{name}")
async def get_game(name: str):
    result = await games.read_game(name)
    return result


@app.get("/games/top/{amount}")
async def get_most_highest_rated_games(amount: int):
    results = await games.get_top_20_games(amount)
    return results



