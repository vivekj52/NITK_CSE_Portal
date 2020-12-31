from django.contrib import admin
from .models import Undergraduate, Postgraduate, Doctoral

admin.site.register(Undergraduate)
admin.site.register(Postgraduate)
admin.site.register(Doctoral)
