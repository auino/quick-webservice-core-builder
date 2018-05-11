# {{{METHODNAME}}} view
class {{{METHODNAME}}}view:
	def POST(self):
		data = json.loads(web.data())
		print "LOG:", str(data)
		return jsonanswer(res)
