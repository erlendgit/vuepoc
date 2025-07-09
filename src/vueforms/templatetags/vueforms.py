from django import template

register = template.Library()


@register.simple_tag
def vue_url():
    return "https://unpkg.com/vue@3/dist/vue.global.js"


@register.filter
def as_json_string(value):
    import json

    return json.dumps(value, ensure_ascii=False)
