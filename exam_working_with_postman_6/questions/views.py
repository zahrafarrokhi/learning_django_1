import json
import random

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from questions.models import Questions,Exam,Answers

# # Create your views here.

# postman
# python manage.py runserver
# GET  http://127.0.0.1:8000/questions/ send
# hello
# def index(requset):
#     return HttpResponse("hello")

User = get_user_model()

@csrf_exempt
def login_page(requset):
    if requset.method == 'POST':
        print(requset.POST)
        # form-data
        # data = requset.POST
        data = json.loads(requset.body)
        # usename = data.get('usename',None)
        # password = data.get('password',None)
        user = authenticate(username = data['username'],password = data['password'])
        if not user:
            return HttpResponse("error!")
        else:
            login(requset, user)
            return HttpResponse("sucess!")
    return JsonResponse("hhh")
# python manage.py runserver
# python manage.py createsuperuser
# yasaman
# 1234yasaman    
# postman
# python manage.py runserver
# POST http://127.0.0.1:8000/questions/login/ send
# body/raw
# {
#         "username":"yasaman",
#         "password":"1234yasaman"
#     }
# sucess!
@csrf_exempt
def register(requset):
    if requset.method == 'POST':
        print(requset.POST)
        # data = requset.POST
        data = json.loads(requset.body)
        if len(data['password']) < 8:
            return HttpResponse("short password!")
           
        try:
            user_obj = User.objects.create_user(data['username'],data['password'])
            user_obj.save()
            return HttpResponse(user_obj)
            
        except :
            return HttpResponse("username should be unique!")
# postman
# python manage.py runserver
# POST  http://127.0.0.1:8000/questions/register send
# body/raw 
# {
        # "username":"nasim",
        # "password":"1234yasiiiii"
    # }
# nasim

@csrf_exempt
def whoami(requset):
    return HttpResponse([requset.user])

# postmam test
# python manage.py runserver
# POST http://127.0.0.1:8000/questions/whoami send
# yasaman

# ********
# *********
# add=>POST
# list=>GET
# answer question=>POST
# show result of exam =>GET

# ***************
@csrf_exempt
def add_question(requset):
   if requset.method == 'POST':
       data = json.loads(requset.body)
       try:
            question_obj = Questions.objects.create(text=data.get('text',None),
            correct_answer=data.get('correct_answer',None),a=data.get('a',None), 
            b=data.get('b',None),c= data.get('c',None),d=data.get('d',None))
 
       except :
            return JsonResponse({"message":"bad input"})

   question_obj.save()  
   return JsonResponse({"message":"question added"})

# postman
# python manage.py runserver
# POST http://127.0.0.1:8000/questions/add/ send
# body/raw
# {

#     "text":"فاصله زمین تا خورشید چقدر است?",
#     "correct_answer":"a",
#     "a":"91مایل",
#     "b":"100مایل",
#     "c":"300مایل",
#     "d":"50مایل"
# }
# result
# {
#     "message": "question added"
# }
# *******************************************************
# for fk relations(Question has fk for Exam)
# class Questions(models.Model):
      # exam = models.ForeignKey(Exam,on_delete = models.CASCADE)  
# def exam_list(request):
#     if request.method == 'GET':
#         exams = Exam.objects.all()
#         result =[]
#         for exam in exams:
#              result.append(
#             {
#                 'name': exam.name,
#                 'url': reverse('question-list', args=[exam.pk])
#             }
#             )

#     return JsonResponse({'result': result})
# postman
# python manage.py runserver
# GET http://127.0.0.1:8000/questions/exam-list/ send
# def question_list(request,id):
#     if request.method == 'GET':
#         exam = Exam.objects.get(id=id)
#         questions = exam.questions.all()
#         result =[]
#         for question in questions:
#             result.append ({

#                 'text':question.text,
#                 'a' : question .a,
#                 'b' : question .b,
#                 'c' : question .c,
#                 'd' : question .d,

#             })
#     else:
#         return JsonResponse({"cant show "})


#     return JsonResponse({'data': result},safe=False)
# postman
# python manage.py runserver
# GET http://127.0.0.1:8000/questions/show/1 send
# ********************************************
  # random.sample must be a sequence or set. For dicts, use list(Dict).
        # postman
        # Exception Type:	TypeError
        # Population must be a sequence.  For dicts or sets, use sorted(d).

        # for i in range(11):
        #     questions_list = random.choice(questions)
@login_required
@csrf_exempt
def question_list_view(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        questions_list = random.sample(list(questions), k=3)
        # Exam.objects.all().delete()
    
        exam, created = Exam.objects.get_or_create(user=request.user,status=True)
        if created :
            for ques in questions_list:
                exam.questions.add(ques)
        # exam.save()
       
        result =[]
        for question in exam.questions.all():
            result.append ({
                
                'text':question.text,
                'a' : question.a,
                'b' : question.b,
                'c' : question.c,
                'd' : question.d,
                'id' : question.id,

            })
        return JsonResponse({'data': result},safe=False)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        print('dsvbfdsbfdbfdbfsdbsf')
        d = data.get('data')
     
        exam_obj = get_object_or_404(Exam, user=request.user,status=True)
        for answer_item in d:
          
            question = get_object_or_404(Questions, id=answer_item.get('question_id'))
            answer,created = Answers.objects.get_or_create(exam=exam_obj,question=question,answer=answer_item.get('answer') )

        exam_obj.status =False
        exam_obj.save()
        return JsonResponse({'result': 'success'})
    
    
# postman
# python manage.py runserver
# GET http://127.0.0.1:8000/questions/question-list send

@csrf_exempt 
def answer_questions(request):
   
       
    return JsonResponse({'answers question':''})    
# postman
# python manage.py runserver
# GET http://127.0.0.1:8000/questions/questioanswer_questions send

# {
#     "data": [
#         {
#             "text": "فاصله زمین تا خورشید چقدر است?",
#             "a": "91مایل",
#             "b": "100مایل",
#             "c": "300مایل",
#             "d": "50مایل",
#             "id": 1
#         },
#         {
#             "text": "فاصله زمین llllتا خورشید چقدر است?",
#             "a": "91مایل",
#             "b": "100مایل",
#             "c": "300مایل",
#             "d": "50مایل",
#             "id": 2
#         },
#         {
#             "text": "فkاklصkلoهkkk ;lll,زم55ین llllتا ;;;خورشید l,چقدر است?",
#             "a": "91mmmمایل",
#             "b": "10,,0مایل",
#             "c": "300مایل",
#             "d": "50مایل",
#             "id": 15
#         }
#     ]
# }

# {
#     "data": [
#         {
#             "question_id": 4,
#             "answer": "a"
#         }
#     ]
# }

@csrf_exempt 
def show_result_of_exam(request):
    if request.method == 'POST':
        
        
        answer = Answers.objects.all()
    return JsonResponse({'answers question'})      


    
