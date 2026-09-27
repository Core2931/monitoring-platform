# Lab 1.5 -------------------------------------------------------------
# TODO(1.5):
#   create_client() -> AsyncMongoClient
#       Hint: from pymongo import AsyncMongoClient
#       Pass serverSelectionTimeoutMS=3000. Find out in the docs what happens without it
#       when Mongo is down.
#
#   get_db(request: Request) -> AsyncDatabase
#       read the client from request.app.state, return client[settings.mongo_db]
#       Hint: from pymongo.asynchronous.database import AsyncDatabase
