### this script analyzes all directory filenames and checks if the image paths exist

from bs4 import BeautifulSoup
import os

dirfilenames = open('directory_filenames.txt','r').read().splitlines()


raw_dirname = 'rawdata'

outFile = open('directory_filenames_imgchecks.txt','w')

for fil in dirfilenames:
	soup = BeautifulSoup( open( os.path.join( os.path.join(raw_dirname,fil) , fil+'.htm' ), 'r') , 'html.parser' )
	imgs = soup.findAll('img')

	outFile.write(fil + ' ')
	for img in imgs:
		if 'src' in img.attrs.keys():
			if os.path.exists( os.path.join( os.path.join(raw_dirname,fil) , img.attrs['src']) ):
				outFile.write(img.attrs['src']+' ')

	outFile.write('\n')

outFile.close()






