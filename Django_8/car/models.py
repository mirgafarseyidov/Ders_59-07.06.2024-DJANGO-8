from django.db import models

# Create your models here.
class Sahib(models.Model):
    name=models.CharField(max_length = 300, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Galeriya(models.Model):
    name=models.CharField(max_length=70)    
    
    def __str__(self):
        return self.name
    

class Masin(models.Model):
    sahib=models.OneToOneField(Sahib, on_delete=models.CASCADE, related_name='masinlar')
    marka=models.CharField(max_length=70)
    model=models.CharField(max_length=70)
    galeriya=models.ForeignKey(Galeriya, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marka}-----------{self.model}"