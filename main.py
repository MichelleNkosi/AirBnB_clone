#!/usr/bin/python3
from models.base_model import BaseModel
from models.__init__ import storage

remake = list()
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
    print(value)
    remake.append(value)

print("REMAKING OBJ")
for values in remake:
    my_old_model = BaseModel(**values)
    print(my_old_model)

