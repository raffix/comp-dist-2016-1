from bottle import run, get, post, view, request, redirect, route, static_file
import sys
import threading
import json

sys.path.append('../t1-part2/')
from request import *
from peers import *

messages = [("Nobody", "Hello!")]
nick = "Nobody"


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

@get('/synchronize/<url>')
def searchPeers():



run(host='localhost', port=8080)