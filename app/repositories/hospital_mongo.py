# Lab 1.5 -------------------------------------------------------------
# Write MongoHospitalRepo with EXACTLY the same public methods as InMemoryHospitalRepo:
#   list, get, create, replace, delete
#
# Things you will have to solve yourself:
#   1. Mongo stores `_id` as ObjectId, the API exposes `id` as str.
#      -> write one helper `_to_out(doc) -> HospitalOut` and use it everywhere.
#   2. A client can send any string as hospital_id, e.g. "abc".
#      ObjectId("abc") raises. What should the API return? (Hint: ObjectId.is_valid)
#   3. Duplicate `code`: do NOT check with find_one before insert (why? think of 2 requests
#      arriving at the same time). Use a unique index and catch
#      pymongo.errors.DuplicateKeyError -> raise DuplicateCodeError.
#   4. replace(): find_one_and_update(..., return_document=ReturnDocument.AFTER)
#
# Also write:
#   async def ensure_indexes(db) -> None   # unique index on "code"
#
# Docs: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/
