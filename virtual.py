from collections import deque

def increment(instTime,que=deque([]),processList={},QUEUE=[]):
	count=0
	for i in range(0,len(QUEUE)):
		if processList.get(QUEUE[i])[3]<=instTime:
			que.append(QUEUE[i])
			QUEUE[i]=-1
			count+=1
			#print que
		i=i+1
	while count>0:
		QUEUE.remove(-1)
		count-=1
processList={1:[7,6,6,7,2,3],2:[5,5,5,5,-1,3],3:[0,7,7,0,2,3],4:[3,3,3,3,2,3],5:[2,4,4,2,-1,3]}
key=[1,2,3,4,5]
enter=[1,2,3,4,5]
ioInstTime=2
n=5
timeS=3
wt=5
RQ=[]
io=[]
io1=[]
AQ=[]
initialQueue=deque([])
auxliary=deque([])
instTime=0