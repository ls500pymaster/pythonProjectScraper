## Tesmanian Blog Scraper

This project is a simple web scraper for the Tesmanian blog that logs in, scrapes new blog posts, and sends them to a Telegram group. It uses the requests library for HTTP requests, BeautifulSoup for parsing HTML, and aiogram for interacting with the Telegram API.

### Features
- Log in to the Tesmanian website
- Scrape new blog posts and their URLs
- Send new blog posts to a Telegram group
- Check for new posts every 15 seconds
- Save scraped data to an SQLite3 database
- Handle 503 status errors by waiting 5 minutes before retrying

Clone this repository:

`git clone https://github.com/yourusername/tesmanian-blog-scraper.git
`

Install the required packages:

`pip install -r requirements.txt
`

## Configuration
Set up your Tesmanian login credentials by updating the EMAIL and PASSWORD variables in the main.py file.

Set up your Telegram bot token by updating the BOT_TOKEN variable in the main.py file.

Set the Telegram group chat ID by updating the GROUP_CHAT_ID variable in the main.py file.

## Usage
Run the script with:

`python main.py
`

The scraper will log in to the Tesmanian website, scrape new blog posts, and send them to the specified Telegram group. It will also save the scraped data to an SQLite3 database. If a 503 status code is encountered, the script will wait for 5 minutes before trying again.