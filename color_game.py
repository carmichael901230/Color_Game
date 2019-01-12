import random
from tkinter import *

timeLimit = 30
timeLeft = timeLimit
score = 0
colors = ["grey", "black", "red", "green", "blue", "cyan", "yellow", "pink"]
color = colors[1]
gameStatus = 0

def gameLoop():
	if timeLeft == timeLimit:
		countDown()

def countDown():
	global timeLabel,colorLabel, timeLeft
	
	if timeLeft>0:
		timeLabel.config(text="Time Left: " + str(timeLeft))
		timeLeft-=1
		timeLabel.after(1000,countDown)
		scoreLabel.config(text="Score: " + str(score))
	else:
		timeLabel.config(text="Time Left: " + str(timeLeft))
		colorLabel.config(text="Time Up", fg="black")

def click(text):
	global colorText,timeLeft,textIndex,colorIndex,color,colorLabel,score,scoreLabel
	if timeLeft>0:
		# if correctly answered color, add score
		if (text.lower() == color):
			score += 1
			scoreLabel.config(text="Score: " + str(score))
		# generate another pair of color and text	
		colorIndex = random.randint(0,len(colors)-1)
		color=colors[colorIndex]
		textIndex = colorIndex
		while (textIndex == colorIndex):		# avoid same color and text
			textIndex = random.randint(0,len(colors)-1)
		# Display colorText
		colorText=colors[textIndex]
		colorLabel.config(text=colorText.upper(), fg=color)


# Create tk object and game window
master = Tk()
master.resizable(width=False, height=False)

master.geometry("455x360")
master.title("Color Game")

instruction = Label(master, text="Click the Correct Color of Text", width=25, fg="black", pady=20)
instruction.config(font=("times",25))

# Initial a pair of random Color and color text
colorIndex = random.randint(0,len(colors)-1)
color = colors[colorIndex]
textIndex = colorIndex
while (textIndex == colorIndex):
	textIndex = random.randint(0,len(colors)-1)
colorText=colors[textIndex]

# Time and Score board
timeLabel = Label(master, text="",pady=10)
scoreLabel = Label(master, text="")

# Display randomly initialed colorText
colorLabel = Label(master, text=colorText.upper(), fg=color, pady=13, relief="solid", bg="white")
colorLabel.config(font=("Helvetica", 50, "bold"))

# Pack-up top Frame
instruction.grid(row=0, column=0, columnspan=4)
timeLabel.grid(row=1, column=0, columnspan=4)
scoreLabel.grid(row=2, column=0, columnspan=4)
colorLabel.grid(row=3, column=0, columnspan=4,sticky=W+N+E+S)

# Buttons
greyBtn = Button(master, text="Grey", pady=5, width=8, font=("times",10,"bold"), command=lambda:click(greyBtn["text"]))
blackBtn = Button(master, text="Black", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(blackBtn["text"]))
redBtn = Button(master, text="Red", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(redBtn["text"]))
greenBtn = Button(master, text="Green", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(greenBtn["text"]))
blueGtn = Button(master, text="Blue", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(blueGtn["text"]))
cyanBtn = Button(master, text="Cyan", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(cyanBtn["text"]))
yellowBtn = Button(master, text="Yellow", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(yellowBtn["text"]))
pinkBtn = Button(master, text="Pink", pady=5, width=8,font=("times",10,"bold"), command=lambda:click(pinkBtn["text"]))

# Pack-up Buttons
greyBtn.grid(row=4,column=0,sticky=W+N+E+S)
blackBtn.grid(row=4,column=1,sticky=W+N+E+S)
redBtn.grid(row=4,column=2,sticky=W+N+E+S)
greenBtn.grid(row=4,column=3,sticky=W+N+E+S)
blueGtn.grid(row=5,column=0,sticky=W+N+E+S)
cyanBtn.grid(row=5,column=1,sticky=W+N+E+S)
yellowBtn.grid(row=5,column=2,sticky=W+N+E+S)
pinkBtn.grid(row=5,column=3,sticky=W+N+E+S)

# Fake copyright lol
Label(master, text="(c) 2018 Zhaochun Wang (TM)", fg="grey", pady=10).grid(columnspan=4,sticky=W+N+E+S)

gameLoop()
master.mainloop()

