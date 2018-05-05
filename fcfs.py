def main():
	key=[1,2,3,4,5,6,7]
	num=len(key)
	proc={1:[3,1],2:[1,1],3:[2,2],4:[4,5],5:[6,7],6:[7,8],7:[5,9]}
	time=0
	i=0
	while num>0:
		var=small(num,proc,key)
		if i==0:
			time=proc.get(var)[0]
			i+=1
		if proc.get(var)[0]>time:
			time=proc.get(var)[0]
		time+=proc.get(var)[1]
		proc.get(var).append(time-proc.get(var)[0])
		print(var,"is running.\nTurn around time=",proc.get(var)[2])
		key.remove(var)
		num-=1
def small(num,dict,array):
	key=array[0]
	small=10
	for i in range(0,num):
		temp=dict.get(array[i])[0]
		if small>temp:
			small=temp
			key=array[i]
	return key

main()