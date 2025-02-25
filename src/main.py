import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


def get_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def get_events(url):
    soup = get_page(url)
    table = soup.find("table", class_="competition-calendar-table")
    individual_events = table.find_all("img", {"title": "konkurs indywidualny"})
    event_rows = []
    for event in individual_events:
        event_rows.append(event.find_parent("tr"))
    return event_rows


def get_results_links(events):
    event_links = []
    for event in events:
        res = event.find_all("a", href=True)[-2]
        if res['href'].startswith("/wyniki/"):
            event_links.append(res['href'])
    return event_links


def events_info_to_csv(events):
    data = []
    for index, event in enumerate(events, start=1):
        cols = event.find_all("td")
        result = {
            "Event_id": index,
            "Date": cols[0].text,
            "Country": cols[1].find("img")["alt"],
            "City": cols[2].text,
            "HS_Point": re.search(r'HS\s*(\d+)', cols[3].text).group(1),
            "K_Point": re.search(r'K-(\d+)', cols[3].text).group(1)
        }
        data.append(result)

    df = pd.DataFrame(data)
    df.to_csv("events.csv", index=False)
def results_to_csv(results):
    data = []
    for event_id, link in enumerate(results, start=1):
        soup = get_page("https://www.skijumping.pl" + link)
        soup.find("table")

        rows = soup.find("table").find_all("tr")[1:]

        for index, row in enumerate(rows, start=1):
            row = row.find_all("td")
            try:
                result = {
                    "Place": row[0].text,
                    "Jumper": row[1].text,
                    "Country": row[2].find("img")["alt"],
                    "Jump1": row[3].text,
                    "Jump2": '0' if row[4].text == "-" else row[4].text,
                    "Points": row[5].text,
                    "Event_id": event_id
                }
            # this exception occurs when the competition has been finished after the first series of jumps
            except IndexError:
                result = {
                    "Place": row[0].text,
                    "Jumper": row[1].text,
                    "Country": row[2].find("img")["alt"],
                    "Jump1": row[3].text,
                    "Jump2": '0',
                    "Points": row[4].text,
                    "Event_id": event_id
                }
            data.append(result)
    df = pd.DataFrame(data)
    df.to_csv("results.csv", index=False)


if __name__ == "__main__":
    URL = f"https://www.skijumping.pl/zawody/ps"

    events = get_events(url=URL)
    events_info_to_csv(events=events)

    results = get_results_links(events=events)
    results_to_csv(results=results)
