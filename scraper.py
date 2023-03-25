import time

import requests
from bs4 import BeautifulSoup
from config import EMAIL, PASSWORD


def login(email: str, password: str) -> requests.Session:
    login_url = "https://www.tesmanian.com/account/login?return_url=%2Faccount"
    session = requests.session()

    while True:
        response = session.get(login_url)

        # Check for 503 status code
        if response.status_code == 503:
            print("Received 503 status code. Waiting 5 minutes before trying again.")
            time.sleep(300)  # Wait 5 minutes
            continue

        login_data = {
            "customer[email]": EMAIL,
            "customer[password]": PASSWORD,
        }
        response = session.post(login_url, data=login_data)

        if response.url != login_url:
            print("Login successful")
        else:
            print("Login failed")

        return session


def scrape_blog(session: requests.Session) -> list[dict]:
    base_url = "https://www.tesmanian.com/blogs/tesmanian-blog/"
    response = session.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", class_="blog-post-card__info")

    results = []

    for card in cards:
        title_element_h2 = card.find("p", class_="h2")
        title_element_h3 = card.findNext("p", class_="h3")
        title_h2 = title_element_h2.text.strip() if title_element_h2 else None
        title_h3 = title_element_h3.text.strip() if title_element_h3 else None
        title = title_h2 or title_h3
        link_element = card.find("a")
        link = link_element["href"] if link_element else None

        results.append({"title": title, "link": link})

    return results
