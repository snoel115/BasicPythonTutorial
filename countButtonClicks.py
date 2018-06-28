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
		self.button_clicks = 0 #class variable to keep the count of clicks
		self.create_widgets()
		
	def create_widgets(self):
		'''Create a button displaying the number of click'''
		self.button = Button(self, text="Total of clicks: 0")
		self.button["command"] = self.update_count	#create the event to receive the button click
		self.button.grid()
		
	''' create the even to receive the click action '''
	def update_count(self):
		''' increase the click count and display the new total '''
		self.button_clicks += 1		# add one to the class variable
		self.button["text"] = "Total of click: " + str(self.button_clicks) # modify the label in the button

		
#create the window
root = Tk()

root.title("Lazy button")		#modify the root window label
root.geometry("200x100")		#set the size of the window

app = Application(root) 		#create the frame to hold other element in the window

#kick off the event loop to keep the window open and to get it ready to trigger events
root.mainloop()
