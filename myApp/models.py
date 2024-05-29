from calendar import month
from time import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Class(models.Model):
    num_name = models.CharField(max_length=30, null = False,)
    class_name = models.CharField(max_length=30, null = False)
    section_nmae = models.CharField(max_length=30, null = False)
    monthly_fee = models.CharField(max_length=30, null = False)
    Fee_for_month = models.CharField(max_length=30, null = False,  default="",)
    total_fee = models.CharField(max_length=30, null = False,  default="",)
    
   
    def __str__(self):
        return self.num_name



class Person(models.Model):
    first_name = models.CharField(max_length=30, null = False,)
    last_name = models.CharField(max_length=30, null = False)

    def __str__(self):
        return self.first_name
    
class Department(models.Model):
    dprt_name = models.CharField(max_length=30, null = False)
    location = models.CharField(max_length=30, null = False)

    def __str__(self):
        return self.dprt_name
    
class Person2(models.Model):
    first_name2 = models.CharField(max_length=30, null = False)
    last_name = models.CharField(max_length=30, null = False)
    depr_name = models.ForeignKey(Department, on_delete=models.CASCADE, default="1", null=True)
    num_name = models.ForeignKey(Class, on_delete=models.CASCADE, default="", null=True)

    def __str__(self):
        return self.last_name





class Classes(models.Model):
    Class_name = models.CharField(max_length=30, null = False)
    section_name = models.CharField(max_length=30, null = False)
    monthly_fee = models.CharField(max_length=30, null = False,default="")
    fee_for_month = models.CharField(max_length=30, null = False,default="")
    total_installment = models.CharField(max_length=30, null = False,default="")
    total_amt = models.CharField(max_length=30, null = False)
    date =models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Class_name    
        
        
class Customers(models.Model):
    student_name = models.CharField(max_length=30, null = False)
    contact = models.CharField(max_length=30, null = False)
    address = models.CharField(max_length=30, null = False)
    customer_type =models.CharField(max_length=30, null = False,choices=[("Regular","Regular"),("Partial","Partial")])
    status =models.CharField(max_length=30, null = False,choices=[("Active","Active"),("Disabled","Disabled")])
    product =models.CharField(max_length=30, null = False, default="")
    previous_amount =models.CharField(max_length=30, null = False, default="")
    scholarship =models.CharField(max_length=30, null = False, default="")
    special_disc =models.CharField(max_length=30, null = False, default="")
    final_amt =models.CharField(max_length=30, null = False, default="")
    previous_dues =models.CharField(max_length=30, null = False, default="")
    remaining_fee =models.CharField(max_length=30, null = False, default="")
    fine_amt =models.CharField(max_length=30, null = False, default="")
    paid_amt =models.CharField(max_length=30, null = False, default="")
    Class_name = models.ForeignKey(Classes, on_delete=models.CASCADE, default="", null=True)
    date =models.DateField(auto_now=True)
    
    def __str__(self):
        return self.student_name
    
class Addbills(models.Model):
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE, default="", null=True)
    Installment_name = models.CharField(max_length=30, null = False)
    months_from_to = models.CharField(max_length=30, null = False)
    Installment_amount = models.CharField(max_length=30, null = False)
   
    date =models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Installment_name
    
class Payments(models.Model):
    student_name = models.CharField(max_length=30, )
    class_name = models.CharField(max_length=30, null = False)
    Installment_name = models.CharField(max_length=30, null = False)
    fee_amount = models.CharField(max_length=30, null = False,default="")
    paid_fee = models.CharField(max_length=30, null = False,default="0")
    disc_amount = models.CharField(max_length=30, null = False,default="0")
    remainng_amount = models.CharField(max_length=30, null = False,default="0")
    
    
   
    date =models.DateField(auto_now=True)
    
    def __str__(self):
        return self.Installment_name    
    
    
    
    
    # models.py

from django.db import models

class Student(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    class_or_grade = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Staff(models.Model):
    staff_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

# models.py

class AttendanceRecord(models.Model):
    date = models.DateField()
    time = models.TimeField()
    booleanvalue = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)



class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)