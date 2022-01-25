
from tkinter import *
from random import randint

root = Tk()
root.title("Secure Password Generator")
root.iconbitmap("")
root.geometry("425x400")

password = chr(randint(33, 126))

def new_pw():
	#Clears entry box
	pw_entry.delete(0, END)

	#Get PW Length, converts to int
	pw_length = int(length_entry.get())

	#Create variable placeholder
	password = ""

	#Loop through password length
	for x in range(pw_length):
		password += chr(randint(33, 126))

	#Output password
	pw_entry.insert(0, password)

#Copy to clipboard
def clipper():
	#Clear
	root.clipboard_clear()
	#Copy
	root.clipboard_append(pw_entry.get())


#Label Frame
lf = LabelFrame(root, text="Define password length:")
lf.pack(pady=20)

#Entry box for password length
length_entry = Entry(lf,text="", font=("Arial", 24))
length_entry.pack(pady=20, padx=20)

#Return Password
pw_entry = Entry(root, text="", font=("Arial", 24),bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#Button Frames
b_frame = Frame(root)
b_frame.pack(pady=20)

#Buttons
pw_button = Button(b_frame, text="Generate Password", command=new_pw)
pw_button.grid(row=0, column=0, padx=10)

clip_button = Button(b_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)



root.mainloop()