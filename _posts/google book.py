import re

path = 'google notes.txt'
lineList = []
matchPattern = re.compile(r'页 –')
matchPattern1 = re.compile(r'默认集合')
matchPattern2 = re.compile(r' 项标注')
last_line = ''
file = open(path,'r',encoding='UTF-8')
while 1:
    line = file.readline()
    if not line:
        print("Read file End or Error")
        break
    elif (matchPattern.search(line)
        or matchPattern1.search(line)
        or matchPattern2.search(line)):
        last_line = line
        pass
    else:
      if not matchPattern1.search(last_line):
        lineList.append(line)


file.close()
file = open(path, 'w',encoding='UTF-8')
for i in lineList:
    file.write(i)
file.close()
