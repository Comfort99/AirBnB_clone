#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place
#all_objs = storage.all()
#print("-- Reloaded objects --")
#for obj_id in all_objs.keys():
#    obj = all_objs[obj_id]
#    print(obj)

print("-- Create a new Place --")
my_place = Place()
my_place.city_id = "109678"
my_place.user_id = "90789-8756-7764213"
my_place.name = "Comfort_City"
my_place.number_rooms = "653790"
my_place.save()
print(my_place)
