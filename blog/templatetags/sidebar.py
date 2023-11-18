from django import template

from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def show_sidebar(count=3):
    posts = Post.objects.order_by('-views')[:count]
    return {'posts': posts}
