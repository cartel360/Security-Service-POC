from django.db import models
   

class RoleType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Role(models.Model):
    role_type = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class UserGroup(models.Model):
    name = models.CharField(max_length=20)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.name
    
class UserGroupUser(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " - " + self.user_group.name
    
