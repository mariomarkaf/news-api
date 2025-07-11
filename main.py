from fastapi import FastAPI
from scraper import get_all_news

app = FastAPI()

@app.get("/news")
def get_news():
    return get_all_news()
