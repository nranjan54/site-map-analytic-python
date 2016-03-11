from urllib.request import urlopen
from linkFinder import LinkFinder
from general import *


class Spider:

	#Class variable (shared among all instances)
	projectName = ''
	baseUrl = ''
	domainName = ''
	queueFile = ''
	crawledFile = ''
	queue = set()
	crawled = set()

	def __init__(self, projectName, baseUrl, domainName):
		Spider.projectName = projectName
		Spider.baseUrl = baseUrl
		Spider.domainName = domainName
		Spider.queueFile = Spider.projectName + '/queue.txt'
		Spider.crawledFile = Spider.projectName + '/crawled.txt'
		self.boot()
		self.crawledPage('First Spider', Spider.baseUrl)

	@staticmethod
	def boot():
		createProjectDir(Spider.projectName)
		createDataFiles(Spider.projectName, Spider.baseUrl)
		Spider.queue = fileToSet(Spider.queueFile)
		Spider.crawled = fileToSet(Spider.crawledFile)

	@staticmethod
	def crawledPage(threadName, pageUrl):
		if pageUrl not in Spider.crawled:
			print(threadName + ' now crawling ' + pageUrl)
			print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
			Spider.addLinksToQueue(Spider.gatherLinks(pageUrl))
			Spider.queue.remove(pageUrl)
			Spider.crawled.add(pageUrl)
			Spider.updateFiles()

	@staticmethod
	def gatherLinks(pageUrl):
		htmlString = ''
		try:
			response = urlopen(pageUrl)
			# for getheader() returning other than 'text/html'
			if 'text/html' in response.getheader('Content-Type'):
			#if response.getheader('Content-Type') == 'text/html':
				htmlBytes = response.read()
				htmlString = htmlBytes.decode("utf-8")
			finder = LinkFinder(Spider.baseUrl, pageUrl)
			finder.feed(htmlString)
		except:
			print('Error: Cannot crawl page')
			return set()
		return finder.pageLinks()

	@staticmethod
	def addLinksToQueue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domainName not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def updateFiles():
		setToFile(Spider.queue, Spider.queueFile)
		setToFile(Spider.crawled, Spider.crawledFile)