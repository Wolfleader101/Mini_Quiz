import time
import datetime
import os
from progress.bar import Bar
from progress.spinner import Spinner
from points import points

points = 0;

bar = Bar('Loading Quiz', max=20, suffix='%(percent).1f%%')
for i in range(20):
    time.sleep(.10)
    bar.next()
bar.finish()

time.sleep(.75)
spinner = Spinner('\nWelcome to the Random Quiz! ')
for i in range(10):
    time.sleep(.10)
    spinner.next()
time.sleep(.5)
print("\n The current Date is:" ,datetime.datetime.now().strftime("%d/%m/%y") ,"\n")
time.sleep(.5)



print("Question 1.")
print("What is the colour of the sky?")
time.sleep(.5)
print("A. Red")
time.sleep(.5)
print("B. Yellow")
time.sleep(.5)
print("C. Blue")
time.sleep(.5)
print("D. pink")

Answer = input("\nAnswer: ").lower()

if Answer == 'c':
    points += 1
    time.sleep(.5)
    print("Correct!\n")
    time.sleep(.5)
    print("your points",points)
else:
    time.sleep(.5)
    print("Incorrect\n")
    time.sleep(.5)
    print("your points",points)
time.sleep(.5)
print("Answer was C!\n If you didn't get that right you should get help!\n")
time.sleep(2)



print("Question 2.")
print("What is the main search engine on most devices?")
time.sleep(.5)
print("A. Google")
time.sleep(.5)
print("B. Yahoo")
time.sleep(.5)
print("C. Bing")
time.sleep(.5)
print("D. DuckDuckGo")

Answer = input("\nAnswer: ").lower()

if Answer == 'a':
    points += 1
    time.sleep(.5)
    print("Correct!\n")
    time.sleep(.5)
    print("your points",points)
else:
    time.sleep(.5)
    print("Incorrect\n")
    time.sleep(.5)
    print("your points",points)
time.sleep(.5)
print("Answer was A!\n Surely you got this?\n")
time.sleep(2)



print("Question 3.")
print("What is a cashew?")
time.sleep(.5)
print("A. seed")
time.sleep(.5)
print("B. nut")
time.sleep(.5)
print("C. fruit")
time.sleep(.5)
print("D. Drupes")

Answer = input("\nAnswer: ").lower()

if Answer == 'a' or Answer == 'd':
    points += 1
    time.sleep(.5)
    print("Correct!\n")
    time.sleep(.5)
    print("your points",points)
else:
    time.sleep(.5)
    print("Incorrect\n")
    time.sleep(.5)
    print("your points",points)
time.sleep(.5)
print('Fun Fact: \n A Cashew is Drupe seed which is something called a "Stone frut" which is a fruit like a peach or a plum! So if you picked A or B you were correct!\n')
time.sleep(2)



print("Question 4.")
print("Who invented Facebook?")
time.sleep(.5)
print("A. Elon Musk")
time.sleep(.5)
print("B. Mark ZUCC")
time.sleep(.5)
print("C. Bill Gates ")
time.sleep(.5)
print("D. Mark Zuckerberg")

Answer = input("\nAnswer: ").lower()

if Answer == 'd':
    points += 1
    time.sleep(.5)
    print("Correct!\n")
    time.sleep(.5)
    print("your points",points)
elif Answer == 'b':
    time.sleep(.5)
    print("YOU JUST GOT ZUCCED\n")
    points -= 100
    time.sleep(.5)
    print("your points",points)
else:
    time.sleep(.5)
    print("Incorrect\n")
    time.sleep(.5)
    print("your points",points)
print("\nIf you didn't get that you were trolling righ?\n")
time.sleep(2)



print("Question 5.")
print("This is gonna be HARD!")
time.sleep(2)
print("What is the world's biggest island?")
time.sleep(.5)
print("A. Australia")
time.sleep(.5)
print("B. Greenland")
time.sleep(.5)
print("C. antarctica")
time.sleep(.5)
print("D. Iceland")

Answer = input("\nAnswer: ").lower()

if Answer == 'b':
    points += 1
    time.sleep(.5)
    print("Correct!\n")
    time.sleep(.5)
    print("your points",points)
else:
    print("Incorrect \n")
    print("your points ",points)
print("\nAnswer was B! \n Greenland is the biggest island in the world with an area of 2,166 million kilometres squared!!!")
time.sleep(5)
print("YOU WILL NOW BE BRUNG TO A NEW PAGE:")
time.sleep(5)
os.system('cls')
