import os
import cv2


IMG_SIZE=128
DATADIR="train"
TARGETDIR="train128"

SkipList = [5,7,8,10,11]
for i in range(49,69):

	if i in SkipList:
		continue
	if i<10:
		D1='00'+str(i)
		D2='00'+str(i)+'_forg'
	else:
		D1='0'+str(i)
		D2='0'+str(i)+'_forg'

	path=os.path.join(DATADIR,D1)
	NameCounter=1
	for img in os.listdir(path):
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE) # convert to array
                resized = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE),)
                TargetPath= "./"+TARGETDIR+"/"+D2+"/"+str(NameCounter)+".png"
                NameCounter+=1
                cv2.imwrite(TargetPath,resized)
            

    
           





               