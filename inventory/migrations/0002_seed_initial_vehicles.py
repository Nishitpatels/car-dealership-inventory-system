from decimal import Decimal

from django.db import migrations


INITIAL_VEHICLES = [
    ("BMW", "X5 xDrive40i", "Luxury SUV", Decimal("78500.00"), 4, "A refined, all-wheel-drive luxury SUV with intuitive technology, a panoramic cabin and confident everyday performance."),
    ("Mercedes", "C300 AMG Line", "Luxury Sedan", Decimal("62900.00"), 2, "An athletic executive sedan balancing contemporary comfort with a responsive, electrified powertrain."),
    ("Tesla", "Model Y Long Range", "Electric SUV", Decimal("54990.00"), 7, "A versatile all-electric SUV with generous range, an airy cabin and intelligent driver assistance."),
    ("Audi", "Q5 S line quattro", "Premium SUV", Decimal("59450.00"), 3, "A composed quattro SUV featuring a versatile cabin, crisp design and a confident long-distance character."),
    ("Toyota", "Fortuner Legender", "SUV", Decimal("48800.00"), 1, "A commanding seven-seat SUV made for families that value road presence, reliability and all-terrain assurance."),
    ("Hyundai", "Creta SX(O)", "Compact SUV", Decimal("27600.00"), 9, "A feature-rich compact SUV with a striking exterior and a city-friendly, comfortable drive."),
    ("Ford", "Mustang GT Premium", "Performance Coupe", Decimal("71200.00"), 0, "An iconic grand touring coupe with unmistakable V8 character and beautifully finished performance details."),
    ("Mahindra", "XUV700 AX7 L", "Family SUV", Decimal("34850.00"), 5, "A spacious seven-seat SUV offering commanding performance, forward-thinking safety and comfort."),
]


def seed_vehicles(apps, schema_editor):
    Vehicle = apps.get_model("inventory", "Vehicle")
    for make, model, category, price, quantity, description in INITIAL_VEHICLES:
        Vehicle.objects.get_or_create(
            make=make,
            model=model,
            defaults={
                "category": category,
                "price": price,
                "quantity": quantity,
                "description": description,
                "image": "default-vehicle.svg",
            },
        )


def remove_seeded_vehicles(apps, schema_editor):
    Vehicle = apps.get_model("inventory", "Vehicle")
    for make, model, *_ in INITIAL_VEHICLES:
        Vehicle.objects.filter(make=make, model=model).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_vehicles, remove_seeded_vehicles),
    ]
