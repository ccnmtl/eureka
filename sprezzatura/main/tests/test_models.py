from django.core.management import call_command
from sprezzatura.main.models import EarTrainingElementContainerPage
from wagtail.tests.utils import WagtailPageTests


class PageTest(WagtailPageTests):
    @classmethod
    def setUpTestData(cls):
        call_command('bootstrap_site_tree')

    def test_ear_training_element_container_page(self):
        """Test that requests to an ear training container page
        redirect to its first child"""
        et_container = EarTrainingElementContainerPage.objects.first()
        response = self.client.get(et_container.get_url())

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         et_container.get_first_child().get_url())
