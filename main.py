from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification, pipeline

API_TOKEN = "(your user access token from https://huggingface.co/settings/tokens)"
API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def pipelineMethod(payload):
     tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
     model = TFAutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

     classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, framework="tf")
     res = classifier(payload)
     return res[0]


column = ['datetime', 'title', 'source', 'link', 'top_sentiment', 'sentiment_score']
df = pd.DataFrame(columns=column)

counter = 0
for page in range(1, 41):

    url = f'https://www.investopaper.com/articles/page/{page}/#wpnw-news-{page-1}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    # Debug: Print the HTML content of the page
    # print(f"Scraping page {page}")
    # print(soup.prettify()[:1000])  # Print the first 1000 characters to check if it's loading correctly

    articles = soup.find_all('div', class_='news-content')
    
    # Debug: Print the number of articles found
    print(f"Found {len(articles)} articles on page {page}")
    
    for article in articles:
        # Extracting the date
        date_post = article.find('div', class_='grid-date-post')
        if date_post:
            date_text = date_post.text.strip().split('/')
            datetime = date_text[0].strip() if date_text else 'N/A'
        else:
            datetime = 'N/A'
        
        # Extracting the title and link
        title_tag = article.find('h3', class_='news-title')
        if title_tag and title_tag.find('a'):
            title = title_tag.find('a').text.strip()
            link = title_tag.find('a').get('href')
        else:
            title = 'N/A'
            link = 'N/A'
        
        # Extracting the source
        source_tag = date_post.find_all('a')
        source = source_tag[1].text.strip() if len(source_tag) > 1 else 'N/A'
        
        # Placeholder values for sentiment fields
        # top_sentiment = ''
        # sentiment_score = ''
        
        # Append data to DataFrame
        output = pipelineMethod(title)
        top_sentiment = output['label']
        sentiment_score = output['score']
        # Print each scraped row
        # print(f"Date: {datetime}, Title: {title}, Source: {source}, Link: {link}")
        df = pd.concat([pd.DataFrame([[datetime, title, source, link, top_sentiment, sentiment_score]], columns=df.columns), df], ignore_index=True)

        counter += 1

        # output = query({
        #      "inputs" : title
        # })
        # print(output)



        # print(top_sentiment, sentiment_score)

print(f'\n{counter} news articles scraped')
df.to_csv('sentiment-nepali-news.csv', index = False)
