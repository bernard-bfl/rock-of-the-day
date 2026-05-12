from django.db import models

# Create your models here.

class Rock(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100) #here it could be igneous, sedimentary or metamorphic 
    hardness_min = models.FloatField(blank=True, null=True)
    hardness_max = models.FloatField(blank=True, null=True)  #using moh's scale 
    image_url = models.URLField()
    location_found = models.TextField(help_text="Regions where this rock is common")
    formation = models.TextField(help_text="The geological process that created this rock")
    uses = models.TextField()
    transparency = models.CharField(max_length=50)
    fun_fact = models.TextField()

    def __str__(self):
        return self.name
