from django.contrib import admin

from.models import *

# Register your models here.

class MasterAdmin(admin.ModelAdmin) :

    list_display = ['created_user','created_date','isactive']
    def save_model(self, request, obj, form, change):
        # Set the created_user field to the currently logged-in user
        obj.created_user = request.user
        super().save_model(request, obj, form, change)


class StudentAdmin(MasterAdmin) :
    
    list_display = ['Name','Mobile','Email','Batch','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Student,StudentAdmin)

class SystemAllocationAdmin(MasterAdmin) :
    
    list_display = ['students','From','To','system','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(SystemAllocation,SystemAllocationAdmin)