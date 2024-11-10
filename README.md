# Nepali stock news scrapping and its sentiment analysis
## Scrapping
<ul>
  <li>
    The scrapping for Nepalese **stock news headlines** is done using [Investopaper](https://www.investopaper.com/).
  </li>
  <li>
    This program scrapes 480 news headlines available in Investopaper.
  </li>
  <li>
    The program file just for the scrapping is 'scrapping.txt'. Just change the extension to '.py' and run it if you will to only scrape the data without performing sentiment analysis.
  </li>
</ul>

## Scrapping with Sentiment Analysis
<ul>
  <li>
    It scrapes the news headlines as well as performs sentiment analysis with the help of an api available in [Hugging Face](https://huggingface.co/).
  </li>
  <li>
    It saves the file as 'sentiment-nepali-news.csv' which contains the final result.
  </li>  
</ul>

## How to create user access token for Sentiment Analysis?
<ol>
  <li>
    Create a free account in [Hugging Face](https://huggingface.co/).
  </li>
  <li>
    After creating an account, head to [User Access Token](https://huggingface.co/settings/tokens).
  </li>
  <li>
    Create a new access token by giving it a name and giving it the 'write' permission.
  </li>
  <li>
    Once created, copy it in the 'main.py' as the API_TOKEN.
  </li>
</ol>

