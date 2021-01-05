#Uncomment this only if you have Linux :/

#import rarfile
#import platform
#class RARCracker(rarfile.RarFile):
	#def __init__(self,path: str, wordlist: str,progressbar: object):
	#	super().__init__(path)
	#	self.wordlist=wordlist
	#	self.countPasswords()
	#	self.password=""
	#	self.ProgressBar=progressbar
	#	self.counter=0

	#def TryBruteForce(self) -> bool:
	#	with open(self.wordlist,'r',errors='ignore',encoding='utf-8') as file:
	#		for word in file.readlines():
	#			if(self.isPasswordCorrect(word.strip())):
	#				self.password=word.strip()
	#				return True
	#			self.counter+=1
	#			self.ProgressBar.update(self.counter)
	#	return False

	#def countPasswords(self) -> int:
    #    output=0
    #    with open(self.wordlist,'r',errors='ignore',encoding='utf-8') as file:
    #        for word in file.readlines():
	#			output+=1
	#	return output
		
	#def RequiresPassword(self) -> bool:
	#	return self.needs_password()

	#def isLinux(self) -> bool:
	#	if "linux" in platform.system().lower():
	#		return True
	#	else:
	#		return False
	#def isPasswordCorrect(self,password: str) -> bool:
	#	try:
	#		self.testrar(pwd=password)
	#		return True
	#	except RuntimeError:
	#		return False
	#	else:
	#		raise Exception
    

