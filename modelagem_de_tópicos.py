import requests
from bs4 import BeautifulSoup as bs
import spacy
from bertopic import BERTopic

nlp = spacy.load("pt_core_news_md")

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

#url = "https://pt.wikipedia.org/wiki/Processamento_de_linguagem_natural"
url = "https://pt.wikipedia.org/wiki/Matem%C3%A1tica"
tokens = coleta_texto(url)

modelagem = BERTopic(language="portuguese", nr_topics=10) #baixa modelo de ML
modelagem.fit_transform(tokens) #treina o modelo com os tokens

topicos = modelagem.get_topic_info()

for idTopico,contagem,titulo,conteudo,palavras in topicos.values:
    print("##########################")
    print("ID do tópico: " + str(idTopico))
    print("contagem do tópico: " + str(contagem))
    print("título do tópico: " + str(titulo))
    print("conteudo do tópico: " + str(conteudo))
