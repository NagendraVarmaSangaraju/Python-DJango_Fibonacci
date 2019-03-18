from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from app.models import Fibonacci
from django.views import View
import time
def fibonacci(number):
    if number < 2:
        return 1
    
    else:
        number_1 = 1
        number_2 = 1

        for number in range(2, number):
            num = number_1 + number_2
            number_1 = number_2
            number_2 = num
        
        return number_2

class FibonacciAPIView(View):

	def get(self, request):
		value = request.GET.get('value')
		if value is None:
			return render(request, 'index.html')
		else:
			start_time = time.time()
			number = int(value)
			result = fibonacci(number)
			end_time = time.time() - start_time
			latency = str(end_time)[0:4]
			fibonacci_qs = Fibonacci.objects.create(
                                    number=number, 
                                    result=result, 
                                    latency=latency
                                )
			fibonacci_qs.save()
			n = number % 10
			data = {
            
			    'number':number,
                'result':result, 
                'latency':latency,
				'n' : n

            }
			return render(request, 'index.html', data)
