#! /usr/bin/python
from __future__ import division
import os,sys
import re


if len(sys.argv)==2:
    inputFilePath=sys.argv[1]
    outFilePath="Statistic.INFO"
elif len(sys.argv)==3:
        inputFilePath=sys.argv[1]
        outFilePath=sys.argv[2]
else:
    print "usage: python statistic.py [input file path] [output file path, this param is not necessary. Default is a file named Statistic.INFO in current directory]"
    exit()

print inputFilePath,"-",outFilePath


try:
    #fsock = open("Libra.INFO", "r")
    fsock = open(inputFilePath, "r")
except IOError:
    print "The file don't exist, Please check!"
    exit()
#print "Process the INFO file"
#print 'The file mode is ',fsock.mode
#print 'The file name is ',fsock.name
#P = fsock.tell()
#print 'the postion is %d' %(P)

dictToSaveStatisticResult={} #in the list [0] stores total number of time, list [1] stores total time 

#pattern = re.compile(r'\w+\s\w+')
pattern = re.compile(r'\[\w+\s*\w*\]:\d+.\d*')

AllLines = fsock.readlines()
totalLines=len(AllLines)
i=0
for EachLine in AllLines:
    i+=1
    print "In row:",i,"  Total rows:",totalLines
    #process
    results = pattern.findall(EachLine)
    #print results
    for result in results:
	#print result
	time=result.split(':')
	#print time[0]
	#print time[1]
	if time[0] in dictToSaveStatisticResult.keys():
	    dictToSaveStatisticResult[time[0]][1]+=float(time[1]);
	    dictToSaveStatisticResult[time[0]][0]+=1;
        else:
	    tempList=[1,float(time[1])]
	    dictToSaveStatisticResult[time[0]]=tempList;
    #if i==66:
    #    break
	

#print dictToSaveStatisticResult

fsock.close()

#foutput=open("Statistic.INFO","w")
foutput=open(outFilePath,"w")
for key in dictToSaveStatisticResult.keys():
    content=key+" :: [total time]: "+str(dictToSaveStatisticResult[key][1] )+" ms  [total number of time]: "+str(dictToSaveStatisticResult[key][0])+"  [avergage time]: "+str(dictToSaveStatisticResult[key][1]/dictToSaveStatisticResult[key][0])+" ms\n"
    foutput.writelines(content)
foutput.close()

print "Complete"



