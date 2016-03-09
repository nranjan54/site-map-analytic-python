import os

# Each website you crawl is a separate project (folder)
def createProjectDir(directory):
	if not os.path.exists(directory):
		print('Creating project ' + directory)
		os.makedirs(directory)