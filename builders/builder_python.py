import os
from utils import getfoldername, getfullpathname, getserverurl, loadfilecontent, writetofile

def builder_makedirectory(outputdirectory, foldername, islog=False):
	directory = getfullpathname(outputdirectory, foldername)
	res = not os.path.exists(directory)
	if res: os.makedirs(directory)
	return res

def builder_writecode(outputdirectory, module, version, logmodule=None):
	server = module.get('server')
	if logmodule == None:
		# TODO, ONLY NODEJS ALLOWED IN THE CURRENT VERSION
		pass
	# getting log server url
	logserverurl = getserverurl(logmodule)+'/log/'
	# building log file from template
	logcode = loadfilecontent('./builders/templates/python/log.py')
	replacements = {
		'{{{LOGS_ENABLED}}}': True,
		'{{{LOGSERVER_URL}}}': logserverurl
	}
	for k in replacements: logcode = logcode.replace(k, str(replacements.get(k)))
	# writing log file to output
	writetofile(outputdirectory, getfoldername(module), 'log.py', logcode)
	# generating outgoing methods implementations
	methodcode_out = loadfilecontent('./builders/templates/python/method_out.py')
	outgoingmethodscode = ''
	for el in module.get('output_interactions'):
		interaction = el.get('interaction')
		url = getserverurl(el.get('server'))
		url += '/'+interaction.get('method_uri')+'/'
		sampledata = interaction.get('sampledata')
		replacements = {
			'{{{METHODNAME}}}': interaction.get('name'),
			'{{{URL}}}': url,
			'{{{SENTDATA}}}':	 sampledata.get('sent'),
			'{{{RECEIVEDDATA}}}': sampledata.get('received')
		}
		methodcode = methodcode_out
		for k in replacements: methodcode = methodcode.replace(k, str(replacements.get(k)))
		outgoingmethodscode += methodcode
	# generating allowed incoming methods implementations
	methodcode_in = loadfilecontent('./builders/templates/python/method_in.py')
	incomingmethodscode = ''
	allowedmethods = ''
	for method in module.get('input_interactions'):
		sampledata = module.get('input_interactions').get(method).get('sampledata')
		allowedmethods+=',\n\t'+'\'/'+method+'/\''+', \''+method+'view\''
		replacements = {
			'{{{METHODNAME}}}': method,
			'{{{REQUESTDATA}}}': sampledata.get('received'),
			'{{{RESPONSEDATA}}}': sampledata.get('sent')
		}
		methodcode = methodcode_in
		for k in replacements: methodcode = methodcode.replace(k, str(replacements.get(k)))
		incomingmethodscode += methodcode
	# generating main server program implementation
	servercode = loadfilecontent('./builders/templates/python/server.py')
	replacements = {
		'{{{LISTENDADDRESS}}}': server.get('bindaddress'),
		'{{{LISTENPORT}}}': server.get('listeningport'),
		'{{{SSLENABLED}}}': ('True' if server.get('ssl') else 'False'),
		'{{{SERVERVERSION}}}': version,
		'{{{COMPONENTNAME}}}': module.get('name'),
		'{{{OUTGOINGMETHODSCODE}}}': outgoingmethodscode[:-1],
		'{{{ALLOWEDMETHODS}}}': allowedmethods,
		'{{{INCOMINGMETHODSCODE}}}': incomingmethodscode[:-1]
	}
	for k in replacements: servercode = servercode.replace(k, str(replacements.get(k)))
	# writing main server file to output
	writetofile(outputdirectory, getfoldername(module), 'server.py', servercode+'b')
	# return result
	return True