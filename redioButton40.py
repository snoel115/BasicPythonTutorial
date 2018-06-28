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
		Label(self, text = "Selecting one:").grid(row=0, column=0, sticky=W)
		
		
		self.favorite = StringVar()
		
		#Commity radio button
		Radiobutton(self, text="Comedy", variable = self.favorite, 
					value = "comedy.",
					command = self.update_text).grid(row=2, column=0, sticky=W)
		
		#drama radio button
		Radiobutton(self, text="Drama", variable = self.favorite, 
					value = "drama.",
					command = self.update_text).grid(row=3, column=0, sticky=W)
	
		#romance radio button
		Radiobutton(self, text="Romance", variable = self.favorite,
					value = "romance.",
					command = self.update_text).grid(row=4, column=0, sticky=W)
	
		self.result = Text(self, width=40, height=5, wrap = WORD)
		self.result.grid(row=5, column=0, columnspan = 3)
		
	def update_text(self):
		#update text widget and diaplay favorite movie
		message = "Your favorite type of movie is "
		message += self.favorite.get()

		self.result.delete (0.0, END)
		self.result.insert (0.0, message)
		
root = Tk()
root.title("Movie chooser")
root.geometry("400x200")
app = Application(root)
root.mainloop()
