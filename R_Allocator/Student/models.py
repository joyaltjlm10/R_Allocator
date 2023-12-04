from django.db import models
from django.contrib.auth.models import User
from ResourceAllocator . models import Batch,RoomAllocation,System,Branch
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Master(models.Model) :
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True,verbose_name='active')
    created_user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    class Meta :
        abstract = True
        ordering = ['isactive']
 

SYSTEM_CHOICES = [
    ('Yes','YES'),
    ('No','NO')
]

class Student(Master) :
    Name = models.CharField(max_length=50,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: 'xxxxxxxxxx'. Up to 10 digits allowed.")
    Mobile = models.CharField(validators=[phone_regex], max_length=10) # validators should be a list
    Email = models.CharField(max_length=50)
    Batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    # Class = ChainedForeignKey(RoomAllocation,chained_field="Batch",chained_model_field="Batch",show_all=False,auto_choose=True,null=True,sort=True,limit_choices_to={"isactive": True})
    Have_Own_System = models.BooleanField(default=False,blank=False)

    def __str__(self):
        return self.Name
        
    class Meta:
        verbose_name_plural = "Students"

class SystemAllocation(Master) :
    Branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True)
    Batch = ChainedForeignKey(Batch,chained_field="Branch",chained_model_field="branch",show_all=False,auto_choose=True,sort=True,null=True,blank=False,limit_choices_to={"isactive": True},)
    students = ChainedForeignKey(Student,chained_field='Batch',chained_model_field='Batch',show_all=False,auto_choose=True,null=True,sort=True,limit_choices_to={'Have_Own_System' : False,'systemallocation__isnull' : True})
    # students = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,limit_choices_to={'Have_Own_System' : False})
    start_date = models.DateField(null=True)
    From = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    To = models.TimeField(null=True)
    system = ChainedForeignKey(System, chained_field="Branch",chained_model_field="branch",show_all=False,auto_choose=True,sort=True,null=True,blank=False,limit_choices_to={"isactive": True,'systemallocation__isnull' : True})
    
    # def clean(self) :
    #     # Check if the system is already allocated during the specified time range
    #     if self.system and self.From and self.To :
    #         conflicting_allocations = SystemAllocation.objects.filter(system = self.system,From__lt = self.To,To__gt = self.From,start_date__lt = self.end_date,end_date__gt = self.start_date,).exclude(pk=self.pk)

    #         if conflicting_allocations.exists():
    #             raise ValidationError({'From' : 'This system is already allocated during the specified time range.'})

    #     super().clean()