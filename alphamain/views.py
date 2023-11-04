from django.shortcuts import render, redirect
from .models import (studentlist, 
                     Events, ProjectPresentation,
                     PaperPresentation,
                     Ideathon,
                     Product,
                     TotalRegistration
                     )

def home(request):
    return render(request, "alphamain/home.html")

def project(request):
    if request.method == 'POST':
            Projectname = request.POST.get("pname")
            Member1 = request.POST.get("mem1")
            Roll1 = request.POST.get("roll1")
            Member2 = request.POST.get("mem2")
            Roll2=request.POST.get("roll2")
            Stream=request.POST.get('stream')
            Contact=request.POST.get('number')
            Abstract=request.POST.get("abstract")

            rollcheck1=ProjectPresentation.objects.filter(roll1=Roll1)
            rollcheck2=ProjectPresentation.objects.filter(roll2=Roll1)

            if rollcheck1 or rollcheck2:
                  return render(request, "alphamain/project.html", context={"err":"Roll No Already Registered"})
            else:
                projectmodel=ProjectPresentation.objects.create(
                    projectname=Projectname,
                    stream=Stream,
                    member1=Member1,
                    roll1=Roll1,
                    member2=Member2,
                    roll2=Roll2,
                    contact=Contact,
                    abstract=Abstract
                )
                projectmodel.save()
                Pr=TotalRegistration.objects.get(eventname="Project Presentation")
                Pr.count += 1
                Pr.save()
                return render(request, "alphamain/success.html")
    return render(request, "alphamain/project.html")

def paper(request):
    if request.method == 'POST':
            Papername = request.POST.get("pname")
            Member1 = request.POST.get("mem1")
            Roll1 = request.POST.get("roll1")
            Member2 = request.POST.get("mem2")
            Roll2=request.POST.get("roll2")
            Stream=request.POST.get('stream')
            Contact=request.POST.get('number')
            Abstract=request.POST.get("abstract")

            rollcheck1=PaperPresentation.objects.filter(roll1=Roll1)
            rollcheck2=PaperPresentation.objects.filter(roll2=Roll1)
            if rollcheck1 or rollcheck2:
                  return render(request, "alphamain/paper.html", context={"err":"Roll No Already Registered"})
            else:
                projectmodel=PaperPresentation.objects.create(
                    papername=Papername,
                    stream=Stream,
                    member1=Member1,
                    roll1=Roll1,
                    member2=Member2,
                    roll2=Roll2,
                    abstract=Abstract,
                    contact=Contact
                )
                
                projectmodel.save()
                Paper=TotalRegistration.objects.get(eventname="Paper Presentation")
                Paper.count+=1
                Paper.save()
                return render(request, "alphamain/success.html")
    return render(request, "alphamain/paper.html")

def ideathon(request):
    if request.method == 'POST':
            Teamname=request.POST.get("teamname")
            Member1 = request.POST.get("mem1")
            Roll1 = request.POST.get("roll1")
            Member2 = request.POST.get("mem2")
            Roll2=request.POST.get("roll2")
            Member3 = request.POST.get("mem3")
            Roll3=request.POST.get("roll3")
            Contact=request.POST.get('number')

            rollcheck1=Ideathon.objects.filter(roll1=Roll1)
            rollcheck2=Ideathon.objects.filter(roll2=Roll1)
            if rollcheck1 or rollcheck2:
                  return render(request, "alphamain/ideathon.html", context={"err":"Roll No Already Registered"})
            ideathon=Ideathon.objects.create(
                teamname=Teamname,
                member1=Member1,
                roll1=Roll1,
                member2=Member2,
                roll2=Roll2,
                member3=Member3,
                roll3=Roll3,
                contact=Contact
            )
            ideathon.save()
            ideathon=TotalRegistration.objects.get(eventname="Ideathon")
            ideathon.count+=1
            ideathon.save()
            return render(request, "alphamain/success.html")
    return render(request, "alphamain/ideathon.html")

def product(request):
    if request.method == 'POST':
            Teamname=request.POST.get("pname")
            Member1 = request.POST.get("mem1")
            Roll1 = request.POST.get("roll1")
            Member2 = request.POST.get("mem2")
            Roll2=request.POST.get("roll2")
            abstract=request.POST.get('abstract')
            Contact=request.POST.get('contact')

            rollcheck1=Product.objects.filter(roll1=Roll1)
            rollcheck2=Product.objects.filter(roll2=Roll1)

            if rollcheck1 or rollcheck2:
                  return render(request, "alphamain/product.html", context={"err":"Roll No Already Registered"})
            else:
                pd=Product.objects.create(
                    topic=Teamname,
                    member1=Member1,
                    roll1=Roll1,
                    member2=Member2,
                    roll2=Roll2,
                    about=abstract,
                    contact=Contact
                )
                pd.save()
                product=TotalRegistration.objects.get(eventname="Product Pitching")
                product.count+=1
                product.save()
                return render(request, "alphamain/success.html")
    return render(request, "alphamain/product.html")
def totalcount(request):
     object = TotalRegistration.objects.all()
     return render(request, "alphamain/count.html", context={"events": object})
def success(request):
    return render(request, "alphamain/success.html")