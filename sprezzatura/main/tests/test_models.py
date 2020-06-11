from django.core.management import call_command
from sprezzatura.main.models import (
    EarTrainingElementContainerPage, EarTrainingLevelPage,
    EarTrainingElementPage
)
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

        self.assertRedirects(response,
                             et_container.get_first_child().get_url())

    def test_ear_training_level_page(self):
        et_page = EarTrainingLevelPage.objects.first()
        response = self.client.get(et_page.get_url())

        self.assertTrue('et_level_nav' in response.context.keys())

    def test_ear_training_element_page(self):
        et_page = EarTrainingElementPage.objects.first()
        response = self.client.get(et_page.get_url())

        self.assertTrue('et_level_nav' in response.context.keys())
        self.assertTrue('et_elements_nav' in response.context.keys())
