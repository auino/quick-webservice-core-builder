# returns the main folder name for a given module
def getfoldername(module):
	return module.get('name').lower()

# returns the full path name for a given directory/file
def getfullpathname(maindir, folder, file=None):
	if maindir[-1:] != '/': maindir += '/'
	res = maindir + folder
	if res[-1:] != '/': res += '/'
	if file != None: res += file
	return res

# computes the full server url from a given (server) object
def getserverurl(server):
	res = 'http'+('s' if server.get('ssl') else '')+'://'+server.get('domainname')
	if (not server.get('ssl')) and server.get('listeningport') != 80: res += ':'+str(server.get('listeningport'))
	if server.get('ssl') and server.get('listeningport') != 443: res += ':'+str(server.get('listeningport'))
	return res

# writes content to file
def writetofile(outputdirectory, foldername, filename, content):
	outputfile = getfullpathname(outputdirectory, foldername, filename)
	file = open(outputfile, 'w')
	file.write(content)
	file.close()
	return True

# loads content from file
def loadfilecontent(inputfile):
	return open(inputfile, 'r').read()
