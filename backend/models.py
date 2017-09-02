from django.db import models
from location_field.models.plain import PlainLocationField


class Area(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

    def __str__(self):
        return self.name
    
    def to_json(self):
        return dict(
            id=self.id,
            name=self.name,
            parent_id=self.parent_id,
        )


class Church(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, blank=False)
    area = models.ForeignKey('Area', blank=False, null=False, related_name='churches')
    location = PlainLocationField(based_fields=['address'], zoom=7)
    website = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '{} [ {} ]'.format(self.name, self.address)

    def to_json(self):
        ll = self.location.split(',')
        return dict(
            id=self.id,
            name=self.name,
            area=self.area_id,
            address=self.address,
            location=dict(
                lat=float(ll[0]),
                long=float(ll[1])
            ),
            website=self.website,
            masses=[m.to_json() for m in self.masses.all()],
        )


class MassTime(models.Model):
    church = models.ForeignKey('Church', blank=False, null=False, related_name='masses')
    day_of_week = models.SmallIntegerField()
    time = models.TimeField()

    def __str__(self):
        return '{} [ {} ]'.format(self.church.name, self.time)
    
    def to_json(self):
        return dict(
            day_of_week=self.day_of_week,
            time=self.time.strftime('%H:%M')
        )