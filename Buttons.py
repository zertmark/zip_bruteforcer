#I know that this is kinda useless, but I like my own names for methods
import tkinter

class Button(tkinter.Button):
    
    def __init__(self, window: object):
        super().__init__(window)

    def setText(self, texts: str):
        self.config(text=texts)
    
    def setWidth(self,width: int):
        self.config(width=width)
    
    def setHeight(self,height: int):
        self.config(height=height)
    
    def setCommand(self,funciton_name):
        self.config(command=funciton_name)
    
    def setBackgroundColor(self,color: str):
        self.config(bg=color)
    
    def setForegroundColor(self,color: str):
        self.config(fg=color)
    
    def setGrid(self,rows: int, columns: int):
        self.grid(row=rows,column=columns)
