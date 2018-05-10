import sys
import requests
import json
import web
import datetime
from log import storeincominglog, storeoutgoinglog

### CONFIGURATION BEGIN ###

# server binding address
LISTENADDRESS='{{{LISTENDADDRESS}}}'
LISTENPORT={{{LISTENPORT}}}

# server ssl enabled
SSLENABLED = {{{SSLENABLED}}}

# server version
SERVERVERSION={{{SERVERVERSION}}}

# component name (useful for logs)
COMPONENTNAME = '{{{COMPONENTNAME}}}'

# debug option
DEBUG = True

### CONFIGURATION END ###

# ssl configuration
if SSLENABLED:
	from web.wsgiserver import CherryPyWSGIServer
	CherryPyWSGIServer.ssl_certificate = 'ssl/certificate.crt'
	CherryPyWSGIServer.ssl_private_key = 'ssl/certificate.key'

# list of urls accepted by the web server and relative callbacks/triggers
urls = (
	'/', 'indexview'{{{ALLOWEDMETHODS}}}
)

# web service application class
class WebServiceApplication(web.application):
	def run(self, *middleware):
		func = self.wsgifunc(*middleware)
		return web.httpserver.runsimple(func, (LISTENADDRESS, LISTENPORT))

# web service object creation
app = WebServiceApplication(urls, locals())
web.config.debug = DEBUG

### COMMON USEFUL METHODS BEGIN ###

# returns the response as a json answer
def jsonanswer(res):
	web.header('Content-Type', 'application/json')
	return json.dumps(res)

# makes a remote post request to another component
def remotepostrequest(url, data):
	if DEBUG: print url
	data = json.dumps(data)
	storeoutgoinglog(COMPONENTNAME, url, data)
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=data, headers=headers)
	json_res = r.json()
	return json_res

# empty files trigger class
def notfound():
	return web.notfound('404')

### COMMON USEFUL METHODS END ###

### OUTGOING CALLS METHODS BEGIN ###

{{{OUTGOINGMETHODSCODE}}}

### OUTGOING CALLS METHODS END ###

### VIEWS DEFINITION BEGIN ###

# index view
class indexview:
	def GET(self):
		res = {
			'module':str(COMPONENTNAME),
			'status':1,
			'server_version':str(SERVERVERSION)
		}
		return jsonanswer(res)

{{{INCOMINGMETHODSCODE}}}

### VIEWS DEFINITION END ###

# main program
if __name__ == '__main__': app.run()
