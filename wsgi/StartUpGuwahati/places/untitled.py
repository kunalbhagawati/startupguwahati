from django.db import connections
from places import models

uniqueLocs = set()
for loc in models.Locality.objects.all():
    try:
        l = models.Locality.objects.get(locality_name=loc.locality_name, city=loc.city.pk)
        uniqueLocs.add(l)
    except Exception as e:
        # print("{0} for id: {1}; locality_name: {2}; city: {3}".format(e, loc.pk, loc.locality_name, loc.city.pk))
        pass

cur = connections['iplisting'].cursor()
for loc in uniqueLocs:
    try:
        sql = "SELECT LocalityId from iplisting.iplocalityhash where LocalityName='{0}' and CityId={1}".format(loc.locality_name, loc.city.pk)
        cur.execute(sql)
        for i in cur:
            prevLocId = i[0]

        sql2 = "SELECT Latitude, Longitude from iplisting.iplocalityinfo where LocalityId={0}".format(prevLocId)
        cur.execute(sql2)
        for i in cur:
            loc.latitude = i[0]
            loc.longitude = i[1]
        loc.save()
    except ProgrammingError as e:
        print(e)
