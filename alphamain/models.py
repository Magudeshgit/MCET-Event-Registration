from django.db import models

class Events(models.Model):
    events=models.CharField(max_length=50)
    description = models.TextField()
    datetime = models.DateField()
    def __str__(self):
        return self.events
    
class slots(models.Model):
    slotname=models.CharField(max_length=50)
    description= models.CharField(max_length=50)
    def __str__(self):
        return self.slotname
    
class studentlist(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    event1 = models.CharField(max_length=50)
    event2 = models.CharField(max_length=50)
    event3 = models.CharField(max_length=50)
    event4 = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class ProjectPresentation(models.Model):
    projectname=models.CharField(max_length=100)
    member1=models.CharField(max_length=50)
    roll1=models.CharField(max_length=20, blank=True)
    member2=models.CharField(max_length=50)
    roll2=models.CharField(max_length=20, blank=True)
    stream=models.CharField(max_length=20, blank=True)
    abstract=models.TextField()
    #timeslot = models.OneToOneField(slots, on_delete=models.CASCADE, primary_key=False)

    def __str__(self):
        return self.projectname

class PaperPresentation(models.Model):
    papername=models.CharField(max_length=100)
    stream = models.CharField(max_length=50)
    member1=models.CharField(max_length=50)
    roll1=models.CharField(max_length=20, blank=True)
    member2=models.CharField(max_length=50)
    roll2=models.CharField(max_length=20, blank=True)
    abstract=models.TextField()
    #timeslot = models.ForeignKey(slots, on_delete=models.CASCADE)

    def __str__(self):
        return self.papername
    
class Ideathon(models.Model):
    teamname=models.CharField(max_length=50)
    member1=models.CharField(max_length=50)
    roll1=models.CharField(max_length=20, blank=True)
    member2=models.CharField(max_length=50)
    roll2=models.CharField(max_length=20, blank=True)
    member3=models.CharField(max_length=50)
    roll3=models.CharField(max_length=20, blank=True)
    contact=models.CharField(max_length=50, blank=True)
    #timeslot = models.ForeignKey(slots, on_delete=models.CASCADE, related_name="slots")
    def __str__(self):
        return self.teamname
    
class Product(models.Model):
    topic=models.CharField(max_length=50)
    member1=models.CharField(max_length=50)
    roll1=models.CharField(max_length=20, blank=True)
    member2=models.CharField(max_length=50)
    roll2=models.CharField(max_length=20, blank=True)
    about=models.TextField()
    contact=models.CharField(max_length=20)
    def __str__(self):
        return self.topic

