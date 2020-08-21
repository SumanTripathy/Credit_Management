from django.contrib import admin
from cm.models import User,history

# Register your models here.
admin.site.register((User,history))