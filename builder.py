import sys
import json

sys.path.insert(0, './builders')

from utils import getfoldername

EXPECTEDARGS = 3

if len(sys.argv) != EXPECTEDARGS:
	print "Usage:", str(sys.argv[0]), "<model_file>", "<output_directory>"
	sys.exit(0)

modelfilename = sys.argv[1]
modelfilecontent = open(modelfilename, 'r').read()
modelfilecontent = json.loads(modelfilecontent)

outputdirectory = sys.argv[2]

def createmoduleproject(outputdirectory, module, version, logmodule=None):
	# module project directory creation/initialization
	foldername = 'log'
	if logmodule != None: foldername = getfoldername(module)
	res_makedir = libname.builder_initializeprogram(outputdirectory, foldername, module.get('ssl'))
	# writing module code
	res_writecode = libname.builder_writecode(outputdirectory, module, version, logmodule)
	return [res_makedir, res_writecode]

# program version retrieval
version = modelfilecontent.get('version')

# log module retrieval
logmodule = modelfilecontent.get('log')

# log module creation
if modelfilecontent.get('log').get('enabled'):
	# library import
	libname = "builder_"+logmodule.get('language')
	import importlib
	libname = importlib.import_module(libname)
	# module project creation
	createmoduleproject(outputdirectory, logmodule, version)

# retrieving all servers first
servers = {}
for x in modelfilecontent.get('modules'): servers[x.get('name')] = x.get('server')

# other modules creation
for module in modelfilecontent.get('modules'):
	# getting output interactions
	module['output_interactions'] = []
	for i in modelfilecontent.get('interactions'):
		if i.get('sender') != module.get('name'): continue
		module['output_interactions'].append({'server':servers.get(i.get('recipient')), 'interaction':i})
	# getting input interactions
	module['input_interactions'] = {}
	for i in modelfilecontent.get('interactions'):
		if i.get('recipient') != module.get('name'): continue
		module['input_interactions'][i.get('method_uri')] = i
		tmp = i.get('sampledata').get('sent')
		module['input_interactions'][i.get('method_uri')]['sampledata']['sent'] = i.get('sampledata').get('received')
		module['input_interactions'][i.get('method_uri')]['sampledata']['received'] = tmp
	# library import
	libname = "builder_"+module.get('server').get('language')
	import importlib
	libname = importlib.import_module(libname)
	# module project creation
	createmoduleproject(outputdirectory, module, version, logmodule)
