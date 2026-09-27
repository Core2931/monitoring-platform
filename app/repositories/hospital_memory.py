from datetime import UTC, datetime
from uuid import uuid4

from app.repositories.errors import DuplicateCodeError
from app.schemas.hospital import HospitalCreate, HospitalOut


# Lab 1.3 -------------------------------------------------------------
# Every method is `async` even though a dict is not I/O.
# Reason: in Lab 1.5 MongoHospitalRepo must have the SAME method signatures,
# so the router never needs to change when we swap storage.
class InMemoryHospitalRepo:
    def __init__(self) -> None:
        self._items: dict[str, HospitalOut] = {}

    async def list(self, *, region: str | None, skip: int, limit: int) -> list[HospitalOut]:
        items = sorted(self._items.values(), key=lambda h: h.code)
        if region:
            items = [h for h in items if h.region == region]
        return items[skip : skip + limit]

    async def get(self, hospital_id: str) -> HospitalOut | None:
        # TODO(1.3): return the hospital or None
        ...

    async def create(self, data: HospitalCreate) -> HospitalOut:
        # TODO(1.3):
        #   1. raise DuplicateCodeError if code already exists (helper below)
        #   2. build HospitalOut with id=uuid4().hex, created_at=datetime.now(UTC)
        #      Hint: HospitalOut(id=..., created_at=..., **data.model_dump())
        #   3. store it and return it
        ...

    async def replace(self, hospital_id: str, data: HospitalCreate) -> HospitalOut | None:
        # TODO(1.3): PUT = replace every client-owned field
        #   - None if not found
        #   - keep the original id and created_at
        #   - code must stay unique (but it may equal its OWN current code)
        ...

    async def delete(self, hospital_id: str) -> bool:
        # TODO(1.3): True if deleted, False if not found
        ...

    def _ensure_unique_code(self, code: str, exclude_id: str | None = None) -> None:
        for h in self._items.values():
            if h.code == code and h.id != exclude_id:
                raise DuplicateCodeError(code)
