from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','is_active','date_joined','last_login') # Added last_login
    actions = ['ban_users','unban_users']


 #USER BANNING FUNCTION
    def ban_users(self, request, queryset):
        queryset.update(is_active = False)

 #USER UNBANNING FUNCTION
    def unban_users(self, request, queryset):
        queryset.update(is_active = True)

class YourModelAdmin(admin.ModelAdmin):
    change_form_template = 'custom_change_form.html'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
