from bottle import run, get, post, view, request, redirect, route, static_file
import sys
import threading
import json

sys.path.append('./../t1-part2/')
from request import *
from peers import *

url = "localhost:"
fixOne = "8080"
fixTwo = "8081"

messages = [("Nobody", "Hello!")]
nick = "Nobody"

ID = 8080

peers = []


@route('/<name>')
@get('/<name>')
@view('index')
def index(nick):
   return {'messages': messages, 'nick': nick }


@post('/send')
def sendMessage():
	global nick
   m = request.forms.get('message')
   n = request.forms.get('nick')
   messages.append([n, m])
   nick = n
   redirect('/')


@post('/synchronize')
def returnPeers():
	return json.dumps(peers)

@post('/message')
def returnMessages():
	return json.dumps(messges)


#Messages 
def getMessage():



#Client
def clientSearchPeers():
	global peers
	#caso não tenha peers na lista
	if len(peers) == 0 :
		responseOne = tryConnect(url+fixOne)
		responseTwo = tryConnect(url+fixTwo)
		if (responseOne != False):
			listPeers = json.loads(responseOne)
			peers = listPeers
		elif (responseTwo != False):
			listPeers = json.loads(responseTwo)
			peers = listPeers
		else :
			ID = fixOne
			return
	#conecta lista de peers
	consumesList()
	

def consumesList():
	global peers	
	for x in peers :
		response = tryConnect(url+x)
		if (response != False):
			listPeers = json.loads(response.text)
			comparePeers(listPeers)

#procura peers na lista local
def comparePeers(listPeers):
	global peers
	for peer in listPeers:
		marcador = 0
		for localPeer in peers:
			if ( peer == localPeer ) :
				marcador = 1
		if (marcador == 0 ):
			peers.append(peer)

def tryConnect(urlPeer):
	try:
		response = request.get(urlPeer)
		return response
	except (ConnectionError, MaxRetryError, ConnectionRefusedError):
		return False


run(host='localhost', port=ID)
