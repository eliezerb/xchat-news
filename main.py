 # -*- coding: utf-8 -*-
__module_name__ = "eNews - Plugin"
__module_version__ = "0.0.1"
__module_description__ = "Get random news from a RSS feed website"

import httplib2
import xchat
from sys import argv
from BeautifulSoup import BeautifulStoneSoup
from random import randint

# Esta linha é utilizada para receber um parametro no terminal indicando de qual site voce deseja visualizar as notícias
# script, source = argv


# Funcao que é chamada ao enviar um mensagem no chat
def message_cb(word, word_eol, userdata):   
    message = word[1]
    #Verifica se ela e igual a !news
    if(message == "!news"):

        # Lista para indexar o nome dos servidores
        rss_servers_names = ['lifehacker', 'linux-journal', 'revista-info', 'gizmodo', 'lol-cats']

        # Dicionário com servidores e links
        rss_servers = {
            'lifehacker': 'http://feeds.gawker.com/lifehacker/full.xml',
            'linux-journal': 'http://feeds.feedburner.com/LinuxJournal-BreakingNews',
            'revista-info': 'http://feeds.feedburner.com/Plantao-INFO',
            'gizmodo': 'http://feeds.gawker.com/gizmodo/full',
            'lol-cats': 'http://feeds.feedburner.com/lolcats/rss',
        }
       

        # Inicia a bibilioteca http
        http = httplib2.Http()

        # Realizar a requisicao no servidor escolhido aleatoriamente na lista de servidores
        # - status -> cabecalho da requisicao
        # - response -> corpo do arquivo XML
        status, response = http.request(rss_servers[rss_servers_names[randint(0, len(rss_servers_names)-1)]])

        # Inicializa o soup com o conteúdo XML
        soup = BeautifulStoneSoup(response)

        # Busca todos os itens dentro do XML, onde cada item representa uma noticia
        all_news = soup.findAll("item");

        #Recupera o inicio da mensagem ate o primeiro espaco em branco
        message = word[1]
   
        # Seleciona aleatoriamente uma noticia presente na lista
        selected = randint(0, len(all_news)-1)

        # Envia a mensagem no IRC
        xchat.command("ME "+all_news[selected].title.string + " - " + all_news[selected].link.string)       
       
xchat.prnt("Plugin carregado com sucesso");
xchat.hook_print("Channel Message", message_cb)
xchat.hook_print("Your Message", message_cb)
xchat.hook_print("Private Message to Dialog", message_cb)

