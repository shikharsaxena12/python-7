from django.shortcuts import render
from .models import cal_history

def cal(request):
    result = None
    if request.method == 'POST':
        num1_raw = request.POST.get('num1')
        num2_raw = request.POST.get('num2')
        op = request.POST.get('op')
        try:
            num1 = float(num1_raw)
            num2 = float(num2_raw)

            if op == 'add':
                result = num1 + num2
            elif op == 'sub':
                result = num1 - num2
            elif op == 'mul':
                result = num1 * num2
            elif op == 'div':
                result = num1 / num2
            elif op == 'floordiv':
                result = num1 // num2
            else:
                result = 'Invalid'
        except:
            result = 'Invalid'

        if result != 'Invalid' and op in {'add', 'sub', 'mul', 'div', 'floordiv'}:
            cal_history.objects.create(
                num1=str(num1_raw),
                num2=str(num2_raw),
                op=op,
                result=str(result)
            )

    return render(request, 'Calcutator.html', {'result': result})


def history(request):
    records = cal_history.objects.order_by('-Created_at')
    return render(request, 'Calcutator_history.html', {'records': records})
