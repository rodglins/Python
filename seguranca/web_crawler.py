# envia solicitações http em python:
import requests
# extrai dados de arquivos html e xml:
from bs4 import BeautifulSoup
# conjunto de funções +-*/ not and :
import operator
# preenche e manipula estruturas de dados como tuplas, dicionários e listas
from collections import Counter

# função define o webcrawler
def start(url):
    # armazena td o conteudo do site:
    wordlist = []
    source_code = requests.get(url).text

    # faz a requisição dos dados da url e transforma em html
    soup = BeautifulSoup(source_code, 'html.parser')

    # procura td que existe com div e classe:
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        # converte em texto (string):
        content = each_text.text

        # transforma em letras minusculas, onde cada conteúdo será uma linha:
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

# função remove qualquer simbolo do wordlist
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%¨&*()_+=-[]{}~^,.;:|\/<>'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

# funcao cria dicionario, fazendo contagem das palavras, evibe, e faz uma lista das mais utilizadas.
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                                key = operator.itemgetter(1)):
        print('% s : % s ' % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')



