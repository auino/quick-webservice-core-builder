import requests
import arrow

LOGS_ENABLED = {{{LOGS_ENABLED}}}
url = '{{{LOGSERVER_URL}}}'

def storelog(componentname, methodname, data, incoming=True):
	if not LOGS_ENABLED: return True
	if incoming: methodname = '['+methodname+']'
	date = str(arrow.utcnow())
	data = {'date':date, 'componentname':componentname, 'methodname':methodname, 'data':data, 'logtype':('IN' if incoming else 'OUT')}
	r = requests.post(url, data)
	return r.json()

def storeincominglog(componentname, methodname, data):
	return storelog(componentname, methodname, data, True)

def storeoutgoinglog(componentname, methodname, data):
	return storelog(componentname, methodname, data, False)
