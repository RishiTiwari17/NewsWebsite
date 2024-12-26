from rest_framework import serializers
from webapp.models import Keyword , api , category , country

class keywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id' , 'key_word' , 'relatedTo']


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id' , 'categoryName' , 'relatedTo']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = ['id' , 'CountryName' , 'relatedTo']

class ApiSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True , read_only=True)
    Country = serializers.StringRelatedField(many=True , read_only=True)
    keyword = serializers.StringRelatedField(many=True , read_only=True)
    class Meta:
        model = api
        fields = [
            'ID' , 
            'title' , 
            'link' , 
            'Creator' , 
            'video_url' , 
            'description' , 
            'content' , 
            'image'  , 
            'category',
            'pubDateTime',
            'pubTimeZone',
            'Country',
            'keyword',
            'source_id' , 
            'source_name' , 
            'source_url' ,
            'language' , 
            'ai_tag' , 
            'sentiment' ,
            'sentiment_stats' , 
            'ai_region' , 
            'ai_org'
        ]

        def get_photo_url(self  , obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_url(photo_url)