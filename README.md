
# SteamDB Game API

This is a simple API built with FastAPI that allows users to retrieve information about games. The API uses a MongoDB database to store and retrieve game data.

## Endpoints

* `GET /game/{name}`: Returns information about the game with the specified name
* `GET /games/top/{amount}`: Returns the top `amount` highest rated games
## Installation

1) Clone the repository:

```bash
  git clone https://github.com/OriginalDCAM/fastapi-game-api.git
```
2) Install the dependencies:

```bash
  pip install -r requirements.txt
```
3) Set up a MongoDB database and update the connection string in: `games.py`

4) Import the `steamdb.json` file into the MongoDB Database

## Usage

5) Start the API:

```bash
  uvicorn  main:app
```
6) Send requests to the endpoints listed above.

## Dependencies

* FastAPI
* Motor (asyncio-base Python driver for MongoDB)


## Authors

- [@OriginalDCAM](https://www.github.com/OriginalDCAM)

