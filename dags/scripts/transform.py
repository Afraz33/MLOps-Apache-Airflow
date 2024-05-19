import re


def clean_text(text):

    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text


def transform_data(articles):
    for article in articles:
        article['title'] = clean_text(article['title'])
        article['description'] = clean_text(article['description'])
    return articles
