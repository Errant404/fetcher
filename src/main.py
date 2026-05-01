from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import HttpUrl
from scrapling.fetchers import StealthyFetcher

app = FastAPI()

@app.get("/rss")
async def fetch_rss(url: str):
    HttpUrl(url)
    page = await StealthyFetcher.async_fetch(url=url)
    data = page.html_content
    return Response(content=data, media_type="application/xml")
