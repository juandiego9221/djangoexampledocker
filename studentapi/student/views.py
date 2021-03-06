from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from student.models import Student
from student.serializer import StudentSerializer

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)


@csrf_exempt
def student_list(request):
    if request.method=='GET':
        student=Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return JSONResponse(student_serializer.data)

