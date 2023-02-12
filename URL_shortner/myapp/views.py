from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LongtoShort

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world!")

def home_page(request):
    context= { #made dic here 
        "submitted": False, #box should not be visible at start
        "error": False #error should not be visible at start
    }
    if request.method == 'POST': #if form request method is post
        data=request.POST # dict stores 2 inputs taken from user 
        # context["submitted"]= True
        # print(request.post)
        
        # sending thses variables to template
        long_url = data['longurl'] #storing long url
        custom_name = data['custom_name'] #storing custom name

        try: #error can be that the alias is already existing hence try and except block
            
            #create
            obj = LongtoShort(long_url = long_url, short_url = custom_name) #inserting row in db dynamically
            obj.save()

            #read
            date = obj.date
            clicks = obj.clicks
            context["long_url"]=long_url #store url in dictionary
            context["short_url"]= request.build_absolute_uri() + custom_name # absolute uri includes front part + we add custom name
            context["date"] = date
            context["clicks"] = clicks                       
            context["submitted"] = True # we can show box now
        except:
            context["error"] = True
    else:
        print("User not sending anything")
    # print(request.method) to see request method use this
    return render(request, 'index.html', context) # to open page use renderr

#link par click karne ke baad redirect hona chahiye
def redirect_url(request, short_url): #we got shorturl from urls.py
    
    row = LongtoShort.objects.filter(short_url = short_url) #we will filter shorturl and include in row
    if len(row) == 0: #if no url present 
        return HttpResponse("No such url exists")
    obj = row[0] # long url 
    long_url = obj.long_url

    obj.clicks = obj.clicks + 1
    obj.save()
    return redirect(long_url) #short se long ko redirect kiya

def all_analytics(request):
    rows = LongtoShort.objects.all() #to fetch all rows
    context = { 
        "rows": rows
    }
    return render(request, "all-analytics.html",context)

def task(request):
    # send dynamic data
    context = {
        "my_name": "Dhanashree", # to display dynamic name in html from here
        "x": "5"
    }
    return render(request, "test.html", context )
