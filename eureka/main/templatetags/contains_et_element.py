from django import template

register = template.Library()


@register.simple_tag()
def contains_et_element(body_blocks):
    return any([True for block in body_blocks if hasattr(block, 'value')])
