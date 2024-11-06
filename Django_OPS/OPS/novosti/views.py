from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, History, Category, Tag
from django.http import HttpResponse
from django.template import loader
import math
import random

def solve_quadratic(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = request.GET.get('c', 0)

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return render(request, 'index.html', {'error': 'Неверный ввод. Пожалуйста, введите числовые значения для a, b и c.'})

    equation = f'{a}x^2 + {b}x + {c} = 0'
    solution = ''

    if a == 0:
        if b == 0:
            if c == 0:
                solution = 'Бесконечное количество решений'
            else:
                solution = 'Нет решений'
        else:
            x = -c / b
            solution = f'x = {x}'
    else:
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКорни: x1 = {x1}, x2 = {x2}'
        elif discriminant == 0:
            x = -b / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКорень: x = {x}'
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            solution = f'\nДискриминант: D = b^2 - 4ac = {discriminant}\n\nКомплексные корни: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i'

    return render(request, 'index.html', {'equation': equation, 'solution': solution})

# Функция для рандома и тренажёра
def generate_quadratic_equation():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c

def quadratic_trainer(request):
    if request.method == 'POST':
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        c = float(request.POST.get('c'))
        user_solution = request.POST.get('solution')

        # Решение уравнения
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = round((-b + discriminant**0.5) / (2*a), 2)
            x2 = round((-b - discriminant**0.5) / (2*a), 2)
            if (float(user_solution.split(',')[0]) == x1 and float(user_solution.split(',')[1]) == x2) or (float(user_solution.split(',')[0]) == x2 and float(user_solution.split(',')[1]) == x1):
                correct_solution = f'x1 = {x1}, x2 = {x2}\n\nОтвет правильный!'
            else: correct_solution = f'x1 = {x1}, x2 = {x2}\n\nОтвет неверный...'
        elif discriminant == 0:
            x = round(-b / (2*a), 2)
            if float(user_solution.split(',')[0]) == x:
                correct_solution = f'x = {x}\n\nОтвет правильный!'
            else: correct_solution = f'x = {x}\n\nОтвет неверный...'
        else:
            real_part = round(-b / (2*a), 2)
            imaginary_part = round((abs(discriminant)**0.5) / (2*a), 2)
            correct_solution = f'x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i'

        # Сохранение в базу данных
        history = History(
            a=a,
            b=b,
            c=c,
            user_solution=user_solution,
            correct_solution=correct_solution
        )
        history.save()

        return render(request, 'trinager.html', {
            'a': a,
            'b': b,
            'c': c,
            'user_solution': user_solution,
            'correct_solution': correct_solution,
            'history': History.objects.all().order_by('-timestamp')
        })

    a, b, c = generate_quadratic_equation()
    return render(request, 'trinager.html', {'a': a, 'b': b, 'c': c})


def home(request):
    return render(request, 'home.html')

def news_list(request):
    news_list = News.objects.all().order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # По 4 новости на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'page_obj': page_obj})


def news_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_list = News.objects.filter(category=category).order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # По 4 новости на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'page_obj': page_obj, 'category': category})

def news_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    news_list = News.objects.filter(tags=tag).order_by('-pub_date')
    paginator = Paginator(news_list, 4)  # По 4 новости на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'page_obj': page_obj, 'tag': tag})