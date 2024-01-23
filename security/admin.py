from django.contrib import admin
from .models import RoleType, Role, UserGroup, UserGroupUser


admin.site.register(RoleType)
admin.site.register(Role)
admin.site.register(UserGroup)
admin.site.register(UserGroupUser)



