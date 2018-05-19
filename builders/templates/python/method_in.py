# {{{METHODNAME}}} view
class {{{METHODNAME}}}view:
	def POST(self):
		# reading data
		data = json.loads(web.data())
		# overriding request object
		if DEBUG: data = {{{REQUESTDATA}}}
		# storing incoming log
		storeincominglog(COMPONENTNAME, '{{{METHODNAME}}}', data)
		# processing data
		res = {{{METHODNAME}}}_process(data)
		# overriding response object
		if DEBUG: res = {{{RESPONSEDATA}}}
		# returning answer
		return jsonanswer(res)
