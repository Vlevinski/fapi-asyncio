#!/usr/bin/python

from fastapi import FastAPI
from time import time
import aiohttp
import asyncio

app = FastAPI()

URL = "http://httpbin.org/uuid"


async def request(session):
    async with session.get(URL) as response:
        return await response.text()


async def task():
    async with aiohttp.ClientSession() as session:
        tasks = [request(session) for i in range(100)]
        result = await asyncio.gather(*tasks)
        print(result)


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


@app.get('/test')
async def f():
    start = time()
    try:
        await task()
        result = {"success": "Ok", "result": "printed"}
    except:
        result = {"success": "Bad", "result": "error"}
    print("time: ", time() - start)
    return result
