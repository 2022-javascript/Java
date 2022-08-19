from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User,NewsData,UserInfo
from .serializer import UserSerialrizer,NewsSerialrizer,UserInfoSerialrizer,UpdateLoginTime
from django.http import QueryDict
from .AIDataGet import res_data
# from COBOK.upbit_crawling import news_crewling

import pandas as pd
# Create your views here.

@api_view(['GET'])
def index(request):
    api_urls = {
        "List" : '/boardlist/',
        "Detail" : '/boardview/<str:pk>',
        "Create" : '/boardinsert/',
        "Update" : '/boardupdate<str:pk>/',
        "Delete" : '/boarddelete<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def UserList(request):
    boards = User.objects.all()

    serializer = UserSerialrizer(boards, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def register(request):

    serializer = UserSerialrizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print('vailed data..')
    else:
        print('invalied data...')
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def NewsList(request):
    news = NewsData.objects.all()

    serializer = NewsSerialrizer(news, many = True)

    return Response(serializer.data)
@api_view(['GET'])
def UserInfoList(request):
    userInfo = UserInfo.objects.all()

    serializer = UserInfoSerialrizer(userInfo, many = True)

    return Response(serializer.data)

@api_view(['POST'])
def UserInfoPost(request):

    serializer = UserInfoSerialrizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        print('vailed data..')
    else:
        print('invalied data...')
    print(serializer.data)
    return Response(serializer.data)
    

@api_view(['GET','PUT'])
def UpdateLastLogin(request,pk):
    if request.method == "PUT":
        user_object = UserInfo.objects.get(Email=pk)
        serializer = UpdateLoginTime(instance = user_object, data = request.data)
        if serializer.is_valid():
            serializer.save()
            print('vailed data..')
        else:
            print('invalied data...')
        return Response(serializer.data)

def sign_up(request):
    return render(request, 'register.html')

def home(request):
    # news_name = pd.read_csv('/Users/yuhyeonseog/개인 작업/javascript/study_project/backend/user/news_data.csv')
    # news_name = news_name.drop(['Unnamed: 0'],axis = 1).to_numpy()
    # news_href = pd.read_csv('/Users/yuhyeonseog/개인 작업/javascript/study_project/backend/user/news_href.csv')
    # news_href = news_href.drop(['Unnamed: 0'],axis = 1).to_numpy()
    # for i in range(len(news_name)):
    #     for j in range(1,10):
    #         try:
    #             NewsData(
    #                 category = str(news_name[i][0]),
    #                 news_name = str(news_name[i][j]),
    #                 news_href = str(news_href[i][j-1])
    #             ).save()
    #         except:
    #             pass
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def userpage(request):
    return render(request, "userpage.html")

def userpageWrite(request):
    return render(request,"userpage_write.html")

def AIResearch(request):
    data = res_data()
    print(data)
    return render(request,"AIResearch.html",{'context': data})