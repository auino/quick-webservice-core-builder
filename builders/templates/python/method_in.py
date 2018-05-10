# {{{METHODNAME}}} view
class {{{METHODNAME}}}view:
	def POST(self):
		data = json.loads(web.data())
		# TODO: remove the following line
		if DEBUG: data = {{{REQUESTDATA}}}
		storeincominglog(COMPONENTNAME, '{{{METHODNAME}}}', data)
		# ...
		# TODO: process data
		# ...
		# TODO: remove the following line
		if DEBUG: res = {{{RESPONSEDATA}}}
		return jsonanswer(res)
