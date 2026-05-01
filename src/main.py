from fastapi import FastAPI
from pydantic import HttpUrl
from scrapling.fetchers import StealthyFetcher

app = FastAPI()

@app.get("/")
async def fetch(url: str):
    HttpUrl(url)
    page = await StealthyFetcher.async_fetch(url=url)
    data = page.html_content
    return data
