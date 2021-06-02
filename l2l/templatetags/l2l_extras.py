from django import template
import datetime

register = template.Library()

@register.filter
def l2l_dt(now):
    if isinstance(now, datetime.datetime):
        return now.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(now, str):
        return now.replace("T", " ")
    else:
        return now
