import requests

STOCK_NAME = "AAPL"
COMPANY_NAME = "APPLE INC"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


#  Data:
#   'Time Series (Daily)': {
#     'YYYY-MM-DD': {
#       '1. open': '172.3300',
#       '2. high': '173.0800',
#       '3. low': '168.0400',
#       '4. close': '168.6400',
#       '5. volume': '98670687'


# Getting Stock Pricing Data
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for  (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

# Difference between yesterday closing price and the day before yesterday closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# Percentage difference
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

up_down = None
if difference > 3:
    up_down = "🔺"
else:
    up_down = "🔻"


news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

# Getting latest news about company data
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]

first_article = articles[1]
first_three_articles = articles[:3]

formatted_articles = [
    f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
    article in first_three_articles
]

for article in formatted_articles:
    print(article)





