from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    
    
    list_display = ('id','firstname','username','lastname','email','address','contactnumber','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('firstname','username','lastname','address','contactnumber')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ( 'firstname','username','lastname','email','address','contactnumber','password', 'password2'),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('id',)
    filter_horizontal =()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)

