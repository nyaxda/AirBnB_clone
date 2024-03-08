# 0x00. AirBnB clone - The console
![AirBnB clone Website](https://media.licdn.com/dms/image/D4D12AQFaPRt92UdRoQ/article-cover_image-shrink_600_2000/0/1699544842196?e=1715212800&v=beta&t=iYmZMoBzc6oiz0Mkwq52c1PajXtHOoIktuZFetC4bps)
This is one of the alx projects aimed at deploying on my server a simple copy of the [AirBnB website](https://www.airbnb.com/)
At this stage, the task to be accomplished is to create a command interpreter to manipulate data without a visual interface, like in a Shell.
## Command Interperter
### CmdModule

-   cmd makes it easy to embed a command line within the program
-   Creating a command line interpreter is done by sub-classing the `cmd.Cmd` class

Sample:

```
import cmd


class MyCmd(cmd.Cmd)
	prompt = '> ' # Prompt displated to the user

	def do_add(self,s):
		l = s.split()
		if len(l) != 2
			print "*** invalid number of arguments"
		return
		try:
			l = [int(i) for i in l]
		except ValueError:
			print "*** arguments should be numbers"
		return
		print l[0] + l[1]


if __name__ == '__main__':
	MyCmd().cmdloop()
```
  

if we run the interpreter we will have:

```
(Cmd) add 4
*** invalid number of arguments
(Cmd) add 5 4
9
```
  

Starting the interpeter:

-   Once you have defined you own interpreter class, create an instance and call the mainloop method:
    
```
interpreter = MyCmdInterpreter()
interpreter.cmdloop()
  ```

Modal interaction:

-   Cmd class allows you to use the `print` and `raw input` functions:
    
```
def do_hello(self, s):
	if s=='':
		s = raw_input('Your name please: ')
	print 'Hello',s
```
Generally, this is how we use the custom-line Interpreter:

1.  Define a Sublass of `cmd.Cmd`
	The subclass is meant to create the custom command-line interpreter. In this context, define command methods with names starting with `do_` to handle user commands. The methods can also be defined by names starting with `help_` to provide help messages for commands.
2. Instantiate your SubClass
3.  Start the Command Loop
The `cmdloop()` method starts the command loop, continuously prompting the user for input and executes commands until the user exits.

If I want to relay inputs from the command-line interpreter to other functions or methods, we call the functions or methods within the command methods (`do_` methods)

For instance:
```
class MyCmd(cmd.Cmd):

prompt = '> '

def do_process_input(self, arg):

	"""Process the input"""

	result = process_input(arg)

	print("Result:", result)

def process_input(input):
# Process the input here:

return input.upper()
```
## Learning Objectives


At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.alxswe.com/rltoken/uV5eZkRZ_XEqYbgPd-0CWw "explain to anyone"),  **without the help of Google**:

### General

-   How to create a Python package
-   How to create a command interpreter in Python using the  `cmd`  module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage  `datetime`
-   What is an  `UUID`
-   What is  `*args`  and how to use it
-   What is  `**kwargs`  and how to use it
-   How to handle named arguments in a function

## Command Inte

## Tasks

### **0. README, AUTHORS**

- A README.md:
	-   description of the project
	-   description of the command interpreter:
	    -   how to start it
	    -   how to use it
	    -   examples
- `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the
Requirements:

-   `localhost`  resolves to  `127.0.0.2`
-   `facebook.com`  resolves to  `8.8.8.8`.

### **1. Be pycodestyle compliant!**
A beautiful code that passes the pycodestyle checks.

### **2. Unittests**
Unit tests that test files, classes, functions

### [**3. BaseModel**](https://github.com/nyaxda/AirBnB_clone/blob/main/models/base_model.py)
a class  `BaseModel`  that defines all common attributes/methods for other classes:

-   `models/base_model.py`
-   Public instance attributes:
    -   `id`: string - assign with an  `uuid`  when an instance is created:
        -   you can use  `uuid.uuid4()`  to generate unique  `id`  but don’t forget to convert to a string
        -   the goal is to have unique  `id`  for each  `BaseModel`
    -   `created_at`: datetime - assign with the current datetime when an instance is created
    -   `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
-   `__str__`: should print:  `[<class name>] (<self.id>) <self.__dict__>`
-   Public instance methods:
    -   `save(self)`: updates the public instance attribute  `updated_at`  with the current datetime
    -   `to_dict(self)`: returns a dictionary containing all keys/values of  `__dict__`  of the instance:
        -   by using  `self.__dict__`, only instance attributes set will be returned
        -   a key  `__class__`  must be added to this dictionary with the class name of the object
        -   `created_at`  and  `updated_at`  must be converted to string object in ISO format:
            -   format:  `%Y-%m-%dT%H:%M:%S.%f`  (ex:  `2017-06-14T22:31:03.285259`)
            -   uses `isoformat()`  of  `datetime`  object
        -   This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our  `BaseModel`
### [**4. Create BaseModel from dictionary**](https://github.com/nyaxda/AirBnB_clone/blob/main/models/base_model.py)
Updated  `models/base_model.py`:

-   `__init__(self, *args, **kwargs)`:
    -  uses  `*args, **kwargs`  arguments for the constructor of a  `BaseModel`. 
    -   `*args`  won’t be used
    -   if  `kwargs`  is not empty:
        -   each key of this dictionary is an attribute name
        -   each value of this dictionary is the value of this attribute name

    -   otherwise:
        -   create  `id`  and  `created_at`  
### [**5. Store first object**](https://github.com/nyaxda/AirBnB_clone/blob/main/models/engine/file_storage.py)
A class  `FileStorage`  that serializes instances to a JSON file and deserializes JSON file to instances:

-   `models/engine/file_storage.py`
-   Private class attributes:
    -   `__file_path`: string - path to the JSON file (ex:  `file.json`)
    -   `__objects`: dictionary - empty but will store all objects by  `<class name>.id`  (ex: to store a  `BaseModel`  object with  `id=12121212`, the key will be  `BaseModel.12121212`)
-   Public instance methods:
    -   `all(self)`: returns the dictionary  `__objects`
    -   `new(self, obj)`: sets in  `__objects`  the  `obj`  with key  `<obj class name>.id`
    -   `save(self)`: serializes  `__objects`  to the JSON file (path:  `__file_path`)
    -   `reload(self)`: deserializes the JSON file to  `__objects`  (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Updated  `models/__init__.py`: to create a unique  `FileStorage`  instance for your application

-   import  `file_storage.py`
-   create the variable  `storage`, an instance of  `FileStorage`
-   call  `reload()`  method on this variable

Updated  `models/base_model.py`: to link your  `BaseModel`  to  `FileStorage`  by using the variable  `storage`

-   import the variable  `storage`
-   in the method  `save(self)`:
    -   call  `save(self)`  method of  `storage`
-   `__init__(self, *args, **kwargs)`:
    -   if it’s a new instance (not from a dictionary representation), add a call to the method  `new(self)`  on  `storage`
 
### [**6. Console 0.0.1**](https://github.com/nyaxda/AirBnB_clone/blob/main/console.py)
A program called  `console.py`  that contains the entry point of the command interpreter:

-   Uses the module  `cmd`
-   Your class definition is:  `class HBNBCommand(cmd.Cmd):`
-   Your command interpreter implements:
    -   `quit`  and  `EOF`  to exit the program
    -   `help` 
    -   a custom prompt:  `(hbnb)`
    -   an empty line +  `ENTER`  shouldn’t execute anything
-  The code cannot be executed when imported.

### [**7. Console 0.1**](https://github.com/nyaxda/AirBnB_clone/blob/main/console.py)
Updated  command interpreter (`console.py`) that has these commands:

-   `create`: Creates a new instance of  `BaseModel`, saves it (to the JSON file) and prints the  `id`. Ex:  `$ create BaseModel`
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ create`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ create MyModel`)
-   `show`: Prints the string representation of an instance based on the class name and  `id`. Ex:  `$ show BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ show`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ show MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ show BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ show BaseModel 121212`)
-   `destroy`: Deletes an instance based on the class name and  `id`  (save the change into the JSON file). Ex:  `$ destroy BaseModel 1234-1234-1234`.
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ destroy`)
    -   If the class name doesn’t exist, print  `** class doesn't exist ** (ex:`$ destroy MyModel`)`
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ destroy BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ destroy BaseModel 121212`)
-   `all`: Prints all string representation of all instances based or not on the class name. Ex:  `$ all BaseModel`  or  `$ all`.
    -   The printed result must be a list of strings (like the example below)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ all MyModel`)
-   `update`: Updates an instance based on the class name and  `id`  by adding or updating attribute (save the change into the JSON file). Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage:  `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at the time
    -   You can assume the attribute name is valid (exists for this model)
    -   The attribute value must be casted to the attribute type
    -   If the class name is missing, print  `** class name missing **`  (ex:  `$ update`)
    -   If the class name doesn’t exist, print  `** class doesn't exist **`  (ex:  `$ update MyModel`)
    -   If the  `id`  is missing, print  `** instance id missing **`  (ex:  `$ update BaseModel`)
    -   If the instance of the class name doesn’t exist for the  `id`, print  `** no instance found **`  (ex:  `$ update BaseModel 121212`)
    -   If the attribute name is missing, print  `** attribute name missing **`  (ex:  `$ update BaseModel existing-id`)
    -   If the value for the attribute name doesn’t exist, print  `** value missing **`  (ex:  `$ update BaseModel existing-id first_name`)
    -   All other arguments should not be used (Ex:  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"`  =  `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    -   `id`,  `created_at`  and  `updated_at`  cant’ be updated. You can assume they won’t be passed in the  `update`  command
    -   Only “simple” arguments can be updated: string, integer and float. Assumption is, nobody will try to update list of ids or datetime.

Added rules:
-   Arguments are always in the right order
-   Each arguments are separated by a space
-   A string argument with a space must be between double quote
-   The error management starts from the first argument to the last one

### [**8. First User**](https://github.com/nyaxda/AirBnB_clone/blob/main/models/user.py)
A class  `User`  that inherits from  `BaseModel`:

-   `models/user.py`
-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string

Updates  `FileStorage`  to manage correctly serialization and deserialization of  `User`.

Updates the command interpreter (`console.py`) to allow  `show`,  `create`,  `destroy`,  `update`  and  `all`  used with  `User`.

### **9. More classes!**
Classes that inherit from  `BaseModel`:

-   [`State`](https://github.com/nyaxda/AirBnB_clone/blob/main/models/state.py)  (`models/state.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   [`City`](https://github.com/nyaxda/AirBnB_clone/blob/main/models/city.py)  (`models/city.py`):
    -   Public class attributes:
        -   `state_id`: string - empty string: it will be the  `State.id`
        -   `name`: string - empty string
-   [`Amenity`](https://github.com/nyaxda/AirBnB_clone/blob/main/models/amenity.py)  (`models/amenity.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   [`Place`](https://github.com/nyaxda/AirBnB_clone/blob/main/models/place.py)  (`models/place.py`):
    -   Public class attributes:
        -   `city_id`: string - empty string: it will be the  `City.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `name`: string - empty string
        -   `description`: string - empty string
        -   `number_rooms`: integer - 0
        -   `number_bathrooms`: integer - 0
        -   `max_guest`: integer - 0
        -   `price_by_night`: integer - 0
        -   `latitude`: float - 0.0
        -   `longitude`: float - 0.0
        -   `amenity_ids`: list of string - empty list: it will be the list of  `Amenity.id`  later
-   [`Review`](https://github.com/nyaxda/AirBnB_clone/blob/main/models/review.py)  (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the  `Place.id`
        -   `user_id`: string - empty string: it will be the  `User.id`
        -   `text`: string - empty string
