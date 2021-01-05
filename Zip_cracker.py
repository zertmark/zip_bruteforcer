import tkinter
import threading
from File import File 
from ZIP import ZIPCracker
#from RAR import RARCracker
from MessageBox import MessageBox
from ProgressBar import GreenProgressBar
from Buttons import Button

WIDTH=500
HEIGHT=500

class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WIDTH}x{HEIGHT}')
        self.config(bg='black')
        self.title("ZIP_CRAKER 2.0")
        self.resizable(False,False)
        self.thread=None

    def createButtons(self):
        self.button_list=[]
        for i in range(0,3):
            self.button_list.append(Button(self))
            self.button_list[i].setWidth(25)
            self.button_list[i].setHeight(2)
            self.button_list[i].setBackgroundColor('black')
            self.button_list[i].setForegroundColor('white')
            self.button_list[i].place(x=160,y=100+(i*50))

    def setTextToButtons(self):
        self.button_list[0].setText("Select zip file")
        self.button_list[1].setText("Select wordlist file")
        self.button_list[2].setText("Crack!")

    def setCommandsToButtons(self):
        self.FileChecker=File()
        self.button_list[0].setCommand(self.FileChecker.setArchiveFile)
        self.button_list[1].setCommand(self.FileChecker.setDicFile)
        self.button_list[2].setCommand(self.startCrack)

    def startCrack(self):

        if not self.FileChecker.isArchiveEmpty() and not self.FileChecker.isDictionaryEmpty():
            
            if self.FileChecker.isArchiveRAR():

                MessageBox.ShowError("Error","This is a RAR file(If you want to use this just uncomment code in Zip_Cracker.py file)")
                #Uncomment this if you have linux :/
                #if not self.FileChecker.RequiresPassword():
                #    Cracker=RARCracker(self.FileChecker.getArchiveFilePath(),self.FileChecker.getDictionaryPath())
                #else:
                #    messagebox.showinfo("WAIT WHAT?","RAR archive doesn't have any password")
                #    return 
            else:
                
                Cracker=ZIPCracker(self.FileChecker.getArchiveFilePath(),self.FileChecker.getDictionaryPath(),self.ProgressBar)
                self.ProgressBar.setMaxValue(Cracker.countPasswords())
                # I'm fucking lazy to create a special class for two lines of code  :/
                self.thread=threading.Thread(target=Cracker.TryBruteForce())
                self.thread.start()
        else:
            MessageBox.ShowError("Error","You didn't choose all options")

    def createProgressBar(self):
        self.ProgressBar=GreenProgressBar(self,200,'green.Horizontal.TProgressbar')
        self.ProgressBar.place(x=160,y=400)

    def startWindow(self):
        self.mainloop()



if __name__ == "__main__":
    window=MainWindow()
    window.createButtons()
    window.setTextToButtons()
    window.setCommandsToButtons()
    window.createProgressBar()
    window.startWindow()