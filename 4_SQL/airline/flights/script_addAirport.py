from flights.models import *


jfk = Airport(code="JFK", city="New York")
lhr = Airport(code="LHR", city="London")
cdg = Airport(code="CDG", city="Paris")
nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
jfk.save()
lhr.save()
cdg.save()
nrt.save()

# Add a flight and save it to the database
f = Flight(origin=jfk, destination=lhr, duration=414)
f.save()

f

lhr.arrivals.all()


jfk = Airport.objects.get(city="New York")

cdg = Airport.objects.get(city="Paris")

f= Flight(origin=jfk, destination=cdg, duration=435)

f.save()

Flight.objects.all()
