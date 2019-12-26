from django.shortcuts import render


import sys

from subprocess import run,PIPE

def button(request):


    return render(request,'home.html')





def external(request):

    

    out= run([sys.executable,'/home/zeus/Desktop/DiVe/Django/DjangoProj/log.py'],shell=False,stdout=PIPE)

    print(out)


    return render(request,'home.html',{'data1':out.stdout.decode('utf-8')})