#! /usr/bin/python
import filecmp
import os
import shutil
import time
import urllib
#import urllib.request 
oldFile = 'interrupt.py'
newFile = 'interruptNew.py'
homePi = '/home/pi/'
githubPath = 'https://raw.githubusercontent.com/gummibearface/Meeseeks/master/interrupt.py'

urllib.urlretrieve(githubPath, homePi + newFile)
#urllib.request.urlretrieve(githubPath, homePi + newFile)


#If directory doesn't exist create it
if not os.path.exists(homePi + 'archive'):
    os.makedirs(homePi + 'archive')
	
#If python script doesn't exist then basically just rename the new file we pulled
if not os.path.exists(homePi +oldFile):
	print('Old script does not exist, renaming new script')
	shutil.move(homePi + newFile, homePi + oldFile);
#If script did exist, then do comparisons
else:
	#If the files are different then move the old file to the archive directory with timestamp suffix
	#then rename the file
	if(not filecmp.cmp(homePi + newFile, homePi + oldFile)):
		print('Files are different archiving')
		ts = int(time.time())
		shutil.move(homePi + oldFile, homePi + "archive/interrupt" + str(ts) + ".py")
		shutil.move(homePi + newFile, homePi +oldFile);
	#Otherwise the files are identical so don't need to archive 
	#just delete the new file
	else:
		print('Files are identical not moving, deleting new file')
		os.remove(homePi + newFile)
