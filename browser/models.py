import uuid
from django.db import models
from django.utils import timezone

class EntityType(models.Model):
    name = models.CharField(max_length=256)
    is_file_required = models.BooleanField()
    imo_field = models.BooleanField(default=False)
    spec_document = models.CharField(max_length=128)
    media_type = models.CharField(max_length=256)

    ordering = (
        "name",
    )

    def __str__(self):
        return self.name


class Entity(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    kind = models.ForeignKey(EntityType, on_delete=models.CASCADE)
    metadata = models.TextField(max_length=8192, blank=True)

    ordering = (
        "name",
    )
    
    def __str__(self):
        return f"{self.name} ({self.kind.name})"


class DataFile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024, default="noname")
    upload_date = models.DateTimeField(default=timezone.now, editable=False)
    metadata = models.TextField(max_length=8192)
    file_data = models.FileField(blank=True)
    spec_version = models.CharField(max_length=32)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    notes = models.TextField(max_length=4096, blank=True)
    dependencies = models.ManyToManyField("DataFile", blank=True)

    ordering = (
        "upload_date",
        "name",
    )
    
    def __str__(self):
        return f"{self.name} ({self.entity.kind.name}, {str(self.uuid)[0:7]})"
