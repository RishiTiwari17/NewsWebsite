from django.urls import path , include
from rest_framework.routers import DefaultRouter
from webapp.views import ApiData , CountryData , categoryData , keywordData
router = DefaultRouter()

router.register('data' , ApiData , basename='DataAPI')
router.register('country' , CountryData , basename='CountryAPI')
router.register('category' , categoryData , basename='CategoryAPI')
router.register('keyword' , keywordData , basename='KeywordAPI')



urlpatterns = [
    path('' , include(router.urls)),
]