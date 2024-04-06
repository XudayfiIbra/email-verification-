from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import secrets
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = ('email')
    REQUIRED_FIELDS = ['username']
    
    def _str__(self):
        return self.email
    
class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otps')
    code = models.CharField(max_length=8, default=secrets.token_hex(4))
    code_created_date = models.DateTimeField(auto_now_add=True)
    exp_code_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

