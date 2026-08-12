from django import template

register = template.Library()


@register.filter
def price_format(value):
    """
    Format price with thousands separator.
    Example:
    1500000 -> 1,500,000
    2500000.00 -> 2,500,000
    """

    if value is None:
        return ""

    try:
        value = int(value)
        return f"{value:,}"
    except (ValueError, TypeError):
        return value