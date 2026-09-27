"""Lab 1.6: fire N concurrent requests at each debug endpoint and measure wall time.

Usage (server must be running):  python scripts/async_experiment.py
"""
import asyncio
import time

import httpx

BASE_URL = "http://127.0.0.1:8000"
N = 10
ENDPOINTS = ["/debug/async-blocking", "/debug/async-nonblocking", "/debug/sync-def"]


async def measure(client: httpx.AsyncClient, path: str) -> float:
    # TODO(1.6): send N requests to `path` AT THE SAME TIME, return elapsed seconds
    # Hint: time.perf_counter() + asyncio.gather(*(client.get(path) for _ in range(N)))
    ...


async def main() -> None:
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=60) as client:
        for path in ENDPOINTS:
            elapsed = await measure(client, path)
            print(f"{path:<28} {N} concurrent -> {elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
