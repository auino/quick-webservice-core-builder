from utils import writetofile
# exports an uml file containing the sequence diagram of the program (in PlantUML format)
def exportuml(interactions, outputdirectory, foldername, filename):
	content = '@startuml\n'
	for i in interactions:
		content += i.get('sender')+' -> '+i.get('recipient')+': '+i.get('name')+'\n'
	content += '@enduml\n'
	# writing UML diagram file to output
	return writetofile(outputdirectory, foldername, filename, content)
