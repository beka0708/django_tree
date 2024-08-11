from django.shortcuts import render, get_object_or_404
from tree_menu.models import Menu


def menu_view(request, menu_name):
    menu = get_object_or_404(Menu, name=menu_name)
    context = {
        'menu_name': menu_name,
        'menu': menu,
    }
    return render(request, 'tree_menu/menu_page.html', context)
