import requests #faz requisiçoes http
from bs4 import BeautifulSoup as bs #analisa o html da pagina
import spacy #biblioteca de pln

#faz uma requisicao http para o url dado e usa o bs4 para transformar o html num texto legível
url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
response = requests.get(url)
soup = bs(response.text, "html.parser")
paragraphs = soup.find_all("p")
page_text = "\n".join([p.get_text() for p in paragraphs])

nlp = spacy.load("pt_core_news_sm") #carrega um modelo de pln em portugues
documento = nlp(page_text) #transforma o texto da página em um objeto
tokens = [token.orth_ for token in documento if token.is_alpha and not(token.is_stop)] #percorre os tokens (palavras)
print(tokens)


#print(len(tokens))
#print(nlp.Defaults.stop_words) mostra quais são as stopwords