from collections import deque
def main():
	RQueue=[]
	ready=deque([])
	time=0
	key=[1,2,3,4]
	enter=[1,2,3,4]
	proc={1:[1,1,1],2:[4,2,2],3:[3,3,4],4:[5,4,5]}
	num=len(key)
	while(num>0):
		function(time,proc,enter,ready)
		if not(ready):
			RQueue.append(-1)
			time+=1
		else:
			num-=1
			element=ready.popleft()
			time+=proc.get(element)[2]
			temp=proc.get(element)[2]
			for k in range(0,temp):
				RQueue.append(element)
			print(element,'\nTurn around time=',time-proc.get(element)[0])			
def function(time,proc,enter,que):
	array=[]
	for i in range (len(enter)):
		if(proc.get(enter[i])[0]<=time):
			array.append(enter[i])
	maximum=-1
	for i in range(len(array)):
		maximum=i
		for j in range (i,len(array)):
			if(proc.get(array[j])[2]>proc.get(array[i])[2]):
				maximum=j
		if not(maximum==i):
			temp=array[maximum]
			array[maximum]=array[i]
			array[i]=temp
	for i in range(len(array)):
		enter.remove(array[i])
		que.append(array[i])
	return len(array)
main()