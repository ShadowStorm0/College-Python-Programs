#Open file and Input Valiadation (User input)
fileName = input('Enter file name: ') # mbox-short.txt
try:
  fileOpen = open(fileName)
except:
  print('File not found. Please try again.')
  exit()
  
#Locate 'From: ' and create Dictionary
Email = dict()
for fromLine in fileOpen:
  if fromLine.startswith('From: '):
    words = fromLine.split()
    #Count
    for word in words:
        if word not in Email:
            Email[word] = 1
        else:
            Email[word] += 1
#Removes 'From:' (Only Emails)
del Email['From:']

#Convert to Tuple List
tupList = []
for i in Email:
  tpl = (i, Email[i])
  tupList.append(tpl)

#Maximum Loop (Calculation)
mostSend = sorted(tupList, key = lambda i: i[1], reverse = True)[0][0]

fileOpen.close()

#Output (Most Prolific Committer using Maximum Loop)
print('The sender with the most sends: ', mostSend)
print('Number of messages: ', Email.get(mostSend))
