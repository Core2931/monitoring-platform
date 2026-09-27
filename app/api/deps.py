# Lab 1.4 -------------------------------------------------------------
# Goal: the router asks for "a hospital repo" and does not know which one it gets.
#
# TODO(1.4):
#   1. create ONE InMemoryHospitalRepo instance at module level
#   2. write get_hospital_repo() that returns it
#   3. make a type alias so routes can write `repo: HospitalRepo`
#      Hint: HospitalRepo = Annotated[<type>, Depends(get_hospital_repo)]
#
# TODO(1.5):
#   get_hospital_repo(request: Request) returns MongoHospitalRepo(get_db(request))
#   when settings.storage == "mongo", otherwise the in-memory repo
