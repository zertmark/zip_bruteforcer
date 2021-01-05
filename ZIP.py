import zipfile
from MessageBox import MessageBox

class ZIPCracker(zipfile.ZipFile):
    
    def __init__(self,path: str, wordlist :str, progressbar: object):
        super().__init__(path)
        self.wordlist=wordlist
        self.password=""
        self.ProgressBar=progressbar
        self.counter=0

    def TryBruteForce(self):
        with open(self.wordlist,'r',errors='ignore',encoding='utf-8') as file:
            for word in file.readlines():
                if(self.isPasswordCorrect(word.strip())):
                    self.password=word.strip()
                    MessageBox.ShowInfo("Done",f"Password found! {self.password}")
                    return

                self.counter+=1
               	self.ProgressBar.updateValue(self.counter)
               							
    def isCracked(self) -> bool:
    	if self.password != "":
    		return True
    	else:
    		return False

    def countPasswords(self) -> int:
        output=0
        with open(self.wordlist,'r',errors='ignore',encoding='utf-8') as file:
            for word in file.readlines():
            	output+=1

        return output

    def isPasswordCorrect(self,password: str) -> bool:
        try:
            self.extractall(pwd=password.encode('utf-8'))
            return True
        except RuntimeError:
            return False
        else:
            raise Exception