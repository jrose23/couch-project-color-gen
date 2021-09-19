from django.shortcuts import render
from django.utils.crypto import get_random_string


def random_color(request):
    color_code = get_random_string(6, 'ABCDEF0123456789')

    # For future ability to save color_code user to profile
    captured_color = str(color_code)

    return render(request, 'core/random_color.html', {
        'color_code': color_code,
        'captured_color': captured_color,
    })


def custom_color(request, color):
    color_code = color.upper()

    return render(request, 'core/random_color.html', {'color_code': color_code})
