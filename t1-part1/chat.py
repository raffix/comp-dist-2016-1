from bottle import run, get, post, view, request, redirect, route
import json
import requests
import sys

sys.path.append('../t1-part2/')
from request import *
from peers import *

ID = 0
peers = []
porta = 8080


@get('/<name>')
@view('index')
@route('/<name>')
def index(name = 'Nobody'):
	return {'nick' : name,'message': mensagens }


@post('/send')
def sendMessage():
    global nick
    m = request.forms.get('message')
    n = request.forms.get('nick')
    messages.append([n, m])
    nick = n
    redirect('/'+n) 	



run(host='localhost', port=(porta + ID))
