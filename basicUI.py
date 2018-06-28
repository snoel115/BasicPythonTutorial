#Simple GUI
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
	
#create the window
root = Tk()

root.title("Labeler")		#modify the root window label
root.geometry("200x200")		#set the size of the window`

app = Frame(root) 			#create the frame to hold other element in the window
app.grid()					#set a grid to attach the components in the window

#create a label
label = Label(app, text="This is a label!")
label.grid()				#put the label on the grid`

#create a button
button1 = Button(app, text="This is my fist button!")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "this is a new text") #how to set the text in a button once created

button3 = Button(app)
button3.grid()
button3["text"] = "text through dictionary" #how to set the text in a button once created


#kick off the event loop to keep the window open and to get it ready to trigger events
root.mainloop()
