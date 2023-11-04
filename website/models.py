from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    application_date = models.DateField()
    location = models.CharField(max_length=50)
    current_status = models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.company_name}")