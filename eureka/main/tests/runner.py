"""Custom test runner to initialize test database with pages"""
from django.core.management import call_command
from django.test.runner import DiscoverRunner


class EurekaTestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        dbs = super().setup_databases(**kwargs)
        call_command('bootstrap_site_tree')
        return dbs
