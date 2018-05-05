from collections import deque

def currentAppend(instTime,key,que=[]):
	for i in range(0,instTime):
		que.append(key)
	

def increment(instTime,que=deque([]),processList={},key=[],io=[],enter=[]):
	count=0	
	for i in range(0,len(enter)):
		if processList.get(enter[i])[0]<=instTime:
			que.append(enter[i])
			count+=1
			enter[i]=-1
	while count>0:
		enter.remove(-1)
		count-=1
	for i in range(0,len(io)):
		if processList.get(io[i])[3]<=instTime:
			que.append(io[i])
			count+=1
			io[i]=-1
	while count>0:
		io.remove(-1)
		count-=1


#procss=name:[a.t,bt,r.t,nextqueinstTime,i/oremaininginstTime,instTimeforruning]
processList={1:[7,6,6,7,2,3],2:[5,5,5,5,-1,3],3:[0,7,7,0,2,3],4:[3,3,3,3,2,3],5:[2,4,4,2,-1,3]}
key=[1,2,3,4,5]
enter=[1,2,3,4,5]
IOInstTime=2
n=5
timeS=3
wt=5
RQ=[]
io=[]
initialQueue=deque([])
instTime=0