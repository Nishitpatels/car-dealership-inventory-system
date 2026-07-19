from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from django.conf import settings
from django.utils.text import slugify

VEHICLE_IMAGE_DIR = settings.BASE_DIR / "static" / "images" / "vehicles"
DEFAULT_IMAGE_NAME = "default-vehicle.svg"

CURATED_IMAGE_SOURCES = {
    "bmw": "https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=1200&q=85",
    "mercedes": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?auto=format&fit=crop&w=1200&q=85",
    "audi": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?auto=format&fit=crop&w=1200&q=85",
    "toyota": "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=1200&q=85",
    "tesla": "https://images.unsplash.com/photo-1617788138017-80ad40651399?auto=format&fit=crop&w=1200&q=85",
    "ford": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1200&q=85",
    "hyundai": "https://images.unsplash.com/photo-1494905998402-395d579af36f?auto=format&fit=crop&w=1200&q=85",
    "mahindra": "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&w=1200&q=85",
}


def ensure_vehicle_image_dir():
    VEHICLE_IMAGE_DIR.mkdir(parents=True, exist_ok=True)


def default_vehicle_image_name():
    ensure_vehicle_image_dir()
    return DEFAULT_IMAGE_NAME


def existing_vehicle_image_name(vehicle):
    ensure_vehicle_image_dir()
    candidates = [
        f"{vehicle.make} {vehicle.model}.jpg",
        f"{slugify(f'{vehicle.make}-{vehicle.model}') or 'vehicle'}.jpg",
    ]
    for filename in candidates:
        if (VEHICLE_IMAGE_DIR / filename).exists():
            return filename
    return None


def assign_vehicle_image(vehicle):
    if vehicle.image:
        return

    ensure_vehicle_image_dir()
    existing = existing_vehicle_image_name(vehicle)
    if existing:
        vehicle.image = existing
        return

    filename = f"{slugify(f'{vehicle.make}-{vehicle.model}') or 'vehicle'}.jpg"
    target = VEHICLE_IMAGE_DIR / filename

    source = CURATED_IMAGE_SOURCES.get(vehicle.make.lower())
    if source:
        try:
            request = Request(source, headers={"User-Agent": "NexusMotorsVehicleImage/1.0"})
            with urlopen(request, timeout=2.5) as response:
                if response.status == 200:
                    target.write_bytes(response.read())
                    vehicle.image = filename
                    return
        except (OSError, URLError, TimeoutError):
            pass

    vehicle.image = default_vehicle_image_name()


def delete_vehicle_image_if_unused(vehicle):
    if not vehicle.image or Path(vehicle.image.name).name == DEFAULT_IMAGE_NAME:
        return

    image_name = vehicle.image.name
    if vehicle.__class__.objects.filter(image=image_name).exclude(pk=vehicle.pk).exists():
        return

    image_path = VEHICLE_IMAGE_DIR / Path(image_name).name
    if image_path.exists():
        image_path.unlink()
