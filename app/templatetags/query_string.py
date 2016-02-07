from django import template
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

@register.simple_tag(takes_context=True)
def current_qs(context):
    return to_query_string(context["request"].GET)

@register.tag
def query_string(parser, token):
    """
    Allows you too manipulate the query string of a page by adding and removing keywords.
    If a given value is a context variable it will resolve it.
    Based on similiar snippet by user "dnordberg".
    
    requires you to add:
    
    TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    )
    
    to your django settings. 
    
    Usage:
    http://www.url.com/{% query_string "param_to_add=value, param_to_add=value" "param_to_remove, params_to_remove" %}
    
    Example:
    http://www.url.com/{% query_string "" "filter" %}filter={{new_filter}}
    http://www.url.com/{% query_string "page=page_obj.number" "sort" %} 
    
    """
    tag_name, name, add, remove = token.split_contents()

    if add == "''":
        add = None
    if remove == "''":
        remove = None
    return QueryStringNode(name, add, remove)

class QueryStringNode(template.Node):

    def __init__(self, name, add,remove):

        self.name = name
        self.add = add
        self.remove = remove
        
    def render(self, context):
        p = {}
        for k, v in context["request"].GET.items():
            p[k] = v
        return get_query_string(p, self.name, self.add, self.remove, context)

def get_query_string(p, name, add, remove, context):
    """
    Add and remove query parameters. From `django.contrib.admin`.
    """
    new_qs = p.pop(name, set())

    if new_qs:
        new_qs = set([str(x) for x in new_qs.split(',')])
    else:
        new_qs = set()

    if add:
        new_qs.add(get_resolved_data(add, context))
    if remove:
        try:
            new_qs.remove(get_resolved_data(remove, context))
        except KeyError:
            pass

    qs = to_query_string(p)

    if new_qs:
        qs = qs + '&amp;{}='.format(name) + ','.join(new_qs)
    return mark_safe('?' + qs)

def to_query_string(items):
    return '&amp;'.join([u'%s=%s' % (k, v) for k, v in items.items()]).replace(' ', '%20')

def get_resolved_data(data, context):
    return str(template.Variable(data).resolve(context))

