#Open file and Input Valiadation (User input)
fileName = input('Please enter the file name: ') # mbox-short.txt
try:
  fileOpen = open(fileName)
except:
  print(fileName, ' can not be opened.')
  print('Program ended, please restart.')
  exit()

#Print Subject lines (Upper-Case) and Subject Count (Calculation)
count = 0
for subjectLine in fileOpen:
  if subjectLine.startswith('Subject:'):
    #Upper Case
    print(subjectLine.upper())
    count = count + 1
    
fileOpen.close()

#Output
print('There were', count, 'subject lines in', fileName)
