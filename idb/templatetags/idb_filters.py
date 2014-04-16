from django import template

register = template.Library()

@register.filter
def tab(value):
    return value.replace('\t', '\xa0\xa0\xa0\xa0')