from django.contrib import admin

# Register your models here.
# "." becoz we are already in polls folder... so
from .models import Question , Choice

admin.site.register(Question)
admin.site.register(Choice)
