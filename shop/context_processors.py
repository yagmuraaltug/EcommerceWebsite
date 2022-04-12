from sympy import im
from .models import Category


def menu_categories(request):
    categories = Category.objects.filter(parent=None)
    return{'categories' : categories}

