#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os


class FileStorage:

    """Class for serialization and deserialization of base classes."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: values.to_dict()
                    for key, values in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {key: self.classes()[values["__class__"]](**values)
                        for key, values in obj_dict.items()}
            FileStorage.__objects = obj_dict
