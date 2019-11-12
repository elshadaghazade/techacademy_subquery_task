import os, datetime, random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "evreka_proj.settings")
    
    import django; django.setup();

    from vehicle_app.models import *
    
    # creating 4 vehicles
    vehicles = []
    Vehicle.objects.all().delete()
    
    for i in range(4):
        vehicle = Vehicle()
        vehicle.plate = "10 AB 10" + str(i)
        vehicles.append(vehicle)

    Vehicle.objects.bulk_create(vehicles)

    # creating 1000000 random points
    NavigationRecord.objects.all().delete()
    points = []
    dt = datetime.datetime.now()
    for i in range(10000001):
        if not i % 20000:
            NavigationRecord.objects.bulk_create(points)
            dt = datetime.datetime.now()
            points = []

        dt -= datetime.timedelta(minutes=random.randint(1, 5))
        point = NavigationRecord()
        point.vehicle = random.choice(vehicles)
        point.latitude = random.random() * 180
        point.longitude = random.random() * 180
        point.datetime = dt
        points.append(point)
