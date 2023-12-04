from django.contrib import admin

from.models import *

# Register your models here.

class MasterAdmin(admin.ModelAdmin) :

    list_display = ['created_user','created_date','isactive']
    def save_model(self, request, obj, form, change):
        # Set the created_user field to the currently logged-in user
        obj.created_user = request.user
        super().save_model(request, obj, form, change)

class StateAdmin(MasterAdmin) :

    
    list_display = ['name','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(State,StateAdmin)


class DistrictAdmin(MasterAdmin) :
    
    list_display = ['Dist_Name', 'State','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(District,DistrictAdmin)


class BranchAdmin(MasterAdmin) :
    
    list_display = ['branch','branch_code','address','street','state','district','pincode','email','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Branch,BranchAdmin)


class ComputerBrandAdmin(MasterAdmin) :
    
    list_display = ['Name','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ComputerBrand,ComputerBrandAdmin)


class CourseAdmin(MasterAdmin) :
    
    list_display = ['course','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Course,CourseAdmin)


class BatchAdmin(MasterAdmin) :
    
    list_display = ['batch','branch','course','start_date','start_time','end_date','Trainer','isactive']
    exclude = ['created_user','batch']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Batch,BatchAdmin)


class SystemAdmin(MasterAdmin) :
    
    list_display = ['Code','Brand','branch','Category','RentalorOwn','DateofPurchase','Amount','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(System,SystemAdmin)


class RoomAdmin(MasterAdmin) :
    
    list_display = ['Name','Branch','Floor','Type','NoofSeats','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Room,RoomAdmin)


class RoomAllocationAdmin(MasterAdmin) :

    list_display = ['Room','Reservation_Type','Batch','From','To','Purpose','isactive']
    exclude = ['created_user']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(RoomAllocation,RoomAllocationAdmin)


admin.site.site_header = 'R_Allocator Admin'

admin.site.site_title = 'Admin R_Allocator'

admin.site.index_title = 'Welcome to Resource Allocator'
