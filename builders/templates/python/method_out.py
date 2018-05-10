# {{{METHODNAME}}} outgoing request
def {{{METHODNAME}}}request(data):
	url = '{{{URL}}}'
	# TODO: remove the following line
	if DEBUG: data = {{{SENTDATA}}}
	res = remotepostrequest(url, data)
	# TODO: remove the following line
	if DEBUG: res = {{{RECEIVEDDATA}}}
	return res
