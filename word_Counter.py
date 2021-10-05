#Open file and Input Valiadation (User input)
fileName = input('What is the name of the file you want to open? ') # mbox-short.txt
try:
  fileOpen = open(fileName)
except:
  print('File not found. Please try again.')
  exit()

#Create Dictionary 
counts = dict()
for line in fileOpen:
    words = line.split()
    #Count
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

fileOpen.close()

#Output dictionary
print(counts)

#Output (Most common word)
mostCommon = (max(counts, key=counts.get))
print('The most common word is: ', mostCommon)

#Output (Word occurred count)
print('This word occurred: ', counts.get(mostCommon) , ' times')
