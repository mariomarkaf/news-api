import requests
from bs4 import BeautifulSoup
import json

def get_businessinsider_stocks_news():
    url = "https://markets.businessinsider.com/stocks"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.instrument-stories__link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://markets.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Stocks"
        })
    return articles

def get_businessinsider_ai_news():
    url = "https://www.businessinsider.com/artificial-intelligence"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "AI"
        })
    return articles

def get_businessinsider_realestate_news():
    url = "https://www.businessinsider.com/real-estate"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Real Estate"
        })
    return articles

def get_businessinsider_startups_news():
    url = "https://www.businessinsider.com/startups"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Startups"
        })
    return articles

def get_businessinsider_defense_news():
    url = "https://www.businessinsider.com/defense"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Defense"
        })
    return articles

def get_businessinsider_economy_news():
    url = "https://www.businessinsider.com/economy"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Economy"
        })
    return articles

def get_businessinsider_finance_news():
    url = "https://www.businessinsider.com/finance"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []
    for item in soup.select("a.tout-title-link")[:5]:
        title = item.get_text(strip=True)
        link = item["href"]
        if link.startswith("/"):
            link = "https://www.businessinsider.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Business Insider",
            "category": "Economy"
        })
    return articles

def get_finextra_crypto_news():
    url = "https://www.finextra.com/channel/crypto"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='/newsarticle']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Finextra",
            "category": "Crypto"
        })
    return articles

def get_finextra_ai_news():
    url = "https://www.finextra.com/channel/ai"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='/newsarticle']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Finextra",
            "category": "AI"
        })
    return articles

def get_finextra_startups_news():
    url = "https://www.finextra.com/channel/startups"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='/newsarticle']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link
        articles.append({
            "title": title,
            "url": link,
            "source": "Finextra",
            "category": "Startups"
        })
    return articles

def get_portfolio_ingatlan_news():
    url = "https://www.portfolio.hu/ingatlan"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='https://www.portfolio.hu/ingatlan/']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Portfolio.hu",
            "category": "Real Estate"
        })
    return articles

def get_portfolio_global_news():
    url = "https://www.portfolio.hu/global"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='https://www.portfolio.hu/global/']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Portfolio.hu",
            "category": "Defense"
        })
    return articles

def get_portfolio_uzlet_news():
    url = "https://www.portfolio.hu/uzlet"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("a[href^='https://www.portfolio.hu/uzlet/']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Portfolio.hu",
            "category": "Economy"
        })
    return articles

def get_monitorblog_news(category_name, category_url):
    r = requests.get(category_url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("h2.entry-title a")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Monitorblog.hu",
            "category": category_name
        })
    return articles

def get_monitorblog_reszvenypiac_news():
    url = "https://monitorblog.hu/category/reszvenypiac/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("h2.entry-title a[href^='https://monitorblog.hu/hirek-']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Monitorblog.hu",
            "category": "Stocks"
        })
    return articles

def get_monitorblog_ingatlanpiac_news():
    url = "https://monitorblog.hu/category/ingatlanpiac/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for a in soup.select("h2.entry-title a[href^='https://monitorblog.hu/']")[:5]:
        title = a.get_text(strip=True)
        link = a["href"]
        articles.append({
            "title": title,
            "url": link,
            "source": "Monitorblog.hu",
            "category": "Real Estate"
        })
    return articles

def get_all_real_estate_news():
    return (
        get_monitorblog_ingatlanpiac_news() +
        get_portfolio_ingatlan_news() +
        get_businessinsider_realestate_news()
    )

def get_all_stock_market_news():
    return (
        get_monitorblog_reszvenypiac_news() +
        get_businessinsider_stocks_news()
    )

def get_all_ai_news():
    return (
        get_businessinsider_ai_news() +
        get_finextra_ai_news()
    )

def get_all_defense_news():
    return (
        get_businessinsider_defense_news() +
        get_portfolio_global_news()
    )

def get_all_startups_news():
    return (
        get_businessinsider_startups_news() +
        get_finextra_startups_news()
    )

def get_all_economy_news():
    return (
        get_businessinsider_economy_news() +
        get_businessinsider_finance_news() +
        get_portfolio_uzlet_news()
    )


def get_all_news():
    return (
        get_all_real_estate_news() +
        get_all_stock_market_news() +
        get_all_ai_news() +
        get_all_defense_news() +
        get_all_startups_news() +
        get_all_economy_news() +
        get_finextra_crypto_news()
    )




if __name__ == "__main__":
    data = get_all_news()
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(json.dumps(data, ensure_ascii=False, indent=2))
