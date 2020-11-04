from django.contrib import admin
from adminuser.models import Admins, Report
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    model = Admins
    ordering = ('email',)
    list_display = ('email','name','phone','picture','is_admin','is_staff','is_active','date_joined','last_login')
    search_fields = ('email','name')
    readonly_fields = ('date_joined','last_login')
    fieldsets = (
        (None, {'fields': ('email','name','phone','picture','is_admin','is_staff','is_active','date_joined','last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','name','phone','picture','is_admin','is_staff','is_active','date_joined','last_login'),
        }),
    )
    filter_horizontal = ()

    list_filter = ()
  
class ReportList(admin.ModelAdmin):
    model = Report
    list_display = ['Action_by', 'Action','Action_to','datetime']


admin.site.register(Admins, AccountAdmin)
admin.site.register(Report, ReportList)
admin.site.site_header = "Superadmin Panel"
admin.site.site_title = "Superadmin Panel"
admin.site.index_title = "Welcome to Sathi Administration"