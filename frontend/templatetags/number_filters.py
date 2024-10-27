from django import template

register = template.Library()

@register.filter(name='convert_to_bangla')
def convert_to_bangla(value):
    # English to Bangla number mapping
    bangla_digits = {
        '0': '০',
        '1': '১',
        '2': '২',
        '3': '৩',
        '4': '৪',
        '5': '৫',
        '6': '৬',
        '7': '৭',
        '8': '৮',
        '9': '৯',
    }
    
    # Convert each digit
    return ''.join(bangla_digits.get(c, c) for c in str(value))
