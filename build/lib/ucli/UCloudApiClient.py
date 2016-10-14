# -*- coding: utf-8 -*-
import hashlib, json, httplib
import urlparse
import urllib
import sys

class UCloudApiClient(object):

	def __init__(self, base_url, public_key, private_key, project_id):
		#g_params就是下面的_params，包含所有用来发起请求的参数
		self.g_params = {}
		self.g_params['PublicKey'] = public_key
		self.private_key = private_key
		self.project_id = project_id
		self.conn = UCloudApiConnect(base_url)

	def get(self, uri, params):
		_params = dict(self.g_params, **params)

		if self.project_id : 
			_params["ProjectId"] = self.project_id

		_params["Signature"] = self._verfy_ac(self.private_key, _params)
		return self.conn.get(uri, _params)

	def _verfy_ac(self, private_key, params):
		items = params.items()
		items.sort()

		params_data = ""
		for key, value in items:
			params_data = params_data + str(key) + str(value)

		params_data = params_data+private_key
    
		'''use sha1 to encode keys'''
		hash_new = hashlib.sha1()
		hash_new.update(params_data)
		hash_value = hash_new.hexdigest()
		return hash_value


class UCloudApiConnect(object):
	def __init__(self, base_url):
		self.base_url = base_url
		o = urlparse.urlsplit(base_url)
		if o.scheme == 'https':
			self.conn = httplib.HTTPSConnection(o.netloc)
		else:
			self.conn = httplib.HTTPConnection(o.netloc)

	def __del__(self):
		self.conn.close()

	def get(self, resouse, params):
		resouse += "?" + urllib.urlencode(params)
		#print("%s%s" % (self.base_url, resouse))
		self.conn.request("GET", resouse)
		response = json.loads(self.conn.getresponse().read())
		return response
		

class UCloudException(Exception):
	def __str__(self):
		return "UCloud Api Client Error"