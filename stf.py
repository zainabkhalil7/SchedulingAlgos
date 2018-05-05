def main():
	process = {1:[0,9],2:[0,2],3:[0,8],4:[0,6]}

	theRange = 4
	theKey = [1,2,3,4]

	timeTaken = 0

	while theRange > 0:

		temporary = minimum(theRange, process, theKey)

		if process.get(temporary)[0] > timeTaken:

			timeTaken = process.get(temporary)[0]

		timeTaken = timeTaken + process.get(temporary)[1]
		process.get(temporary).append(timeTaken - process.get(temporary)[0])

		print(temporary, 'is running.\nBurst time taken=', process.get(temporary)[2])

		theKey.remove(temporary)
		theRange = theRange - 1
def minimum(theRange, theTuple={}, theList=[]):
	
	index = 0
	thetheKey = theList[0]
	minimum = 99
	minimumtimeTaken = 0
	
	while index < theRange:	
		
		if theTuple.get(theList[index])[0] < minimum:
		
			minimum = theTuple.get(theList[index])[0]
			minimumtimeTaken = theTuple.get(theList[index])[1]
			theKey = theList[index]
		
		if theTuple.get(theList[index])[0] == minimum:
		
			if theTuple.get(theList[index])[1] < minimumtimeTaken:
		
				theKey = theList[index]
				minimumtimeTaken = theTuple.get(theList[index])[1]
		
		index = index + 1
	
	return theKey

main()