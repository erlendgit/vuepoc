from django import template

register = template.Library()


@register.simple_tag(name="define")
def pass_trough_value(value):
    return value
