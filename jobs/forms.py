from django import forms
from .models import Company, JobPost

class CompanyRegistrationForm(forms.ModelForm):
    """
    This class is used to create a new form for company.
    param: converts the model into django form
    """
    class Meta:
        """
        Configuration class for the form. Includes defining the model and fields
        """
        model = Company
        fields = ["name", "address", "contact_number"]

class JobPostForm(forms.ModelForm):
    """
    This class is used to create new job posts.
    param: converts the model into django form
    """
    class Meta:
        """
        Configuration class for the form. Includes defining the model and fields
        """
        model = JobPost
        fields = ["title", "description", "location", "salary_range", "tags"]

