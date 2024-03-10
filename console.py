#!/usr/bin/python3
""" Is this necessary?"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
	""" CLASS"""
	prompt = "(hbnb) "
	
	def do_EOF(self, line):
		""" EOF RETURNS TRUE ,THEN A NEW LINE
		"""
		print()
		return (True)
		
	def emptyline(self):
		""" THIS IS AN EMPTY LINE
		"""
		pass

	def do_create(self, line):
		""" TO CREATE NEW INSTANCES
		USAGE: <create> <class>
		"""
		if line == "":
			print("** class name missing **")
			return
		var = line.split()
		cl_name = var[0]
		if cl_name not in  FileStorage.definedclass:
			print("** class doesn't exist **")
			return
		else:
			instance_1 = FileStorage.definedclass[line]() #instance_1 = BaseModel
			instance_1.save()
			print(instance_1.id)

	def do_show(self, line):
		""" THIS SHOWS THE ATTRIBUTE OF AN OBJECT BASED ON ITS CLASS AND ID
		USAGE: <show> <class> <id> 
		"""
		var = line.split() # VAR IS A LIST
		if not var:
			print("** class name missing **")
			return
		if  var[0] not in  FileStorage.definedclass:
			print("** class doesn't exist **")
			return
		if len(var) < 2:
			print("** instance id missing **")
			return
		instance_id = var[1]
		key = "{}.{}".format(var[0], instance_id)
		if key not in storage.all():
			print("** no instance found **")
			return
		print(storage.all()[key])
	
	def do_destroy(self, line):
		""" THIS DESTROYS A SPECIFIED INSTANCE BASED ON CLASS AND ID.
		USAGE: <destroy> <class> <id>
		"""
		var = line.split() # VAR IS A LIST
		if not var:
			print("** class name missing **")
			return
		if  var[0] not in  FileStorage.definedclass:
			print("** class doesn't exist **")
			return
		if len(var) < 2:
			print("** instance id missing **")
			return
		instance_id = var[1]
		key = "{}.{}".format(var[0], instance_id)
		if key not in storage.all():
			print("** no instance found **")
			return
		del storage.all()[key]
		storage.save()
	
	def do_all(self, line):
		""" TO DISPLAY ALL [SPECIFIED] OBJECTS.
		USAGE: <all> [class]
		"""
		var = line.split()
		if line == "":
#			print(storage.all())
#			print()
#			for key in storage.all():
#				print(key)
#			print()
			print([str(value) for value in storage.all().values()])	
			return
		if  var[0] not in  FileStorage.definedclass:
			print("** class doesn't exist **")
		else:
			list1 = list()
			for value in storage.all().values():
				if value.__class__.__name__ == var[0]:
					list1.append(str(value))
			print(list1)
	

	def do_update(self, line):
		""" USAGE: update <class name> <id> <attribute name> "<attribute value>"
		"""
		var = line.split() # VAR IS A LIST
		if not var:
			print("** class name missing **")
			return
		if  var[0] not in  FileStorage.definedclass:
			print("** class doesn't exist **")
			return
		if len(var) < 2:
			print("** instance id missing **")
			return
		instance_id = var[1]                                        
		key = "{}.{}".format(var[0], instance_id)                  
		if key not in storage.all():                                       
			print("** no instance found **")                            
			return
		if len(var) < 3:
			print("** attribute name missing **")
			return
		if len(var) < 4:
			print("** value missing **")
			return	
		attr_value = None
		try:
			attr_value = eval(var[3])
			setattr(storage.all()[key], var[2], attr_value)
		except Exception as t:
			print("** value missing **")
		storage.save()
		return

			
	def do_quit(self, line):
		""" TO QUIT THE PROGRAM SUCCESSFULLY WITH THE STATUS CODE
		"""
		sys.exit(0) #status code - 0

if __name__ == '__main__':
    HBNBCommand().cmdloop()
