from django.db import models
import mongoengine

class Location(mongoengine.Document):
    latitude = mongoengine.FloatField()
    longitude = mongoengine.FloatField()
    building = mongoengine.StringField(max_length=250)
    city = mongoengine.StringField(max_length=250)
    address = mongoengine.StringField(max_length=250)

    def __unicode__(self):
        return str(Building)+"|"+str(city)


class Office(mongoengine.Document):
    title = mongoengine.StringField(max_length=250)
    location = mongoengine.ReferenceField(Location)
    type_office_choices = (('CV', 'Civilian'), ('MI', 'Military'), ('CV and MI', 'Civilian and Military'))
    type_office = mongoengine.StringField(choices = type_office_choices)

    def __unicode__(self):
        return str(title) + "|" + str(type_office)
# Create your models here.
