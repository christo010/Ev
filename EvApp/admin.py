from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from EvApp.models import Department,CustUser,Complaint

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the admin panel
    fieldsets = (
         (None, {'fields': ('username', 'password')}),
         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_officer', 'departments')}),
        # ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    # Include is_officer and departments in the 'list_filter' if you want to filter users based on these fields
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'departments', 'is_officer')
    list_display = ['username', 'is_officer', 'email','is_staff']


admin.site.register(Department)
admin.site.register(CustUser,CustomUserAdmin)
admin.site.register(Complaint)

