from django.db import models

class AuthItem(models.Model):
    name = models.CharField(max_length=32, unique=True)
    auth_type = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    rule_name = models.CharField(max_length=32, blank=True, null=True)
    data = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AuthAssignment(models.Model):
    item_name = models.ForeignKey(AuthItem, to_field='name', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', related_name='auth_assignment', on_delete=models.CASCADE)
