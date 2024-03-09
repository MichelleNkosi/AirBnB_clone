#!/usr/bin/python3
from models.base_model import BaseModel
from models.__init__ import storage

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 100
my_model.id = 123
my_model.save()

my_model2 = BaseModel()
my_model2.name = "My Second Model"
my_model2.my_number = 200
my_model2.id = 911
my_model.save()

all_models = storage.all()
print(all_models)