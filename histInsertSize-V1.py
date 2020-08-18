import sys
#import array

# Wei Gu 3/16/15

targetCol = int(sys.argv[1])
inFile = open(sys.argv[2])
outFile = open(sys.argv[3], 'w')

hist = [0]*201

for line in inFile.xreadlines(): 
	
    lineCol = line.split('\t')
    
    #print targetCol, lineCol[targetCol-1], abs(int(lineCol[targetCol-1]))/5
    
    
    length = abs(int(lineCol[targetCol-1]))/5
    if (length > 199):
        hist[200] += 1
    else:
        hist[length] += 1




countUp = 1
totalSum = 0
while countUp < 201 :
	totalSum += hist[countUp]
	countUp += 1
totalSum = float(totalSum)

countUp = 1
while countUp < 201 :
	outFile.write('%i\t%i\t%i\t%f\n'%(countUp,countUp*5,hist[countUp],hist[countUp]/totalSum))
	countUp += 1
        
inFile.close()
outFile.close()

print "it's done"






