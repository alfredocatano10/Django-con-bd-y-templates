from django.contrib import admin
from .models import post, post2

model = post, post2

admin.site.register(model)
