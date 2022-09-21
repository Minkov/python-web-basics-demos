from django101.tasks.models import Task


def get_all_tasks():
    return Task.objects \
        .order_by('id') \
        .all()
