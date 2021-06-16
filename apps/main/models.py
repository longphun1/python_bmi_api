from django.db import models

# Create your models here.
class BmiManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if post_data['height'].isdigit()==False:
            errors['height']='Provide height'
        if post_data['weight'].isdigit()==False:
            errors['weight']='Input your weight'
        if len(post_data['sex']) > 1:
            errors['sex']='Input your sex'
        if post_data['age'].isdigit()==False:
            errors['age']='Input your age'
        if post_data['waist'].isdigit()==False:
            errors['waist']='Input your waist'

        return errors

class Bmi(models.Model):
    user = models.CharField(max_length=255, default=None)
    weight = models.CharField(max_length=255, default=None)
    height = models.CharField(max_length=255, default=None)
    sex = models.CharField(max_length=255)
    age = models.CharField(max_length=255, default=None)
    waist = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=255, default=None, null=True, blank=True)
    risk = models.CharField(max_length=255, default=None, null=True, blank=True)
    ideal = models.CharField(max_length=255, default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-created_at']

    objects = BmiManager()