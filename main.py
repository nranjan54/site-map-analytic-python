import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Create worker threads (die when main exists)
def createWorkers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon= True
		t.start()

# Do the next job in the queue
def work():
	while True:
		url = queue.get()
		Spider.crawledPage(threading.currentThread().name, url)
		queue.task_done()

#Each queued link is a new job
def createJobs():
	for link in fileToSet(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()


#check if items in queue, if so then crawl them
def crawl():
	queuedLinks = fileToSet(QUEUE_FILE)
	if len(queuedLinks) > 0:
		print(str(len(queuedLinks)) + ' links in the queue')
		createJobs()

createWorkers()
crawl()