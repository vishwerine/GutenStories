### this script analyzes all the directory_filenames_imgchecks.txt file and filters the ones with less than 4 images in the story.

filnames = open('directory_filenames_imgchecks.txt','r').read().splitlines()


print(len(filnames))


indices = [i for i in range(len(filnames)) if len(filnames[i].split()) > 3]

print(len(indices))

outFile = open('directory_filenames_imgchecks1.txt','w')

for indice in indices:
	outFile.write(filnames[indice]+'\n')

outFile.close()


