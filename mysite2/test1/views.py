from django.shortcuts import render
from test1.models import ActionMovie,ComedyMovie,HorrorMovie,ScienceMovie,StoryMovie
from test1 import search
# Create your views here.
import json
def home(request):

    return render(request,'homepage.html')
def home1(request):

    page=0
    pages=1
    key=request.GET['k']
    key1='%'+key+'%'
    result = search.search_mysql(key=key1,pg=page)

    if result==None :

        status = '0'
        return render(request, "home.html", {'status': status,'string1':None})
    else:
        cpage = int(int(result[2]) / 30)+1
        status = '1'
        return render(request, "home.html",{'status': status, 'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyword':key,'crtpage':page,'cpage':cpage,'crtpages':pages})
def home1pgnext(request):

    page=request.GET['pg']
    print(page)
    key=request.GET['kw']
    key1='%'+key+'%'
    print(key1)
    page1 = int(int(page)+1)
    result=search.search_mysql(key=key1,pg=page1)
    cpage = int(int(result[2]) / 30)+1
    pages=int(page1)+1
    if result==None :

        status = '0'
        return render(request, "home.html", {'status': status})
    else:
        status = '1'
        return render(request, "home.html",{'status': status, 'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyword':key,'crtpage':page1,'cpage':cpage,'crtpages':pages})
def home1pgback(request):

    page=request.GET['pg']
    print(page)
    page=str(int(page)-1)
    key=request.GET['kw']
    key1='%'+key+'%'
    print(key1)
    result=search.search_mysql(key=key1,pg=page)
    page1=(int(page))
    cpage=int(int(result[2])/30)+1
    pages=int(page)+1
    if result==None :

        status = '0'
        return render(request, "home.html", {'status': status})
    else:
        status = '1'
        return render(request, "home.html",{'status': status, 'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyword':key,'crtpage':page1,'cpage':cpage,'crtpages':pages})
def turntopage(request):

    page=request.GET['pgs']
    page1=int(page)-1
    key=request.GET['kw1']
    key1 = '%' + key + '%'
    pages=int(page)
    result = search.search_mysql(key=key1, pg=page1)
    cpage = int(int(result[2]) / 30)+1
    status='1'
    print(result[0])
    return render(request,"home.html",{'status': status,'string1': json.dumps(result[0]),'countpg': result[1],'countall': result[2],'keyword':key,'crtpage':page1,'cpage':cpage,'crtpages':pages})
def movies(request):
    mv=request.GET['id']
    pages = 1
    page = 0
    mv=int(mv)
    result=search.search_mysql_move(id=mv,pg=page)
    cpage = int(int(result[2]) / 30) + 1
    return render(request, "home1.html",{'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyid': mv, 'crtpage': page, 'cpage': cpage, 'crtpages': pages})
def movies_next(request):
    mv = request.GET['id']
    page = request.GET['pgs']
    mv = int(mv)
    page1 = (int(page)+1)
    result = search.search_mysql_move(id=mv, pg=page1)
    cpage = int(int(result[2]) / 30) + 1
    pages = int(page1) + 1

    return render(request,"home1.html",{'string1': json.dumps(result[0]),'countpg': result[1], 'countall': result[2], 'keyid': mv, 'crtpage': page1, 'cpage': cpage, 'crtpages': pages})
def movies_back(request):
    mv = request.GET['id']
    page = request.GET['pgs']
    mv = int(mv)
    page = str(int(page)-1)
    result = search.search_mysql_move(id=mv, pg=page)
    cpage = int(int(result[2]) / 30) + 1
    page1=int(page)
    pages = int(page1) + 1
    return render(request,"home1.html",{'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyid':mv, 'crtpage': page1, 'cpage': cpage, 'crtpages': pages})
def movies_turntopage(request):
    mv = request.GET['id']
    page = request.GET['pgs']
    page1=int(page)-1
    pages=int(page)
    mv = int(mv)
    result = search.search_mysql_move(id=mv, pg=page1)
    cpage = int(int(result[2]) / 30) + 1
    return render(request,"home1.html",{'string1': json.dumps(result[0]), 'countpg': result[1], 'countall': result[2],'keyid': mv, 'crtpage': page1, 'cpage': cpage, 'crtpages': pages})
