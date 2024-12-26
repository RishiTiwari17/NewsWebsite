from django.db import models
from datetime import timezone , datetime
# Create your models here.




class api(models.Model):
    ID = models.CharField(max_length=20 ,  blank=False , primary_key=True)
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    Creator = models.CharField(null=True , max_length=1000)
    video_url = models.CharField(blank=False ,  max_length=1000)
    description = models.CharField(max_length=1000)
    content = models.CharField(max_length=500)
    pubDateTime = models.CharField(  max_length=1000)
    pubTimeZone = models.CharField( max_length=1000)
    image = models.ImageField()
    source_id = models.CharField(max_length=200)
    source_name = models.CharField(max_length=100)
    source_url = models.CharField(max_length=1000)
    language = models.CharField(max_length=100)
    ai_tag = models.CharField(max_length=200)
    sentiment = models.CharField(max_length=200)
    sentiment_stats = models.CharField(max_length=200)
    ai_region = models.CharField(max_length=200)
    ai_org = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Keyword(models.Model):
    key_word = models.CharField(max_length=200)
    relatedTo = models.ForeignKey(api , on_delete=models.CASCADE , related_name='keyword')
    
    def __str__(self):
        return self.key_word

class country(models.Model):
    CountryName = models.CharField(max_length=200)
    relatedTo = models.ForeignKey(api , on_delete=models.CASCADE , related_name='Country')
    
    def __str__(self):
        return self.CountryName


class category(models.Model):
    categoryName = models.CharField(max_length=200)
    relatedTo = models.ForeignKey(api , on_delete=models.CASCADE , related_name='category')
    
    def __str__(self):
        return self.categoryName



class UserSubsDetails(models.Model):
    name = models.CharField(max_length=100 , null=False , blank=False)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    city = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100 , default="blank")
    order_payment_id = models.CharField(max_length=100 , default="blank")
    order_signature_id = models.CharField(max_length=100 , default="blank")


class PlansDetails(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    featureOne = models.CharField(max_length=100)
    featureTwo = models.IntegerField(default=0)
    featureThree = models.CharField(max_length=100)
    featureFour = models.CharField(max_length=100)
    featureFive = models.CharField(max_length=100 , default="blank")
    featureSix= models.CharField(max_length=100 , default="blank")
    featureSeven = models.CharField(max_length=100 , default="blank")

class Plan(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    featureOne = models.CharField(max_length=100)
    featureTwos = models.CharField(max_length=100)
    featureThree = models.CharField(max_length=100)
    featureFour = models.CharField(max_length=100)
    featureFive = models.CharField(max_length=100 , default="blank")
    featureSix= models.CharField(max_length=100 , default="blank")
    featureSeven = models.CharField(max_length=100 , default="blank")