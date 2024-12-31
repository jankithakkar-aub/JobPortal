from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    """
    Company class represents the Company table in database
    param: base class from which all Django models inherit
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Each User has one company
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class JobPost(models.Model):
    """
    JobPost class represents the JobPost table in database
    param: base class from which all Django models inherit
    """

    company = models.ForeignKey(Company, related_name="job_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
