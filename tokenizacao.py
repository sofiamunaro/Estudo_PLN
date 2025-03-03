#tokenizacao
import requests
from bs4 import BeautifulSoup as bs
import spacy

url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
response = requests.get(url)
soup = bs(response.text, "html.parser")
paragraphs = soup.find_all("p")
page_text = "\n".join([p.get_text() for p in paragraphs])

nlp = spacy.load("pt_core_news_sm")
documento = nlp(page_text)
tokens = [token.orth_ for token in documento]
print(tokens)