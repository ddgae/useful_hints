#random seed generator
from random import seed
from random import randint
#david gae

seed(1)
#sge_....
job_id = [300,1,5,300,20000]
count = 0;
for j in range(5):
	i = randint(0,50001)
	count = count + 1
	if i  > 0:
		print(job_id[count],i)
	elif i < 50000:
		print(job_id[count],i)
	if j == 3:
		break


