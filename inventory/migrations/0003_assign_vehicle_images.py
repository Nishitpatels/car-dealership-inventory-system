from django.db import migrations


VEHICLE_IMAGES = {
    ("BMW", "X5 xDrive40i"): "BMW X5 xDrive40i.jpg",
    ("Mercedes", "C300 AMG Line"): "Mercedes C300 AMG Line.jpg",
    ("Tesla", "Model Y Long Range"): "Tesla Model Y Long Range.jpg",
    ("Audi", "Q5 S line quattro"): "Audi Q5 S line quattro.jpg",
    ("Toyota", "Fortuner Legender"): "Toyota Fortuner Legender.jpg",
    ("Hyundai", "Creta SX(O)"): "Hyundai Creta SX(O).jpg",
    ("Ford", "Mustang GT Premium"): "Ford Mustang GT Premium.jpg",
    ("Mahindra", "XUV700 AX7 L"): "Mahindra XUV700 AX7 L.jpg",
}


def assign_vehicle_images(apps, schema_editor):
    Vehicle = apps.get_model("inventory", "Vehicle")
    for (make, model), image_name in VEHICLE_IMAGES.items():
        Vehicle.objects.filter(make=make, model=model).update(image=image_name)


def revert_vehicle_images(apps, schema_editor):
    Vehicle = apps.get_model("inventory", "Vehicle")
    for make, model in VEHICLE_IMAGES:
        Vehicle.objects.filter(make=make, model=model).update(image="default-vehicle.svg")


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_seed_initial_vehicles"),
    ]

    operations = [
        migrations.RunPython(assign_vehicle_images, revert_vehicle_images),
    ]
