from django import template

register = template.Library()


@register.simple_tag()
def contains_et_element(body_blocks):
    for block in body_blocks:
        if not hasattr(block, 'value'):
            return False
        elif hasattr(block.value, 'values') \
                and list(block.value.values())[0] == '':
            return False

    return True
