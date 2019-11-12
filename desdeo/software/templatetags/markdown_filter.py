from django import template
from django.template.defaultfilters import stringfilter

import markdown2 as md

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extras=['fenced-code-blocks', 'sane-lists', 'cuddled-lists'])
