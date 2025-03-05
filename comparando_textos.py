import requests
from bs4 import BeautifulSoup as bs
import spacy
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#carrega o modelo de pln (usando agora o médio em vez do small)
nlp = spacy.load("pt_core_news_md")

#criar função que recebe uma url e retorna lista de tokens
def coleta_texto(url):

    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    page_text = "\n".join([p.get_text() for p in paragraphs])

    documento = nlp(page_text)

    tokens = []
    for token in documento:
        if token.pos_ == "VERB" and token.is_alpha and not(token.is_stop):
            tokens.append(str.lower(token.lemma_))
        elif not(token.pos_ == "VERB") and token.is_alpha and not(token.is_stop):
            tokens.append(str.lower(token.text))

    return tokens

url1 = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
url2 = "https://pt.wikipedia.org/wiki/Ci%C3%AAncia_da_computa%C3%A7%C3%A3o"
url3 = "https://pt.wikipedia.org/wiki/Andorinha"

tokens1 = coleta_texto(url1)
tokens2 = coleta_texto(url2)
tokens3 = coleta_texto(url3)

documento1 = nlp(" ".join(tokens1)) #método join pois nlp só recebe string
documento2 = nlp(" ".join(tokens2))
documento3 = nlp(" ".join(tokens3))

similaridade11 = documento1.similarity(documento1)
print("a similaridade entre pln e pln é de " + str(similaridade11))
similaridade13 = documento1.similarity(documento3)
similaridade12 = documento1.similarity(documento2)
print("a similaridade entre pln e ciência da computação é de " + str(similaridade12))
similaridade13 = documento1.similarity(documento3)
print("a similaridade entre pln e andorinha é de " + str(similaridade13))

