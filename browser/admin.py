from django.contrib import admin
from .models import EntityType, Entity, DataFile

admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(DataFile)
