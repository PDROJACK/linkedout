from django.db import models
import crypt
import json

# Create your models here.
class User(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    username = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    isEmployer = models.BooleanField()
    hashs = models.CharField(max_length=256)
    salt = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    def post(request):
        data=json.loads(request.body)
        password = data["password"]
        data.pop("password")
        data["salt"] = crypt.mksalt()
        data["hashs"] = crypt.crypt(password, salt=data["salt"])
        user = User(**data)
        user.save()

    def setPassword(self, password):
        self.salt = crypt.mksalt()
        self.hash = crypt.crypt(password, salt=self.salt)
        self.save()

    def validPassword(self, password):
        hash = crypt.crypt(password, salt=self.salt)
        return self.hash == hash
