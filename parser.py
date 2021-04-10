import feedparser
import pandas as pd
import config

"""in this parser use code from https://github.com/germanjke/RSSparsing, tnx a lot"""


def check_url(url_feed):
    """func get rss feed url and parse it with feedparser"""
    return feedparser.parse(url_feed)


def get_headlines(url_feed):
    """func get title of news"""
    _headlines = []
    feed = check_url(url_feed)
    for item_of_news in feed['items']:
        _headlines.append(item_of_news['title'])
    return _headlines


def get_descriptions(url_feed):
    """func get text of news"""
    _descriptions = []
    feed = check_url(url_feed)
    for item_of_news in feed['items']:
        _descriptions.append(item_of_news['description'])
    return _descriptions


def get_links(url_feed):
    """func get url of news"""
    _links = []
    feed = check_url(url_feed)
    for item_of_news in feed['items']:
        _links.append(item_of_news['link'])
    return _links


def get_dates(url_feed):
    """func get dates of news"""
    _dates = []
    feed = check_url(url_feed)
    for item_of_news in feed['items']:
        _dates.append(item_of_news['published'])
    return _dates


def write_df():
    """func parse urls,
    write data to dataframe,
    then write .csv file"""
    headlines = []
    descriptions = []
    links = []
    dates = []
    for key, url in config.feeds.items():
        headlines.extend(get_headlines(url))

    for key, url in config.feeds.items():
        descriptions.extend(get_descriptions(url))

    for key, url in config.feeds.items():
        links.extend(get_links(url))

    for key, url in config.feeds.items():
        dates.extend(get_dates(url))
    df = pd.DataFrame({
            'title': headlines,
            'text': descriptions,
            'link': links,
            'date': dates
                       })

    return df.to_csv(config.csv_news, index=False)

