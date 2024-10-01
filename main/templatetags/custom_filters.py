from django import template

register = template.Library()


@register.filter
def truncate_words(value, max_length=100):
    if len(value) <= max_length:
        return value
    truncated_value = value[:max_length].rsplit(" ", 1)[0]
    return f"{truncated_value}..."
