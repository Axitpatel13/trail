from django.contrib import admin
from .models import user
from app.models import payment_request
# Register your models here.
admin.site.register(user)
admin.site.register(payment_request)