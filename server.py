from flask import Flask
server = Flask(__name__)
@server.route('/')
def index():
	string = '<title>Home</title><style>body{width:100%;height:100%;background:url(https://im0-tub-ru.yandex.net/i?id=5fb8f760eb245cdc54d49de2d7c811ec&n=13);}</style><h1>Home Page</h1><div style="display:flex;justify-content:space-around"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return(string)
@server.route('/app')
def app():
	string = '<title>App</title><style>body{background:url(https://im0-tub-ru.yandex.net/i?id=5fb8f760eb245cdc54d49de2d7c811ec&n=13);}</style><h1>App</h1><div style="display:flex;justify-content:space-around"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return(string)
@server.route('/help')
def help():
	string = '<title>Help</title><style>body{background:url(https://im0-tub-ru.yandex.net/i?id=5fb8f760eb245cdc54d49de2d7c811ec&n=13);}</style><h1>Help Page</h1><div style="display:flex;justify-content:space-around;"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return (string)
if __name__=="__main__":
	server.run()
