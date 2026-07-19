from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.deconstruct import deconstructible


@deconstructible
class VehicleImageStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("location", settings.BASE_DIR / "static" / "images" / "vehicles")
        kwargs.setdefault("base_url", f"{settings.STATIC_URL}images/vehicles/")
        super().__init__(*args, **kwargs)
