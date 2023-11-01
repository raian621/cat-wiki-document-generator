from os import mkdir
from os.path import exists

from download import download_articles

def main():
  download_articles('./articles.json')

if __name__ == '__main__':
  main()