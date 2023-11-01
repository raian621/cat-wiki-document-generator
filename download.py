import json
import requests
from os.path import exists
from os import mkdir
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
from htmlmin import minify


def download_article(filepath, url):
  print('Downloading', filepath)
  
  if exists(filepath):
    return
  
  with open(filepath, 'w') as file:
    response = requests.get(url)
    if response.ok:
      soup = BeautifulSoup(response.content, 'html.parser')
      file.write(minify(
        soup.find('main').__str__(),
        remove_comments=True,
        remove_empty_space=True,
      ))


def download_articles(filepath):
  articles = None
  with open(filepath, 'rb') as file:
    articles = json.load(file)
    
  if not exists('./articles'):
    mkdir('./articles')
  if not exists('./articles/good'):
    mkdir('./articles/good')
  if not exists('./articles/decent'):
    mkdir('./articles/decent')
  if not exists('./articles/meh'):
    mkdir('./articles/meh')

  threads = []
  
  for key in articles.keys():
    for article in articles[key]:
      filepath = f'./articles/{key}/{article.split("/")[-1]}.html'
      if not exists(filepath):
        threads.append(Thread(target=download_article, args=[filepath, article]))
        threads[-1].start()
        sleep(0.5) # be nice to cat wiki servers
  
  # ensure all threads have finished executing before exiting the main thread
  for thread in threads:
    thread.join()
    