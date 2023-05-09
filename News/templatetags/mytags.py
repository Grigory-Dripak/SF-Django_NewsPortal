from django import template


register = template.Library()


@register.simple_tag()
def hrefcreate(href='http://127.0.0.1:8000/news/', value=''):
   return f'{href}{value}'