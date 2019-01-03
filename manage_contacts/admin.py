from django.contrib import admin

from .models import Person, Contact

admin.site.register(Person)
admin.site.register(Contact)