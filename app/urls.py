from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import HomeView,addview,adddview
urlpatterns=[
	   path('addr/cd/',views.firstpage,name='firstpage'),
     path('addr/cd/login/',views.edu,name = 'edu'),
     path('addr/cd/login/add/',views.educrev,name='educrev'),
     path('addr/cd/login/next/',views.EducationView.as_view(),name='education'),
     path ('addr/cd/login/next/<int:pk>',views.UpdatepostView.as_view(), name='updateview'),
     path('addr/cd/login/next/save/',views.job345, name='job345'),
     path('addr/cd/login/next/save/job/',views.JobView.as_view(),name='job'),
     path ('addr/cd/login/next/save/job/<int:pk>',views.UpdatepostViewjob.as_view(), name='updateviewjob'),
     path ('addr/cd/login/next/save/job/<int:pk>/delete/',views.Deletepostviewjob.as_view(), name='deleteviewjob'),
     path('check',views.formfunction),
     path ('addr/cd/login/next/<int:pk>/delete/',views.Deletepostview.as_view(), name='deleteview'),
     

     path('addr/cd/login/next/job/skill/',views.addonstest,name='extra'),#Tejaswini
     path('addr/cd/login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='addonemoreaddon'),
     path('addr/cd/login/next/job/skill/fieldadd/',views.ExtrafieldView.as_view(),name='extrafi'),
     path ('addr/cd/login/next/job/skill/fieldadd/<int:pk>',views.UpdateEFView.as_view(), name='updateviewef'),
     path ('addr/cd/login/next/job/skill/fieldadd/<int:pk>/delete/',views.DeleteEFview.as_view(), name='deleteviewef'),
     path('addr/cd/login/next/job/skill/final/',views.home,name='home1'),#Tejaswini




      #BELOW URLS ADDED BY SIRI.

         #path('login/back/',views.backopt,name='backopt'),
     path('addr/cd/login/next/skills/',views.skilledu,name='skillsedu'),
         # path('login/next/add/',views.jobadd,name='jobadd'),
     path('addr/cd/login/next/skills/add',views.skillseducrev,name='skillseducrev'),
     path('addr/cd/login/next/skills/next/',views.SkillsView.as_view(),name='skillsview'),
     path('addr/cd/login/next/skills/next/<int:pk>',views.skillUpdatepostView.as_view(),name='skillsupdateview'),
         #path ('login/next/job/<int:pk>',views.UpdatepostView.as_view(), name='updateview'),
     path ('addr/cd/cd/login/next/skills/next/<int:pk>/delete/',views.skillDeletepostview.as_view(), name='skillsdeleteview'),

         #path('login/next/job/skill/',views.addonstest,name='home'),
         #path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
         #path('login/next/job/skill/next/fieldadd/',views.home,name='home'),
     path('addr/cd/login/next/job/skill/next/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),

          #path('login/back/',views.backopt,name='backopt'),
          #path('login/next/job/',views.skillsfun,name='skillfun'),
          #path('login/next/add/',views.jobadd,name='jobadd'),
          #path('login/next/job/add/',views.skillsadd,name='skillfun'),
          #path('login/next/job/skill/',views.addons,name='home'),
          #path('login/next/job/skill/',views.addonstest,name='home'),
          #path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
          #path('login/next/job/skill/fieldadd/',views.home,name='home'),
          #path('login/next/job/skill/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),
          #chichaa code
      path('',HomeView.as_view(),name="home"),
      path('addr',addview.as_view(),name='addresume'),
      path('addr/addd',adddview.as_view(),name='adddetails'),



      path('check2',views.homer,name='mainpage'),

      
]