# AirBnB clone

## The console

### Description

**This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: User, Amenity, City, State, Place, Review), and a storage engine. The command interpreter, is like Shell, but limited to a specific use-case. It takes in user input, and manipulates the object instances**:

* ***Create a new object (ex: a new User or a new Place)***
* ***Retrieve an object from a file***
* ***Do operations on objects (count, compute stats, etc…)***
* ***Update attributes of an object***
* ***Destroy an object***

**This first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored. This abstraction will also allow you to change the type of storage easily without updating all of your codebase. The console will be a tool to validate this storage engine**


# Usage
Your shell should work like this in `interactive mode`:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in `non-interactive mode`: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
