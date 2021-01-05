from tkinter.ttk import Progressbar

class GreenProgressBar(Progressbar):

    def __init__(self, window: object, length: int, style: str):
        super().__init__(window,length=length,style=style)
        self.updateValue(0)

    def updateValue(self,new_value: int):
        if new_value >=0:
            self['value']=new_value

    def setMaxValue(self, max_value: int):
        self.configure(maximum=max_value)