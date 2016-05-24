# -*- coding:utf-8 -*-

from __future__ import unicode_literals

import datetime

from django.http import HttpResponse, JsonResponse

from polls.models import Question

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    questions = Question.objects.all()
    html = []
    for question in questions:
        line = "%d: %s <br>" % (question.id, question)
        html.append(line)

    return HttpResponse(''.join(html))


def add_question(request):
    data = {
        'msg': 'hello api!!!',
        'status': 'ok',
    }
    request_dict = request.GET
    question_text = request_dict.get('question_text')
    if question_text:
        question = Question(
            question_text=question_text,
            pub_date=datetime.datetime.now())
        question.save()
        msg = '存储了 %s' % (question)
    else:
        msg = 'question_text 参数没有传入数据'
        data['status'] = 'error'

    data['msg'] = msg

    return JsonResponse(data)
