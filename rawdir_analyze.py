## this python script - reads and analyzes raw html folders scraped off gutenberg

import os

raw_directory_name = 'rawdata'

fils  = os.listdir(raw_directory_name)
fils.sort()


######## filter - check if it is a directory ################

dirFiles = []

for fil in fils:
	if fil.split('-')[-1] == 'h' and os.path.isdir(os.path.join(raw_directory_name, fil)):
		dirFiles.append( fil)

print(len(dirFiles))
########################################



###### filter - check if htm file exists and images folder exists ###########

dirFiles2 = open('directory_filenames.txt','w')

for fil in dirFiles:
	if os.path.exists( os.path.join( os.path.join(raw_directory_name, fil) , fil+'.htm') ) and os.path.exists(os.path.join( os.path.join(raw_directory_name, fil), 'images') ):
		dirFiles2.write(fil+'\n')

dirFiles2.close()

