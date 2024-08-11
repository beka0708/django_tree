from django import template
from tree_menu.models import Menu

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_items': []}

    current_url = context['request'].path

    def build_menu(items, current_url):
        result = []
        for item in items:
            item_dict = {
                'name': item.name,
                'url': item.url or item.named_url,
                'children': build_menu(item.children.all(), current_url),
                'active': current_url == (item.url or item.named_url),
            }
            result.append(item_dict)
        return result

    menu_items = build_menu(menu.items.filter(parent__isnull=True), current_url)
    return {'menu_items': menu_items}
