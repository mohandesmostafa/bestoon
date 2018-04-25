from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import Token, Expense, User, Income
from datetime import datetime
# Create your views here.


@csrf_exempt
def submit_income(request):
    """user sabmit an income"""

    #TODO: validate data. user might be fake. token might be fake. amount might be fake
    this_token = request.POST['token']
#    this_token = request.POST[Token]
    this_user = User.objects.filter(token__token=this_token).get()
#    now = datetime.now()  # TODO: user might want to submit the date herself
    if 'date' not in request.POST:
        date = datetime.now()
#    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    i = Income(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    i.save()

#    print('we are here')
#    print(request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)




@csrf_exempt
def submit_expense(request):
    """user sabmit an expense"""

    #TODO: validate data. user might be fake. token might be fake. amount might be fake
    this_token = request.POST['token']
#    this_token = request.POST[Token]
    this_user = User.objects.filter(token__token=this_token).get()
#    now = datetime.now()  # TODO: user might want to submit the date herself
    if 'date' not in request.POST:
        date = datetime.now()
#    Expense.objects.create(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    e = Expense(user=this_user, amount=request.POST['amount'], text=request.POST['text'], date=date)
    e.save()

#    print('we are here')
#    print(request.POST)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)
