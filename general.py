import os

# Each website you crawl is a separate project (folder)
def createProjectDir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		print('Created project ' + directory)

#Create queue and crawled files (if not created)
def createDataFiles(projectName, baseUrl):
	queue = projectName + '/queue.txt'
	crawled = projectName + '/crawled.txt'
	if not os.path.isfile(queue):
		writeFile(queue, baseUrl)
	if not os.path.isfile(crawled):
		writeFile(crawled, '')

#Create a new file
def writeFile(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

#Add data onto an existing file
def appendToFile(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')

#Delete the contents of the file
def deleteFileContents(path):
	with open(path, 'w'):
		pass

#Read a file and convert each line to a set items
def fileToSet(fileName):
	results = set()
	with open(fileName, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

#Iterate through a set, each item will be a new line in the file
def setToFile(links, file):
	deleteFileContents(file)
	for link in sorted(links):
		appendToFile(file, link)