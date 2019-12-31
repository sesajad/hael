from django.contrib import admin
from profiles.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass


class IpSpecAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(IpSpec, IpSpecAdmin)
