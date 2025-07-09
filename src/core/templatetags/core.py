from django import template

register = template.Library()


@register.simple_tag(name="define")
def pass_trough_value(value):
    """
    A simple template tag that returns the value passed to it.
    This can be used to define variables in templates.
    """
    return value