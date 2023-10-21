from django import template

register = template.Library()

@register.filter
def page_range(value, range_size):
    value = int(value)
    start = max(1, value - range_size)
    end = min(value + range_size, value + range_size + 1)
    return range(start, end)
