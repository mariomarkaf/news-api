from fastapi import FastAPI
from scraper import get_all_news  # vagy news_scraper ha úgy hívod

app = FastAPI()

@app.get("/news")
def get_news():
    return get_all_news()
