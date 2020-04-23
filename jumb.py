import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle

answer = ["google","youtube","india","cake"]
words=[]
num= random.randint(0,len(words))
for i in answer:
	word=list(i)
	shuffle(word)
	words.append(word)

def initial():
	global words,num
	lb1.configure(text=words[num])
def ans_check():
	global words,num,answer
	user_input=e1.get()
	if(user_input==answer[num]):
		messagebox.showinfo("Success!! Yup this is right")
		Reset()
	else:
		messagebox.showinfo("Error!! This isn't right")
		e1.delete(0,END)
def Reset():
		global words,num,answer
		num= random.randint(0,len(words))
		lb1.configure(text=words[num])
		e1.delete(0,END)
		
		
root = tkinter.Tk()
root.geometry("300x300")

lb1 = Label(root,font = 'times 20')
lb1.pack(pady=30,ipady=10,ipadx=10)

answer12 = StringVar()
e1 = Entry(root,textvariable=answer)
e1.pack(ipady=5,ipadx=5)

button1 = Button(root,text="Check",width=20,command=ans_check)
button1.pack(pady=40)

button2 = Button(root,text="Reset",width=20,command=Reset)
button2.pack()

initial()
root.mainloop()

