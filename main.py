from tkinter import *
from PyDictionary import PyDictionary
root = Tk()

#background
bg = "#ffff77"
fg = "#000077"
root.config(background=bg)

#heading
hframe = Frame(root, bg=bg)
hframe.place(relx=0.5, rely=0.2, anchor=CENTER)
Label(hframe, text="Dictionary", bg=bg, fg=fg, font=("Comic Sans MS", 20, "underline")).pack()

#prompt
mframe = Frame(root, bg=bg)
mframe.place(relx=0.5, rely=0.3, anchor=CENTER)
Label(mframe, text="Enter a word: ", bg=bg, fg=fg, font=("Comic Sans MS", 10)).pack(side=LEFT)

#entry box
word = StringVar()
entrybox = Entry(mframe, textvariable=word)
entrybox.pack(side=RIGHT)

#meaning Label
lframe = Frame(root, bg=bg)
lframe.place(relx=0.5, rely=0.44, anchor=CENTER)
meaning = Text(lframe, bg=bg, fg=fg, font=("Comic Sans MS", 10), width=32, height=7)
meaning.pack()

#update meaning label
dictionary = PyDictionary()
def submit():
	meaning.delete(1.0, END)
	try:
		temp = dictionary.meaning(word.get())
	except:
		temp = "Invalid word"
	meaning.insert(1.0, temp)

#submit button
bframe = Frame(root, bg=bg)
bframe.place(relx=0.5, rely=0.6, anchor=CENTER)
submitbtn = Button(bframe, text="Search", bg="pink", fg=fg, activebackground="turquoise", font=("Comic Sans", 10), command=submit)
submitbtn.pack()

root.mainloop()
