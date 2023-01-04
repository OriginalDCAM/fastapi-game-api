import motor.motor_asyncio

client = motor.motor_asyncio\
    .AsyncIOMotorClient('ENTER_YOUR_CONNECTION_STRING_HERE')

db = client.GamesSearch

games_collection = db.Games


async def read_game(game_name: str):
    result = await games_collection.find_one({"name": game_name}, {'_id': 0})
    return result


async def get_top_20_games(amount: int):
    cursor = games_collection.find({}, {'_id': 0}).sort("meta_score", -1).limit(amount)
    games = []
    async for game in cursor:
        games.append(game)
    return games



