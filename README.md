# Ski Jumping results scraper 


This scraper collects data about ski jumping events and results. It gathers information about each event, such as the event ID, ski jump location, country, date, hill size (in meters), and the K-point. Additionally, the scraper collects individual results for each competition, including jump IDs, athlete names, first and second jump distances, points, and the event ID associated with each result.


# Technologies and Tools

    Python
    -BeautifulSoup4
    -requests
    -pandas
    JupyterNotebook

# Example Data
### Events Data (events.csv)
The scraper saves event data in a CSV file with the following structure:

| Event_id | Date       | Country  | City        | HS_Point | K_Point |
|----------|------------|----------|-------------|----------|---------|
| 1        | 23-11-2024 | Norway   | Lillehammer | 140      | 123     |
| 2        | 24-11-2024 | Norway   | Lillehammer | 140      | 123     |
| 3        | 30-11-2024 | Finland  | Ruka        | 142      | 120     |

### Results Data (results.csv)
The scraper also saves competition results in a separate CSV file with the following structure:

| Place | Jumper              | Country | Jump1  | Jump2  | Points | Event_id |
|-------|---------------------|---------|--------|--------|--------|----------|
| 1     | PASCHKE Pius        | Germany | 131.5  | 138.5  | 317.1  | 1        |
| 2     | TSCHOFENIG Daniel   | Austria | 132.5  | 132.5  | 309.2  | 1        |
| 3     | ORTNER Maximilian   | Austria | 132    | 131.5  | 307.1  | 1        |

### Code Overview
The scraper is designed to collect and store data from the [skijumping.pl](https://www.skijumping.pl) website. It performs the following tasks:

### 1. Fetch the page with events list and result links
- The script fetches the main page and extracts event details and result links.

### 2. Fetch event details and save to `.csv`
- It collects event data (date, country, city, hill size, K-point) and saves it to `events.csv`.

### 3. Fetch results for events and save to `.csv`
- The script retrieves results (placement, jumper, jump distances, points) and saves them to `results.csv`.
