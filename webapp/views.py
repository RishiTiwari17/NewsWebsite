from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from webapp.models import Plan
import razorpay
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
 
from allauth.socialaccount.models import SocialAccount
import pandas as pd
# Create your views here.
from rest_framework import viewsets
from webapp.serializer import ApiSerializer , CountrySerializer , categorySerializer , keywordSerializer
from webapp.models import api , Keyword , category ,country , UserSubsDetails
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from webapp.Pagination import pagination
class ApiData(viewsets.ModelViewSet):
    queryset = api.objects.all()
    serializer_class = ApiSerializer
    # filter_backends = [DjangoFilterBackend]
    pagination_class = pagination
    filter_backends = [SearchFilter , DjangoFilterBackend]
    search_fields =  ['ID' ,  
            'source_id' , 
            'Country__CountryName' , 
            'keyword__key_word' , 
            'category__categoryName' , 
            'title' , 
            'link' , 
            'Creator' , 
            'video_url' , 
            'description' , 
            'content' , 
            'image'  , 
            'pubDateTime',
            'pubTimeZone', 
            'source_name' , 
            'source_url' ,
            'language' , 
            'ai_tag' , 
            'sentiment' ,
            'sentiment_stats' , 
            'ai_region' , 
            'ai_org']

    filterset_fields = ['ID' , 'Country__CountryName' ,   'source_id' , 'category__categoryName'  ]
    

class CountryData(viewsets.ModelViewSet):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter]
    search_fields =  ['Country']

class categoryData(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categorySerializer
    filter_backends = [SearchFilter]
    search_fields =  ['category']
class keywordData(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = keywordSerializer




URL = "http://127.0.0.1:8000/api/data/"

from allauth.socialaccount.signals import social_account_added, pre_social_login
from django.dispatch import receiver

# @receiver(pre_social_login)
# def link_to_existing_user(sender, request, sociallogin, **kwargs):
#     # Example logic: Link Google account to existing user based on email
#     user_email = sociallogin.account.extra_data.get('email')
#     if user_email:
#         try:
#             user = User.objects.get(email=user_email)
#             sociallogin.connect(request, user)
#         except User.DoesNotExist:
#             pass

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        uname = email.strip('@gmail.com')
        
        # social_acc = SocialAccount.objects.get('Username')
        password = request.POST.get('password')
        user = authenticate(request  , username=uname , password=password)
        if user is not None:
            login(request , user)
            request.session['Username'] = uname
            request.session['email'] = email
            return redirect('home')
        else:
            return redirect('login')
    return render(request , 'login.html')

def Logout(request):
    
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def index(request):
    username = request.session.get('Username')
    
    
    if request.method == 'GET':
        # print(User.username)
        cursor = request.GET.get('cu', None)
        params = {'cu': cursor} if cursor else {}
        cat = requests.get('http://127.0.0.1:8000/api/category/').json()
        response = requests.get(url=URL ,  params=params).json()
        
        
        data = {
                'res' : response,
                'cat':cat,
                'prev' : response.get('previous'),
                'next' : response.get('next'),
                'name' : username
            }
        abc = set()
        if data['prev'] is not None:
            data['prev'] = data['prev'].strip('http://127.0.0.1:8000/api/data/')
        
        data['next'] = data['next'].strip('http://127.0.0.1:8000/api/data/')
        for e in  data['cat']:
            e['categoryName'] = "".join(filter(lambda c : c!= "]" , e['categoryName']))
            abc.add(e['categoryName'])
            data['cat'] = abc
            SearchInbox = request.GET.get('Search')
            # print(SearchInbox)
            data['search'] = SearchInbox
    return render(request , 'index.html' , data)

def Category(request):
    category = request.GET.get('category', None)
    params = {'category': category} if category else {}
    response = requests.get('http://127.0.0.1:8000/api/data/?Country__CountryName=&ID=&category__categoryName='+category).json()
    cat = requests.get('http://127.0.0.1:8000/api/category/').json()
    abc = set()
    for e in cat:
        e['categoryName'] = "".join(filter(lambda c : c!= "]" , e['categoryName']))
        abc.add(e['categoryName'])
           
    catData = {
        'res' : response,
        'category' : category,
        'cat' : abc
    }

    return render(request , 'Category.html' , catData)




def SearchBar(request):
    search = request.GET.get('search' , None)
    cursor = request.GET.get('cu', None)
    params = {'cu': cursor} if cursor else {}
    response = requests.get('http://127.0.0.1:8000/api/data/?search='+search , params=params).json()
    Sugeestion = requests.get('http://127.0.0.1:8000/api/data/?Country__CountryName=&ID=&category__categoryName=Top').json()
    cat = requests.get('http://127.0.0.1:8000/api/category/').json()
    
    abc = set()
    for e in cat:
        e['categoryName'] = "".join(filter(lambda c : c!= "]" , e['categoryName']))
        abc.add(e['categoryName'])

    InfoData = {
        'data' : response,
        'cat' : abc,
        'search': search,
        'sug' : Sugeestion,
        'prev' : response.get('previous'),
        'next' : response.get('next')

    }
    if response['next'] is not None:
        InfoData['next'] = InfoData['next'].strip('http://127.0.0.1:8000/api/data/')
    if InfoData['prev'] is not None:
        InfoData['prev'] = InfoData['prev'].strip('http://127.0.0.1:8000/api/data/')
        
    
    return render(request , 'info.html' , InfoData)



def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        uname = email.strip('@gmail.com')
        request.session['Username'] = uname
        passwordOne = request.POST.get('passwordOne')
        passwordTwo = request.POST.get('passwordTwo')
       
        if passwordOne != passwordTwo:
            return HttpResponse("password are not match")
        else:
            myuser = User.objects.create_user(uname , email , passwordOne)
            myuser.save()
            return redirect('login')
    return render(request , 'signin.html')


def subsription(request):

    if request.user.is_authenticated:
        cat = requests.get('http://127.0.0.1:8000/api/category/').json()
    
        abc = set()
        for e in cat:
            e['categoryName'] = "".join(filter(lambda c : c!= "]" , e['categoryName']))
            abc.add(e['categoryName'])
        planDetails = Plan.objects.all()
        data = {
            'cat' : abc,
            'amountOne' : 1,
            'amountTwo' : 2,
            'Currency' : 'INR',
            'plans' : planDetails,
        }

        # request.session['amount'] =  planDetails['amount']
        # request.session['amountTwo'] = data['amountTwo']
        return render(request , 'subs.html' , data)
    return redirect('login')
    
client = razorpay.Client(auth = (settings.RAZOR_KEY_ID , settings.RAZOR_KEY_SECRET))
@login_required
def payment(request , amount):
    amount = int(amount)
    request.session['amount'] = amount
    data = {      
            'amount' : amount,
            
        }
    razorpay_order = client.order.create({'amount':amount*100 , 'currency':'INR' , 'payment_capture':1})
    data['payment'] = razorpay_order 
    return render(request , 'payment.html' , data)


def fail(request):
    return render(request , 'failure.html')
@login_required
@csrf_exempt
def result(request):
    return render(request , 'payres.html' )

    