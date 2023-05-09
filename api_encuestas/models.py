from django.db import models
# from django.contrib.auth.models import User


# class user(User):
#     state = models.BooleanField(default=True)

class company(models.Model):
    name= models.CharField(max_length=100)
    is_active= models.BooleanField(default=True)
    create_at= models.DateTimeField(auto_now_add=True)
    delete_at= models.DateTimeField(default=False)

class domain(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    id_company = models.ForeignKey(company, on_delete=models.CASCADE, related_name='fk_id_company_domain')
    create_at= models.DateTimeField(auto_now_add=True)
    delete_at= models.DateTimeField(default=False)


# class poll(models.Model):


# class companiy_poll(models.Model):
#     name = models.CharField(max_length=100)
#     id_company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_id_company_domain')
#     id_poll = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_id_company_domain')
#     is_active = models.BooleanField(default=True)
#     create_at= models.DateTimeField(auto_now_add=True)
#     delete_at= models.DateTimeField(default=False)
