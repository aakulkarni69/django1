from django.shortcuts import render
from django.http import HttpResponse

def check(request):
	if request.method == 'GET':
		lists =[]
		for i in range(1,21):
			lists.append(i)
		return render(request,'home.html',{'array':lists})
	elif request.method == 'POST':
		num1 = request.POST.get('number1')
		num2 = request.POST.get('number2')
		arr=[]
		if int(num1)>int(num2):
			return HttpResponse('invalid')
		else:	
			for i in range(int(num1),int(num2) + 1):
				arr.append(i)
			return render(request,'index.html',{'array':arr})

