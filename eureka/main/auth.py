from django.conf import settings
from django.contrib.auth.models import Group


class WagtailEditorMapper(object):
    """ if the user is in one of the specified wind affil groups,
        give the user Editor privileges in the Wagtail environment """

    def __init__(self):
        if not hasattr(settings, 'WIND_STAFF_MAPPER_GROUPS'):
            self.groups = []
        else:
            self.groups = settings.WIND_STAFF_MAPPER_GROUPS

    def map(self, user, affils):
        for affil in affils:
            if affil in self.groups:
                (grp, create) = Group.objects.get_or_create(name='Editor')
                user.groups.add(grp)
