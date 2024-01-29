from django import template

register = template.Library()


@register.inclusion_tag("tags/profile_avatar.html", takes_context=True)
def profile_avatar(context):
    print(context)
    # Return `context`, much like in `View`s
    user = context.request.user
    initials = \
        user.first_name[0] + user.last_name[0] \
            if user.is_authenticated \
            else "AN"

    return {
        "user_fullname": initials,
    }
