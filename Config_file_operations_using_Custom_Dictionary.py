"""
 We are in need of a configuration file which happens to have data in the form of key vaue pairs inside it , 
 like 'Email' = 'hkbiet@gmail.com'.
 We've got to be able to write keys and respective values in the config file and also be able to retrieve 
 the values of key asked for .

 Hence , The best way to go around is to create a custom dictionary , which writes key value pairs to the 
 configuration file and retrieves data as va- -lue for key asked for

 (C) HEMANT KUMAR 
                                                        PROJECT REPO : github.com/hkbiet


"""

import os
import sys

class CustomException(Exception):

	def __init__(self, dict_instance, key):
		self.key = key
		self.keys = dict_instance.keys()

	def __str__(self):
		return "\n\t '{0}' is NOT a valid key in the file ! please choose one of the below keys \n\t {1}".format(self.key,", ".join(self.keys))
		
		

class CustomDict(dict):

	def __init__(self):
		self.filename = input("Type the name or path to the Config file : ")
		if not os.path.isfile(self.filename):
			try:
				fh = open(self.filename,"w").close()
			except IOError:
				raise IOError(" Please provide a valid path/to/filename ")
		with open(self.filename,"r") as fh :
			for line in fh:
				line = line.rstrip()
				key, value = line.split("=", 1)
				super(CustomDict,self).__setitem__(key, value)


	def __getitem__(self, key):
		if not key in self.keys():
			raise CustomException(self, key)
		return dict.__getitem__(self,key)




	def __setitem__(self, key, value):
		dict.__setitem__(self, key, value)
		with open(self.filename,"a") as fh:
			fh.write(str(key)+"="+str(value)+"\n")



if __name__ == "__main__":
	
	print(""" \n\n\n\tPlease run this on Python interpretor as shown below

			>>> from Dict import CustomDict
			>>> file = CustomDict()
			
			# It will ask for the filename
			>>> Type the name of the file : <filename>

			# Then you can use the 'file' object as a dict to read and write data from and to the file named by you as above.
			>>> file
			>>> {} #Empty Dictionary assuming there  was nothing in the file

			>>> file["Email"] = "hkbiet@gmail.com"
			>>> file
			>>> {"Email":"hkbiet@gmail.com"}

			# and so on , Thanks !
			


""")
