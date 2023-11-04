from django.contrib import admin
from .models import (Events,studentlist, 
                     ProjectPresentation, 
                     Ideathon,
                     PaperPresentation,TotalRegistration,Product
)
from import_export.admin import ExportActionMixin   


class EventAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('events','description','datetime')

class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name','rollno','dept','year','event1','event2','event3','event4')
#Project Presentation
class ProjectPresenterIT(ExportActionMixin, admin.ModelAdmin):
    list_display = ('projectname','stream','member1','roll1','member2','abstract', 'contact')
# Paper Presentation
class PaperPresenterIT(ExportActionMixin, admin.ModelAdmin):
    list_display = ('papername','member1','roll1','member2','abstract','contact')
#ProjectPitch & Ideathon
class Ideathon_ad(ExportActionMixin, admin.ModelAdmin):
    list_display = ('member1','roll1','member2','roll2','member3','roll3', 'contact')

class Product_ad(ExportActionMixin, admin.ModelAdmin):
    list_display=('topic', 'member1', 'roll1','member2', 'roll2','contact')

#Admin Registration
admin.site.register(Events,EventAdmin)
admin.site.register(studentlist,StudentAdmin)
admin.site.register(TotalRegistration)
#Events
admin.site.register(ProjectPresentation,ProjectPresenterIT)
#paper
admin.site.register(PaperPresentation,PaperPresenterIT)
#Common Events
admin.site.register(Ideathon, Ideathon_ad)
admin.site.register(Product, Product_ad)
