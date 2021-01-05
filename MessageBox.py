#I know that this is kinda useless, but I like my own names for methods
from tkinter.messagebox import showerror, showinfo

class MessageBox:
	
	@staticmethod
	def ShowError(title: str,text: str):
		showerror(title,text)

	@staticmethod
	def ShowInfo(title: str,text: str):
		showinfo(title,text)

