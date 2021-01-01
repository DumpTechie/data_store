import json
from bson import json_util
import datetime
import os
import sys
import os.path
from os import path

class data_store_exception(Exception):
	def __init__(self, msg):
		self.msg=msg
	def print_exception(self):
		print("ERROR_IN_DATASTORE: ",self.msg)
		
class data_store():	

	def __init__(self, file_path="",name="deault"):

		if(not path.exists(file_path) and file_path!=""):
			raise data_store_exception("File path does not exists")
		self.path =file_path+name+".json"
		if(path.exists(self.path)):
			raise data_store_exception("file already exists")
		person_dict = {}
		with open(self.path, 'w') as json_file:
		    json.dump(person_dict, json_file)
		    json_file.close()

	def insert_key_value(self,key,value):
		person_dict={}
		with open(self.path,'r+') as json_file:
  			person_dict= json.load(json_file)
  			if(key in person_dict.keys()):
  				raise data_store_exception("key already present")
  			if(len(key)>16):
  				raise data_store_exception("length of key exceeds limit")
  			if(sys.getsizeof(value)>16000):
  				raise data_store_exception("JSON object is exceeding limit")
  			person_dict[key]=value
  			json_file.close()
  			with open(self.path, 'w') as json_file:
	  			json.dump(person_dict, json_file)
	  			json_file.close()
	  			if(os.stat(self.path).st_size>1073741824):
	  				self.Delete_key_value(key)
	  				raise data_store_exception("Size of file exceeds 1GB")

	def Read_key(self,key):
		with open(self.path,'r+') as json_file:
			person_dict= json.load(json_file)
			json_file.close()
			if(key not in person_dict.keys()):
				raise data_store_exception("Key not present")
			return(person_dict[key])

	def Delete_key_value(self,key):
		person_dict={}
		with open(self.path,'r+') as json_file:
  			person_dict= json.load(json_file)
  			print(person_dict)
  			print("jiiji")
  			person_dict.pop(key)
  			print(person_dict)
  			json_file.close()
  			with open(self.path, 'w') as json_file:
	  			json.dump(person_dict, json_file)
	  			json_file.close()	
	def delete_file(self):
		os.remove(self.path)
	

#raise data_store_exception("memoryerro")				
d=data_store()
dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}
print(sys.getsizeof(dict))
d.insert_key_value("now",dict)
print(d.Read_key("now"))
d.delete_file()
#d.Delete_key_value("now")
		
e=datetime.datetime.now()
ee=datetime.datetime.now()
print(path.exists("deault.json"))

print(e)