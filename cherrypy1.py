import cherrypy

class HelloWorld(object):
	def index(self):
		return "Hello World ! from CherryPy - A Minialist Python based WSGI and Web Framework"
	index.exposed= True

	def pagex(self):
		return "THis is noather page lying in the vicinity"
	pagex.exposed= True



cherrypy.quickstart(HelloWorld())
