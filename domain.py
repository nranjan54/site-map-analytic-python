from urllib.parse import urlparse

# Get Domain Name
def getDomainName(url):
	try:
		results = getSubDomainName(url).split('.')
		return results[-3] + '.' + results[-2] + '.' + results[-1]
		#return results[-2] + '.' + results[-1]
	except:
		return ''


#Get sub domain name
def getSubDomainName(url):
	try:
		return urlparse(url).netloc
	except:
		return ''