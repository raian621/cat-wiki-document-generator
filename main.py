from download import download_articles
from generate import generate_document

def main():
  download_articles('./articles.json')
  generate_document('./articles')

if __name__ == '__main__':
  main()