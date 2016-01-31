from django import template
from django.utils.safestring import mark_safe
import datetime

register = template.Library()

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
    tag_name, add, remove = token.split_contents()

    if add == "''":
        add = None
    if remove == "''":
        remove = None
    return QueryStringNode(add, remove)

class QueryStringNode(template.Node):
    def __init__(self, add,remove):
        self.add = add
        self.remove = remove
        
    def render(self, context):
        p = {}
        for k, v in context["request"].GET.items():
            p[k] = v
        return get_query_string(p, self.add, self.remove, context)

def get_query_string(p, add, remove, context):
    """
    Add and remove query parameters. From `django.contrib.admin`.
    """
    # import pdb; pdb.set_trace()
    sub_cats = p.pop('sub_cat', set())
    if sub_cats:
        sub_cats = set([str(x) for x in sub_cats.split(',')])
    if add:
        sub_cats.add(get_resolved_data(add, context))
    if remove:
        sub_cats.remove(get_resolved_data(remove, context))

    qs = '&amp;'.join([u'%s=%s' % (k, v) for k, v in p.items()]).replace(' ', '%20')
    if sub_cats:
        qs = qs + '&amp;sub_cat=' + ','.join(sub_cats)
    return mark_safe('?' + qs)

def get_resolved_data(data, context):
    return str(template.Variable(data).resolve(context))

