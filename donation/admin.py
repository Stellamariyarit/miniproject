from django.contrib import admin
from .models import Donor, Recipient, Organ

admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Organ)
