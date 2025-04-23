from django.contrib.auth.decorators import user_passes_test



def group_required(group_name):
    """
    Decorator to check if the user belongs to a specific group.
    """
    def in_group(user):
        if user.is_superuser:
            return True
        
        for group in group_name:
            if user.groups.filter(name=group).exists():
                return True

    return user_passes_test(in_group, login_url='home')


admin_required = group_required(['admin'])
editor_required = group_required(['editor','admin'])
author_required = group_required(['author','editor','admin'])