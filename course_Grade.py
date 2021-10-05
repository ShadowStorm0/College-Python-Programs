#Intilize lists
chapterList = []
quizList = []
finalProjectList = []
finalExamList = []

#Chapter Projects
i = 1 #For Count Reset
print("Please enter 10 'Chapter Project' scores between 0 and 100\n")
for n in range(10):
  while True:
    try:
      #User input
      print("Chapter Project: ", i)
      chapterScore = float(input()) 
      #Check if in bounds
      if chapterScore < 0 or chapterScore > 100:
        print("Please enter a valid score between 0 and 100\n")
        continue
      #Create score list
      i = i + 1 #Count to terminal
      chapterList.append(chapterScore)
    #Check if number
    except ValueError:    
      print("Please try again and input a valid score between 0 and 100\n") 
      continue
    break
#Adds the list and average (Calculation)
chapterSum = (sum(chapterList))
chapterScore = chapterSum / 10


#Quizzes
i = 1 #For Count Reset
print("Please enter 5 'Quiz' scores between 0 and 100\n")
for n in range(5):
  while True:
    try:
      #User input
      print("Quiz: ", i)
      quizScore = float(input()) 
      #Check if in bounds
      if quizScore < 0 or quizScore > 100:
        print("Please enter a valid score between 0 and 100\n")
        continue
      #Create score list
      i = i + 1 #Count to terminal
      quizList.append(quizScore)
    #Check if number
    except ValueError:    
      print("Please try again and input a valid score between 0 and 100\n") 
      continue
    break
#Adds the list and average (Calculation)
quizSum = (sum(quizList))
quizScore = quizSum / 5


#Final Programming Project Assessment
i = 1 #For Count Reset
print("Please enter 1 'Final Project' score between 0 and 100\n")
for n in range(1):
  while True:
    try:
      #User input
      print("Final Project: ", i)
      finalProjectScore = float(input()) 
      #Check if in bounds
      if finalProjectScore < 0 or finalProjectScore > 100:
        print("Please enter a valid score between 0 and 100\n")
        continue
      #Create score list
      i = i + 1 #Count to terminal
      finalProjectList.append(finalProjectScore)
    #Check if number
    except ValueError:    
      print("Please try again and input a valid score between 0 and 100\n") 
      continue
    break
#Adds the list and average (Calculation)
finalProjectSum = (sum(finalProjectList))
finalProjectScore = finalProjectSum / 1


#Final Exam
i = 1 #For Count Reset
print("Please enter 1 'Final Exam' score between 0 and 100\n")
for n in range(1):
  while True:
    try:
      #User input
      print("Final Exam: ", i)
      finalExamScore = float(input()) 
      #Check if in bounds
      if finalExamScore < 0 or finalExamScore > 100:
        print("Please enter a valid score between 0 and 100\n")
        continue
      #Create score list
      i = i + 1 #Count to terminal
      finalExamList.append(finalExamScore)
    #Check if number
    except ValueError:    
      print("Please try again and input a valid score between 0 and 100\n") 
      continue
    break
#Adds the list and average (Calculation)
finalExamSum = (sum(finalExamList))
finalExamScore = finalExamSum / 1


#Averages the scores (Calculation)
course_Grade = (chapterScore + quizScore + finalProjectScore + finalExamScore) / 4

#Round to one decimal place (Calculation)
course_Round = round(course_Grade, 1)

#Get Letter grade (Output)
print("\n")
if course_Round >= 89.5 and course_Round <= 100:
    print('The Letter Grade is: A')
elif course_Round >= 79.5 and course_Round <= 89.4:
    print('The Letter Grade is: B')
elif course_Round >= 69.5 and course_Round <= 79.4:
    print('The Letter Grade is: C')
elif course_Round >= 59.5 and course_Round <= 69.4:
    print('The Letter Grade is: D')
else:
    print('The Letter Grade is: F')

#Course Grade (Output)
print('The Course Grade is: ' + str(course_Round) + '%\n')


