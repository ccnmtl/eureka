from sprezzatura.main.models import (
    EarTrainingElementContainerPage, EarTrainingLevelPage,
    EarTrainingElementPage, pack_nav_pages
)
from wagtail.tests.utils import WagtailPageTests


class PageTest(WagtailPageTests):
    def test_ear_training_element_container_page(self):
        """Test that requests to an ear training container page
        redirect to its first child"""
        et_container = EarTrainingElementContainerPage.objects.first()
        response = self.client.get(et_container.get_url())

        self.assertRedirects(response,
                             et_container.get_first_child().get_url())

    def test_pack_nav_elements(self):
        """Tests that the pack_nav_elements function correctly marks
        active and inactive elements
        """
        test_list = EarTrainingLevelPage.objects.all()
        test_active = test_list.first()
        packed_list = pack_nav_pages(test_list, test_active)
        self.assertTrue(packed_list[0]['active'])

        for el in packed_list[1:]:
            self.assertFalse(el['active'])

    def test_ear_training_level_page(self):
        et_page = EarTrainingLevelPage.objects.first()
        response = self.client.get(et_page.get_url())

        self.assertTrue('et_level_nav' in response.context.keys())

    def test_ear_training_element_page(self):
        et_page = EarTrainingElementPage.objects.first()
        response = self.client.get(et_page.get_url())

        self.assertTrue('et_level_nav' in response.context.keys())
        self.assertTrue('et_elements_nav' in response.context.keys())
