# {{{METHODNAME}}} outgoing request
def {{{METHODNAME}}}request(data):
	url = '{{{URL}}}'
	# overriding request object
	if DEBUG: data = {{{SENTDATA}}}
	# making the remote request
	res = remotepostrequest(url, data)
	# overriding response object
	if DEBUG: res = {{{RECEIVEDDATA}}}
	# method return object
	return res
