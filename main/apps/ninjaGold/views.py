from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
import random
# the index function is called when root is visited
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0 
    if 'activity' not in request.session:
        request.session['activity'] =[]   
    
    context ={
        'gold':request.session['gold'],
        'activity':request.session['activity']
    }  

    return render(request,'ninjaGold/index.html',context)


def processMoney(request):
    temp_activity = request.session['activity']
    if 'farm' in request.POST['building']:
        request.session['time'] = strftime("%Y-%m-%d %H:%M %p", localtime())
        request.session['goldearned'] = random.randrange(10,20)
        request.session['gold'] += request.session['goldearned']
        temp_activity.append({"color":'green',"location":'farm',"gold":request.session['goldearned'],"time":request.session['time'] })


    if 'cave' in request.POST['building']:
        request.session['time'] = strftime("%Y-%m-%d %H:%M %p", localtime())
        request.session['goldearned'] = random.randrange(5,10)
        request.session['gold'] += request.session['goldearned']
        temp_activity.append({"color":'green',"location":'cave',"gold":request.session['goldearned'],"time":request.session['time'] })


    if 'house' in request.POST['building']:
        request.session['time'] = strftime("%Y-%m-%d %H:%M %p", localtime())
        request.session['goldearned'] = random.randrange(2,5)
        request.session['gold'] += request.session['goldearned']
        temp_activity.append({"color":'green',"location":'house',"gold":request.session['goldearned'],"time":request.session['time'] })


    if 'casino' in request.POST['building']:
        if request.session['gold'] <= 0:
            temp_activity.append({"broke":'true',"time":request.session['time']})
        else:
            request.session['goldearned'] += random.randrange(-50,50)
            request.session['time'] = strftime("%Y-%m-%d %H:%M %p", localtime())
            if request.session['goldearned'] > 0:
                request.session['gold'] += request.session['goldearned']
                temp_activity.append({"color":'green',"location":'casino',"gold":request.session['goldearned'],"time":request.session['time'] })

            if request.session['goldearned'] < 0:
                request.session['gold'] += request.session['goldearned']
                temp_activity.append({"color":'red',"location":'casino',"gold":(request.session['goldearned']*(-1)),"time":request.session['time']})           
                if request.session['gold'] <0:
                    request.session['gold']=0



    # temp_list.append({"words":request.session['words'] })
    
    request.session['activity'] = temp_activity



    if 'clearGold' in request.POST['building']:#FOR TESTING
        request.session['gold'] = 0
        request.session['activity'] =[]
      
    return redirect("/")