from docx import Document
from os import listdir
from bs4 import BeautifulSoup

document_actions = {
  "h1": lambda document, text : document.add_heading(text, 0),
  "h2": lambda document, text : document.add_heading(text, 1),
  "h3": lambda document, text : document.add_heading(text, 2),
  "p": lambda document, text : document.add_paragraph(text),
}

def generate_document(dirname):
  document = Document()
  
  for filename in listdir(f'./{dirname}/good'):
    with open(f'{dirname}/good/{filename}', 'rb') as file:
      print(filename)
      soup = BeautifulSoup(file.read(), 'html.parser')
      heading = soup.find(class_='mw-page-title-main')
      document.add_heading(heading.getText(), 0)
      content = soup.find(class_='mw-parser-output')
      for child in content.children:
        document_action = document_actions.get(child.name, None)
        if document_action == None:
          continue
        document_action(document, child.getText())
      
  document.save('articles.docx')