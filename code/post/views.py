from django.shortcuts import render
from django.views import View
from string import ascii_letters
from random import choice

class AnyDataView(View):
    """Представление создающее какие-то данные"""
    def get(self, request):
        """Метод обработки GET метода"""
        template = 'post/main.html'
        data = []
        for i in range(10):
            value = ''.join([choice(ascii_letters) for _ in range(10)])
            data.append(value)
        context = {
            'data': data
        }
        return render(request, template, context)