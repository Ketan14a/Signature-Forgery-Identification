import os
import cv2
import numpy as np
from tqdm import tqdm
import pickle

DATADIR = "train128"
CATEGORIES = ["Genuine", "Forged"]
training_data = []


SkipList = [5,7,8,10,11]
for i in tqdm(range(1,70)):
	PivotFlag=0
	if i in SkipList:
		continue
	if i<10:
		D1='00'+str(i)
		D2='00'+str(i)+'_forg'
	else:
		D1='0'+str(i)
		D2='0'+str(i)+'_forg'

	path1=os.path.join(DATADIR,D1)
	for img in os.listdir(path1): 
		if PivotFlag==0:
			pivotArray= cv2.imread(os.path.join(path1,img) ,cv2.IMREAD_GRAYSCALE)
			Feature=np.subtract(pivotArray,pivotArray)
			training_data.append([Feature,0])
			PivotFlag=1
		else:
			SecondArray=cv2.imread(os.path.join(path1,img) ,cv2.IMREAD_GRAYSCALE)
			Feature=np.subtract(pivotArray,SecondArray)
			training_data.append([Feature,1])

	path2=os.path.join(DATADIR,D2)
	for img in os.listdir(path2): 
			SecondArray=cv2.imread(os.path.join(path2,img) ,cv2.IMREAD_GRAYSCALE)
			Feature=np.subtract(pivotArray,SecondArray)
			training_data.append([Feature,0])


X = []
y = []

for features,label in training_data:
    X.append(features)
    y.append(label)


X = np.array(X).reshape(-1,128,128,1)
# Storing the training set into Pickle file for easy import in some other file
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()




           
           


