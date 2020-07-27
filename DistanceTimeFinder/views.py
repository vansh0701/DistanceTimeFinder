from django.shortcuts import render
import requests
from django.conf import settings
from datetime import datetime
from django.contrib import messages
def home(request):
    try:
        if request.method=='POST':
            origin=request.POST['origin']
            destination=request.POST['destination']
            
            r=requests.get("http://www.mapquestapi.com/directions/v2/route?from=" +origin + "&to="+destination+"&key=PEYIGSBz15WYXDv2AgGGUkiLjXCBKobx&unit=k").json()

            data={
            
            'distance':round(float(r["route"]["distance"])),
            'time':datetime.strptime(r["route"]["formattedTime"],'%H:%M:%S').time()
            }
        
            print(data['distance'])
            print(data['time'].hour)
            print(data['time'].minute)

        
            return render(request,'submit.html',{'data':data})

        else:
            return render(request,'index.html')

    except KeyError:
        messages.info(request,"location not found")
        return render(request,'index.html')