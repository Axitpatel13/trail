from django.contrib import admin
from .models import services,site_info,about_us,case_studies,contact_us
# Register your models here.
admin.site.register(services)
admin.site.register(site_info)
admin.site.register(about_us)
admin.site.register(case_studies)
admin.site.register(contact_us)