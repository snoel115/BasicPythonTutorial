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
		#''' create label '''
		#self.label = Label(self, text="This is a label!")
		#self.label.grid()				#put the label on the grid`

		'''Create 3 buttons that do nothing'''
		self.button1 = Button(self, text="This is my fist button!")
		self.button1.grid()

		self.button2 = Button(self)
		self.button2.grid()
		self.button2.configure(text = "this is a new text") #how to set the text in a button once created

		self.button3 = Button(self)
		self.button3.grid()
		self.button3["text"] = "text through dictionary" #how to set the text in a button once created

		
#create the window
root = Tk()

root.title("Lazy button")		#modify the root window label
root.geometry("200x100")		#set the size of the window

app = Application(root) 		#create the frame to hold other element in the window

#kick off the event loop to keep the window open and to get it ready to trigger events
root.mainloop()
