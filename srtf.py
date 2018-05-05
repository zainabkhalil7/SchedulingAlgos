def main():
	theProcess = {1:[1,15,15],2:[2,10,10],3:[4,6,6],4:[5,9,9]}
	theRange = 4
	theKey = [1,2,3,4]
	request = []
	theTime = 0
	while True: 
		temporary = -1
		temporary = function(theRange,theTime,temporary,theProcess,theKey)
		request.append(temporary)
		theTime += 1
		if temporary != -1:
			theProcess.get(temporary)[2] = theProcess.get(temporary)[2]-1
			if theProcess.get(temporary)[2] == 0:
				theRange -= 1
				print(temporary ,'turning time is:', theTime - theProcess.get(temporary)[0])
				theKey.remove(temporary)
				if theRange == 0:
					break

def function(theRange, thetheTime, thetheKey, thetheProcess, theList):
	if theKey == -1:
		for index in range (theRange):
			if(theTime >= theProcess.get(theList[index])[0]):
				theKey = theList[i]
				break
	index=0
	if theKey != -1:
		for index in range (theRange):
			if(theTime >= theProcess.get(theList[index])[0]):
				if(theProcess.get(theList[index])[2] < theProcess.get(theKey)[2]):
					theKey = theList[index]		
	return theKey
main()