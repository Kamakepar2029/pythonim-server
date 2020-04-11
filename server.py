from flask import Flask
server = Flask(__name__)
@server.route('/')
def index():
	string = '<title>Home</title><style>body{width:100%;height:100%;background:white;}</style><h1>Home Page</h1><div style="display:flex;justify-content:space-around"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return(string)
@server.route('/app')
def app():
	string = '<title>App</title><style>body{background:white;}</style><h1>App</h1><div style="display:flex;justify-content:space-around"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return(string)
@server.route('/help')
def help():
	string = '<title>Help</title><style>body{background:white;}</style><h1>Help Page</h1><div style="display:flex;justify-content:space-around;"><a href="/">Home</a><br><a href="/app">App</a><br><a href="/help">Help Page</a><br></div>'
	return (string)
print('Do you have a root?')
print('1 -yes')
print('2-no')
roots = int(input('1/2'))
if (roots == 1):
	if __name__=="__main__":
		server.run(host='0.0.0.0', port=80)
else:
	
	if __name__=="__main__":
		server.run()

