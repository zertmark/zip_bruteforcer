import os
import tkinter
from tkinter import messagebox
from tkinter import filedialog

class File():
    def __init__(self):
        self.zip_path=""
        self.wordlist_path=""

    def setArchiveFile(self):
        path=filedialog.askopenfilename(title="Select archive file",filetypes = (("ZIP","*.zip"),("All files","*.*"),("RAR","*.rar"))).strip()
        if os.path.exists(path):
            print("ZIP path is{}".format(path))
            self.zip_path=path
        else:
            messagebox.showerror("Error in the Archive's path","Invalid selected path to the archive file")

    def setDicFile(self):
        path=filedialog.askopenfilename(title="Select wordlist",filetypes = (("All files","*.*"),("Wordlist (txt)","*.txt"),("Wordlist (dic)","*.dic"))).strip()
        if os.path.exists(path):
            print("Dictionary path is{}".format(path))
            self.wordlist_path=path

        else:
            messagebox.showerror("Error in the Dictionary's path","Invalid selected path to the dictionary file")

    def isArchiveRAR(self) -> bool:
        if '.rar' in self.zip_path:
            print("This is a RAR archive")
            return True
        else:
            print("This isn't a RAR archive")
            return False

    def isDictionaryEmpty(self) -> bool:
        if self.wordlist_path != "":
            if os.path.getsize(self.wordlist_path) == 0:
                print("Wordlist file is empty")
                return True
            else:
                print("Wordlist file isn't empty")
                return False
        else:
            print("Wordlist path string is empty")
            return True

    def isArchiveEmpty(self) -> bool:
        if self.zip_path != "":
            if os.path.getsize(self.zip_path) == 0:
                print("RAR file is empty")
                return True
            else:
                print("RAR file isn't empty")
                return False
        else:
            print("RAR file string is empty")
            return True

    def getArchiveFilePath(self) -> str:
        return self.zip_path

    def getDictionaryPath(self) -> str:
        return self.wordlist_path

