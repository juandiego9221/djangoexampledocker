from django.conf.urls import url
from student import views

urlpatterns=[
    url(r'^student/$',views.student_list),
]

