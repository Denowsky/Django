from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger(__name__)

html = [
    """
<h1>Главная</h1>
<h2>Мой первый Django-сайт</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla fugit quas repellendus doloribus totam pariatur
    alias sint dignissimos laboriosam vitae beatae iure laborum, culpa et non commodi odit placeat explicabo optio.
    Laborum vel quidem doloribus consequatur repellat ea rem consequuntur, officia sequi incidunt voluptatem tenetur
    accusantium similique, quam officiis iste. Ratione aut vero, fugit autem quia cupiditate sunt. Esse laboriosam,
    delectus non consequuntur velit, facilis voluptatum illum harum commodi soluta eum placeat, dolores nisi
    incidunt unde ab atque. Eos aut quam optio, illo, qui accusamus natus magnam praesentium possimus id incidunt!
    Harum soluta sequi molestiae quasi iste, accusamus nostrum molestias!</p>
<a href="/about/">Обо мне</a>
""",
    """
<h1>Обо мне</h1>
<h2>Информация обо мне</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nulla fugit quas repellendus doloribus totam pariatur
    alias sint dignissimos laboriosam vitae beatae iure laborum, culpa et non commodi odit placeat explicabo optio.
    Laborum vel quidem doloribus consequatur repellat ea rem consequuntur, officia sequi incidunt voluptatem tenetur
    accusantium similique, quam officiis iste. Ratione aut vero, fugit autem quia cupiditate sunt. Esse laboriosam,
    delectus non consequuntur velit, facilis voluptatum illum harum commodi soluta eum placeat, dolores nisi
    incidunt unde ab atque. Eos aut quam optio, illo, qui accusamus natus magnam praesentium possimus id incidunt!
    Harum soluta sequi molestiae quasi iste, accusamus nostrum molestias!</p>
<a href="/">Вернуться на главную</a>
"""
]


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(html[0])


def about(request):
    logger.info('About page accessed')
    return HttpResponse(html[1])
