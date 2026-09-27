from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, Response, status

from app.repositories.errors import DuplicateCodeError
from app.repositories.hospital_memory import InMemoryHospitalRepo
from app.schemas.hospital import HospitalCreate, HospitalOut, Region

router = APIRouter(prefix="/hospitals", tags=["hospitals"])

# Lab 1.3: a module-level repo so every request shares the same data.
# Lab 1.4: DELETE this line and receive the repo through Depends() instead.
repo = InMemoryHospitalRepo()


# Example: one endpoint done for you. Read it, then write the other four.
@router.get("", response_model=list[HospitalOut])
async def list_hospitals(
    region: Region | None = None,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
):
    return await repo.list(region=region, skip=skip, limit=limit)


# TODO(1.3): GET /hospitals/{hospital_id}
#   200 -> HospitalOut, 404 if not found
#   Hint: raise HTTPException(status.HTTP_404_NOT_FOUND, "hospital not found")


# TODO(1.3): POST /hospitals
#   body HospitalCreate -> 201 + HospitalOut
#   duplicate code -> 409 (catch DuplicateCodeError)
#   Hint: status_code= on the decorator


# TODO(1.3): PUT /hospitals/{hospital_id}
#   body HospitalCreate -> 200 + HospitalOut, 404, 409


# TODO(1.3): DELETE /hospitals/{hospital_id}
#   204 no body, 404 if not found
