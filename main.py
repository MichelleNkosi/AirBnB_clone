#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.__init__ import storage

remake = list()
classes = list()
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 100
my_model.brain = "123"
my_model.save()
print("THE MODEL")
print(my_model)
print("THE MODEL DICT")
print(my_model.to_dict())
print("THE MODEL JSON RETURNED")
storage.reload()
all_models = dict(storage.all())
for key, value in all_models.items():
    remake.append(value)
    classes.append(key)
print(all_models)

print("REMAKING OBJ")
for num in range(len(classes)):
    values, cls = remake[num], classes[num]
    class_name, obj_id = cls.split(".")
    class_obj = globals().get(class_name)
    my_old_model = class_obj(**values)
    print(my_old_model)

