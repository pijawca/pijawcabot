from bs4 import BeautifulSoup
from pyowm import OWM
import feedparser
import requests


#  RSS
def nt_t():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[0].title
def nt_l():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[0].link
def nt_t1():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[1].title
def nt_l1():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[1].link
def nt_t2():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[2].title
def nt_l2():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[2].link
def nt_t3():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[3].title
def nt_l3():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[3].link
def nt_t4():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[4].title
def nt_l4():
    url = 'http://news.yandex.ru/internet.rss'
    feed = feedparser.parse(url)
    return feed.entries[4].link
def ga_t():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[0].title
def ga_l():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[0].link
def ga_t1():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[1].title
def ga_l1():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[1].link
def ga_t2():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[2].title
def ga_l2():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[2].link
def ga_t3():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[3].title
def ga_l3():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[3].link
def ga_t4():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[4].title
def ga_l4():
    url = 'http://news.yandex.ru/gadgets.rss'
    feed = feedparser.parse(url)
    return feed.entries[4].link