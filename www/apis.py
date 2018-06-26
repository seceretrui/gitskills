import json,logging,inspect,functools

class APIError(Exception):
	def __init__(self,error,data='',message=''):
		super(APIError，self).__init__(message)
		self.error = error
		self.data = data
		self .message = message

class APIValueError(APIError):
	def __init__(self,field,message='')
		super(APIValueError,self).__init__('value:invalid',field,message)

class APIResourceNotountError(APIError):
	def __init__(self,field,message=''):
		super(APIResourceNotFoundError,self).__init__('value:notfound',field,message)

class APIPermissonError(APIError):
	def __init__(self,message=''):
		super(APIPermissonError,self).__init__('Permision:forbidden','permission',message)