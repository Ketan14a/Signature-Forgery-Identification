import os

DATADIR="train128"


for i in range(1,70):

	if i<10:
		D1='00'+str(i)
		D2='00'+str(i)+'_forg'
	else:
		D1='0'+str(i)
		D2='0'+str(i)+'_forg'

	TargetPath = DATADIR+"/"+D1
	os.mkdir(TargetPath)
	TargetPath = DATADIR+"/"+D2
	os.mkdir(TargetPath)



