## Sof crawler

A Crawler for stackoverflow.com's latest 5000 questions by tag 

#### Run locally

1. Clone the repository
    
2. Install the requirements
    
    `pip install -r requirements.txt`

3. Run the crawler

    `scrapy crawl sof`


#### Run with docker

1. Clone the repository

2. Run docker-compose

    `docker-compose up -d --build`

After this processes latest 5000 questions will be inserted to **sof.db** database file.
