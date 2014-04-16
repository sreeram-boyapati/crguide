from django.db import models

class Location(models.Model):
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    building = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __unicode__(self):
        return str(self.building)+"|"+str(self.city)


class Office(models.Model):
    title = models.CharField(max_length=250)
    location = models.ForeignKey(Location)
    type_office_choices = (('CV', 'Civilian'), ('MI', 'Military'), ('CV and MI', 'Civilian and Military'))
    type_office = models.CharField(max_length=50, choices = type_office_choices)

    def __unicode__(self):
        return str(self.title) + "|" + str(self.type_office)
