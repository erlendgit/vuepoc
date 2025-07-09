import json

from django import template
from django.utils.safestring import mark_safe

from core.models import ContentType

register = template.Library()


@register.simple_tag()
def load_site_content_types_json():
    return mark_safe(json.dumps([t.key for t in ContentType.objects.all()]))


@register.simple_tag()
def load_site_groups_for_select():
    from core.models import Group

    response = Group.objects.all().values_list("id", "name")
    return [(str(id), name) for id, name in response]