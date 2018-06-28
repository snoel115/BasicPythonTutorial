#Simple GUI
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

class Application(Frame):
	def __init__(self, master):
		''' Initialize the frame '''
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		''' create button, text, and entry widgets'''
		self.lblInstruction = Label(self, text = "Enter the password")
		self.lblInstruction.grid(row=0, column=0, columnspan=2, sticky=W) #W=west - starting left side of the form
		
		self.txtPassword = Entry(self)						#create a textbox
		self.txtPassword.grid(row=0, column=1, sticky = W)	#West, North, East, South
		
		self.btnSubmit_button = Button(self, text="Submit", command = self.reveal) # call the event
		self.btnSubmit_button.grid(row=2, column=0, sticky=W)
		
		self.text = Text(self, width=35, height=5, wrap=WORD) #WORD, CHAR, NONE
		self.text.grid(row=3, column=0, columnspan=2, sticky=W)
		
	''' define the button event '''
	def reveal(self):
		''' display message based on the password pass in'''
		content = self.txtPassword.get()
		
		if content == "password":
			message = "You have access to something"
		else:
			message = "Access denied!"
		
		self.text.delete(0.0, END)		#clear before entering a new message
		self.text.insert(0.0, message) 	#0.0 is row=0, column=0
		
		
root = Tk()
root.title("Password")
root.geometry("250x150")
app = Application(root)
root.mainloop()


	
		