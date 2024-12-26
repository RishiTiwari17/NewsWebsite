from django.contrib import admin
from webapp.models import api , category , country , Keyword , UserSubsDetails , Plan 
# Register your models here.

@admin.register(api)
class ApiModel(admin.ModelAdmin):
    list_display = ['ID' , 'title' , 'link' , 'Creator' , 'video_url' , 'description' , 'content' , 'pubDateTime' , 'pubTimeZone' , 'image'  , 'source_id' , 'source_name' , 'source_url' , 'language' , 'ai_tag' , 'sentiment' , 'sentiment_stats' , 'ai_region' , 'ai_org']

@admin.register(category)
class categoryModel(admin.ModelAdmin):
    list_display = ['id' , 'categoryName' , 'relatedTo']

@admin.register(country)
class countryModel(admin.ModelAdmin):
    list_display = ['id' , 'CountryName' , 'relatedTo']

@admin.register(Keyword)
class keywordModel(admin.ModelAdmin):
    list_display = ['id' , 'key_word' , 'relatedTo']

@admin.register(UserSubsDetails)
class UserSubsDetailsModel(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'contact' , 'city' , 'state' , 'country' , 'order_id' , 'order_payment_id' , 'order_signature_id' , 'amount']

@admin.register(Plan)
class PlanDetailsModel(admin.ModelAdmin):
    list_display = ['title' , 'amount' , 'featureOne' , 'featureTwos' , 'featureThree' , 'featureFour' , 'featureFive' , 'featureSix' , 'featureSeven']

