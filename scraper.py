import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ----------- FINEXTRA ------------

def get_finextra_ai_news():
    url = "https://www.finextra.com/channel/ai"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for card in soup.select("div.card-body")[:10]:
        a_tag = card.select_one("h2.card-title a[href^='/newsarticle']")
        time_tag = card.select_one("time.card-timestamp")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link

        if time_tag and time_tag.has_attr("datetime"):
            try:
                dt = datetime.strptime(time_tag["datetime"], "%Y-%m-%d %H:%M:%SZ")
                time_iso = dt.isoformat()
            except:
                time_iso = None
        else:
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Finextra",
            "category": "Artificial Intelligence"
        })
    return articles


def get_finextra_startups_news():
    url = "https://www.finextra.com/channel/startups"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for card in soup.select("div.card-body")[:10]:
        a_tag = card.select_one("h2.card-title a[href^='/newsarticle']")
        time_tag = card.select_one("time.card-timestamp")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link

        if time_tag and time_tag.has_attr("datetime"):
            try:
                dt = datetime.strptime(time_tag["datetime"], "%Y-%m-%d %H:%M:%SZ")
                time_iso = dt.isoformat()
            except:
                time_iso = None
        else:
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Finextra",
            "category": "Startups"
        })
    return articles

def get_finextra_crypto_news():
    url = "https://www.finextra.com/channel/crypto"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    for card in soup.select("div.card-body")[:10]:
        a_tag = card.select_one("h2.card-title a[href^='/newsarticle']")
        time_tag = card.select_one("time.card-timestamp")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]
        if link.startswith("/"):
            link = "https://www.finextra.com" + link

        if time_tag and time_tag.has_attr("datetime"):
            try:
                dt = datetime.strptime(time_tag["datetime"], "%Y-%m-%d %H:%M:%SZ")
                time_iso = dt.isoformat()
            except:
                time_iso = None
        else:
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Finextra",
            "category": "Crypto"
        })
    return articles


# ----------- PORTFOLIO ------------

def get_portfolio_ingatlan_news():
    url = "https://www.portfolio.hu/ingatlan"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    honapok = {
        "január": "January", "február": "February", "március": "March", "április": "April",
        "május": "May", "június": "June", "július": "July", "augusztus": "August",
        "szeptember": "September", "október": "October", "november": "November", "december": "December"
    }

    for article in soup.select("article.article-block-item")[:10]:
        a_tag = article.select_one("h3.title a")
        time_tag = article.select_one("p.properties")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        # Idő feldolgozása
        time_iso = None
        if time_tag:
            raw_time = time_tag.get_text(strip=True).lower()  # pl.: "2025. július 14. 09:00"
            try:
                for hu, en in honapok.items():
                    raw_time = raw_time.replace(hu, en)
                dt = datetime.strptime(raw_time, "%Y. %B %d. %H:%M")
                time_iso = dt.isoformat()
            except Exception as e:
                print(f"⚠️ Hiba dátum konvertálásnál: {e}")

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Portfolio.hu",
            "category": "Real Estate"
        })

    print(f"📥 get_portfolio_ingatlan_news(): {len(articles)} hír betöltve")
    return articles

def get_portfolio_global_news():
    url = "https://www.portfolio.hu/global"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    honapok = {
        "január": "January", "február": "February", "március": "March", "április": "April",
        "május": "May", "június": "June", "július": "July", "augusztus": "August",
        "szeptember": "September", "október": "October", "november": "November", "december": "December"
    }

    for article in soup.select("article.article-block-item")[:10]:
        a_tag = article.select_one("h3.title a")
        time_tag = article.select_one("p.properties")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        # Idő feldolgozása
        time_iso = None
        if time_tag:
            raw_time = time_tag.get_text(strip=True).lower()
            try:
                for hu, en in honapok.items():
                    raw_time = raw_time.replace(hu, en)
                dt = datetime.strptime(raw_time, "%Y. %B %d. %H:%M")
                time_iso = dt.isoformat()
            except Exception as e:
                print(f"⚠️ Hiba dátum konvertálásnál: {e}")

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Portfolio.hu",
            "category": "Defense"
        })

    print(f"📥 get_portfolio_global_news(): {len(articles)} hír betöltve")
    return articles

def get_portfolio_uzlet_news():
    url = "https://www.portfolio.hu/uzlet"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    honapok = {
        "január": "January", "február": "February", "március": "March", "április": "April",
        "május": "May", "június": "June", "július": "July", "augusztus": "August",
        "szeptember": "September", "október": "October", "november": "November", "december": "December"
    }

    for article in soup.select("article.article-block-item")[:10]:
        a_tag = article.select_one("h3.title a")
        time_tag = article.select_one("p.properties")

        if not a_tag:
            continue

        title = a_tag.get_text(strip=True)
        link = a_tag["href"]

        # Idő feldolgozása
        time_iso = None
        if time_tag:
            raw_time = time_tag.get_text(strip=True).lower()
            try:
                for hu, en in honapok.items():
                    raw_time = raw_time.replace(hu, en)
                dt = datetime.strptime(raw_time, "%Y. %B %d. %H:%M")
                time_iso = dt.isoformat()
            except Exception as e:
                print(f"⚠️ Hiba dátum konvertálásnál: {e}")

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Portfolio.hu",
            "category": "Economy"
        })

    print(f"📥 get_portfolio_uzlet_news(): {len(articles)} hír betöltve")
    return articles


# ----------- MONITORBLOG ------------

def get_monitorblog_reszvenypiac_news():
    url = "https://monitorblog.hu/category/reszvenypiac/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    honapok = {
        "január": "January", "február": "February", "március": "March", "április": "April",
        "május": "May", "június": "June", "július": "July", "augusztus": "August",
        "szeptember": "September", "október": "October", "november": "November", "december": "December"
    }

    for content in soup.select("div.content")[:10]:
        title_tag = content.select_one("h3 a")
        time_author_tag = content.select_one("div.cat a")

        if not title_tag or not time_author_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = title_tag["href"]

        # Idő kinyerése: "2025. június 25. - Debreczeni Csaba"
        raw_time = time_author_tag.get_text(strip=True).split(" - ")[0].lower()
        time_iso = None
        try:
            for hu, en in honapok.items():
                raw_time = raw_time.replace(hu, en)
            dt = datetime.strptime(raw_time, "%Y. %B %d.")
            time_iso = dt.isoformat()
        except Exception as e:
            print(f"⚠️ Hiba dátum konvertálásnál: {e}")

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Monitorblog.hu",
            "category": "Stock Market"
        })

    print(f"📥 get_monitorblog_reszvenypiac_news(): {len(articles)} hír betöltve")
    return articles

def get_monitorblog_ingatlanpiac_news():
    url = "https://monitorblog.hu/category/ingatlanpiac/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    honapok = {
        "január": "January", "február": "February", "március": "March", "április": "April",
        "május": "May", "június": "June", "július": "July", "augusztus": "August",
        "szeptember": "September", "október": "October", "november": "November", "december": "December"
    }

    for content in soup.select("div.content")[:10]:
        title_tag = content.select_one("h3 a")
        time_author_tag = content.select_one("div.cat a")

        if not title_tag or not time_author_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = title_tag["href"]

        # Idő szöveg feldolgozása
        raw_time = time_author_tag.get_text(strip=True).split(" - ")[0].lower()
        time_iso = None
        try:
            for hu, en in honapok.items():
                raw_time = raw_time.replace(hu, en)
            dt = datetime.strptime(raw_time, "%Y. %B %d.")
            time_iso = dt.isoformat()
        except Exception as e:
            print(f"⚠️ Hiba dátum konvertálásnál: {e}")

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Monitorblog.hu",
            "category": "Real Estate"
        })

    print(f"📥 get_monitorblog_ingatlanpiac_news(): {len(articles)} hír betöltve")
    return articles
# ---------------------- INVESTOPEDIA ----------------------

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_investopedia_crypto_news():
    url = "https://www.investopedia.com/cryptocurrency-news-5114163"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    cards = soup.select("div.card__content[data-tag='Cryptocurrency News']")
    for card in cards[:10]:
        title_tag = card.select_one("span.card__title-text")
        link_tag = card.find_parent("a")
        date_tag = card.select_one("span.displayed-date__date")

        if not title_tag or not link_tag or not date_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]
        if link.startswith("/"):
            link = "https://www.investopedia.com" + link

        try:
            time_obj = datetime.strptime(date_tag.get_text(strip=True), "%b %d, %Y")
            time_iso = time_obj.isoformat()
        except Exception as e:
            print(f"⚠️ Hiba dátum konvertálásnál: {e}")
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Investopedia",
            "category": "Cryptocurrency"
        })

    print(f"📥 get_investopedia_crypto_news(): {len(articles)} hír betöltve")
    return articles

def get_investopedia_markets_news():
    url = "https://www.investopedia.com/markets-news-4427704"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    cards = soup.select("div.card__content[data-tag='Markets News']")
    for card in cards[:10]:
        title_tag = card.select_one("span.card__title-text")
        link_tag = card.find_parent("a")
        date_tag = card.select_one("span.displayed-date__date")

        if not title_tag or not link_tag or not date_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]
        if link.startswith("/"):
            link = "https://www.investopedia.com" + link

        try:
            time_obj = datetime.strptime(date_tag.get_text(strip=True), "%b %d, %Y")
            time_iso = time_obj.isoformat()
        except Exception as e:
            print(f"⚠️ Hiba dátum konvertálásnál: {e}")
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Investopedia",
            "category": "Markets"
        })

    print(f"📥 get_investopedia_markets_news(): {len(articles)} hír betöltve")
    return articles

def get_investopedia_economic_news():
    url = "https://www.investopedia.com/economic-news-5218422"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = []

    cards = soup.select("div.card__content[data-tag='Economic News']")
    for card in cards[:10]:
        title_tag = card.select_one("span.card__title-text")
        link_tag = card.find_parent("a")
        date_tag = card.select_one("span.displayed-date__date")

        if not title_tag or not link_tag or not date_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]
        if link.startswith("/"):
            link = "https://www.investopedia.com" + link

        try:
            time_obj = datetime.strptime(date_tag.get_text(strip=True), "%b %d, %Y")
            time_iso = time_obj.isoformat()
        except Exception as e:
            print(f"⚠️ Hiba dátum konvertálásnál: {e}")
            time_iso = None

        articles.append({
            "title": title,
            "url": link,
            "time": time_iso,
            "source": "Investopedia",
            "category": "Economy"
        })

    print(f"📥 get_investopedia_economic_news(): {len(articles)} hír betöltve")
    return articles



# ---------------------- GYŰJTŐ FÜGGVÉNYEK ----------------------

def get_all_real_estate_news():
    return (
        get_monitorblog_ingatlanpiac_news() +
        get_portfolio_ingatlan_news() 
    )

def get_all_stock_market_news():
    return (
        get_monitorblog_reszvenypiac_news() +
        get_investopedia_markets_news()
    )

def get_all_ai_news():
    return (
        get_finextra_ai_news()
    )

def get_all_defense_news():
    return (
        get_portfolio_global_news() 
    )

def get_all_startups_news():
    return (
        get_finextra_startups_news()
    )

def get_all_economy_news():
    return (
        get_portfolio_uzlet_news() +
        get_investopedia_economic_news()
    )

def get_all_news():
    all_articles = (
        get_all_real_estate_news() +
        get_all_stock_market_news() +
        get_all_ai_news() +
        get_all_defense_news() +
        get_all_startups_news() +
        get_all_economy_news() +
        get_finextra_crypto_news() +
        get_investopedia_crypto_news()
    )

    return [a for a in all_articles if a.get("title")]

import json

def scrape_all():
    return get_all_news()

def write_to_json(data, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    all_articles = scrape_all()
    write_to_json(all_articles)
    print(f"{len(all_articles)} cikk elmentve a 'news.json' fájlba.")
