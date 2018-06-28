#Simple GUI
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

class Application(Frame):
	def __init__(self, master):
		#Initialize the frame
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		#create widgets for movie type choice
		Label(self, text = "Choose your favorite type").grid(row=0, column=0, sticky=W)
		
		#instructions
		Label(self, text = "Selct all that apply:").grid(row=0, column=0, sticky=W)
		
		#Commity check button
		self.comedy = BooleanVar()
		Checkbutton(self, text="Comedy", variable = self.comedy, command = self.update_text).grid(row=2, column=0, sticky=W)
		
		#drama check button
		self.drama = BooleanVar()
		Checkbutton(self, text="Drama", variable = self.drama, command = self.update_text).grid(row=3, column=0, sticky=W)
	
		#romance check button
		self.romance = BooleanVar()
		Checkbutton(self, text="Romance", variable = self.romance, command = self.update_text).grid(row=4, column=0, sticky=W)
	
		self.result = Text(self, width=40, height=5, wrap = WORD)
		self.result.grid(row=5, column=0, columnspan = 3)

	def update_text(self):
		#update text widget and diaplay favorite movie
		likes = ""

		if self.comedy.get():
			likes  += "You like comedy" + '\r\n' 
		if self.drama.get():
			likes += "You like drama"  + '\r\n'
		if self.romance.get():
			likes += "You like romance"
			
		self.result.delete (0.0, END)
		self.result.insert (0.0, likes)
	
		
root = Tk()
root.title("Movie chooser")
root.geometry("250x150")
app = Application(root)
root.mainloop()
