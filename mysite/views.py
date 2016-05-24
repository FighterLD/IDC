# -*- coding:utf-8 -*-
import datatime

from django.http import HttpResponse

from pools.models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_question(request):
    data = {
        'msg': 'hello api!!!',
        'status': 'ok',
    }

    print request.GET

    question = Question(
        question_text = '下一届总统是谁呢？',
        pub_data=datatime.datatime.now()
    )
    question.save()

    return JsonResponse(data)
