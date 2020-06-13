from django.core.management import call_command
from sprezzatura.main.models import (
    HomePage, ImprovisationTypeIndexPage, ImprovisationTypePage,
    EarTrainingIndexPage, EarTrainingLevelPage,
    EarTrainingElementPage, ImprovisationCombinationIndexPage,
    ImprovisationCombinationPage
)
from wagtail.tests.utils import WagtailPageTests


class ViewTest(WagtailPageTests):
    """These test check that the page can be routed and can
    render templates cleanly"""
    def test_smoketest(self):
        response = self.client.get('/smoketest/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'PASS')

    def test_home_page(self):
        page = HomePage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_improvisation_type_index_page(self):
        page = ImprovisationTypeIndexPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_improvisation_type_page(self):
        page = ImprovisationTypePage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_ear_training_index_page(self):
        page = EarTrainingIndexPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_ear_training_level_page(self):
        page = EarTrainingLevelPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_ear_training_element_page(self):
        page = EarTrainingElementPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_improvisation_combination_index_page(self):
        page = ImprovisationCombinationIndexPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)

    def test_improvisation_combination_page(self):
        page = ImprovisationCombinationPage.objects.first()
        response = self.client.get(page.get_url())
        self.assertEquals(response.status_code, 200)
