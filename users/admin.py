from django.contrib import admin
from .models import User, Citizenship, education, experience, Address
# Register your models here.
admin.site.register(User)
admin.site.register(Citizenship)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(Address)