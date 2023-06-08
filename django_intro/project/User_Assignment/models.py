from django.db import models


# Create your models here.

class UserModel(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()

    def __str__(self):
        return self.name


class UserProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, null=True, blank=True,
                                related_name="user_profile_model")
    bio = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    university = models.CharField(max_length=30)


class UserPostModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    user_des = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="user_post_model")

    def __str__(self):
        return self.title
