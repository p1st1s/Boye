from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Represent a project instance in a portfolio
    """
    project_name = models.CharField(max_length=100)
    
    short_description = models.TextField(max_length=1000,\
        help_text="Enter a short description of the project")
    
    category = models.ForeignKey('Category',\
        on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return(self.project_name)


class Category(models.Model):
    """
    Represent the category of service that a project belongs
    to.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        string for representint the model object
        """
        return(self.name)


class Service(models.Model):
    """
    Represent a service provided to customers
    """
    name = models.CharField(max_length=100)

    summary = models.TextField(max_length=1000,\
        help_text='Enter a short description of the service')