from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Citizenship)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(Address)
admin.site.register(Country)