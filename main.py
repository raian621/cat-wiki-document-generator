from download import download_articles
from generate import generate_documents
from tabulate import generate_spreadsheet

def main():
  download_articles('./articles.json')
  doc_md = generate_documents('./articles', './documents')
  generate_spreadsheet('./progress_tracker.xlsx', doc_md)

if __name__ == '__main__':
  main()