from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,passkey,full_name,password =None,is_staff=False,is_admin=False,is_active =True):
        if not passkey:
            raise ValueError('You must have a passkey')
        if not password:
            raise ValueError('you must have a password')
        user_obj=self.model
        (
            passkey == self.normalize_passkey(passkey)
            )
        user_obj.set_password(password)
        user_obj,staff =is_staff
        user_obj.admin=is_admin
        user_obj.active =active
        user_obj.save(using=self.db)
        return user_obj
    def create_staffuser(self,passkey,password=None):
        user = self.create_user(passkey,
        password=password,
        is_staff =True)
        return user
    def create_superuser(self,passkey,password=None):
        user = self.create_user(passkey,
        password=password,
        is_staff =True,
        is_admin =True,
        )
        return user
class User(AbstractBaseUser):
    passkey = models.CharField(max_length=50, blank=True)
    active =models.BooleanField(default=True)
    staff =models.BooleanField(default=False)
    admin  =models.BooleanField(default=False)
    Timestamp  = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD ='passkey'
  
    objects =UserManager()
    
    def _str_(self):
        return self.passkey
    def get_first_name(self):
        return self.passkey
    def get_last_name(self):
        return self.passkey
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
    
    
    