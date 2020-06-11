from django.core.management.base import (
    BaseCommand, CommandError
)
from sprezzatura.main.models import (
    HomePage, ImprovisationTypeIndexPage, ImprovisationTypePage,
    EarTrainingIndexPage, EarTrainingLevelPage,
    EarTrainingElementContainerPage, EarTrainingElementPage,
    ImprovisationCombinationIndexPage, ImprovisationCombinationPage
)
from wagtail.core.models import Page, Site
from wagtail.core.rich_text import RichText

IMPROV_TYPE_LIST = [
    'Landscaping', 'Arithmetic', 'Patterning', 'Call and Response',
    'Rhythm', 'Change', 'Smorgasboard'
]


def create_ear_training_elements(et_root_page, element_list):
    # Nested function so that it has access to the models
    for el in element_list:
        element_container = EarTrainingElementContainerPage(
            title=el
        )
        et_root_page.add_child(instance=element_container)
        element_container.save_revision().publish()

        for improv_type in IMPROV_TYPE_LIST:
            imp_type_page = EarTrainingElementPage(
                title='{} with {}'.format(el, improv_type),
                body=[('rich_text', RichText('<p>TBD</p>'))]
            )
            element_container.add_child(instance=imp_type_page)
            imp_type_page.save_revision().publish()


class Command(BaseCommand):
    """Build out the basic site tree"""
    def handle(self, *args, **options):
        if Page.objects.count() > 2:
            raise CommandError('There already exists content in the database.')

        # Delete the existing 'Welcome to Wagtail' page, create homepage
        Page.objects.get(id=2).delete()
        Site.objects.all().delete()

        root = Page.objects.get(id=1)
        homepage = HomePage(title='Sprezzatura')
        root.add_child(instance=homepage)
        homepage.save_revision().publish()

        Site.objects.create(
            hostname='localhost',
            root_page_id=homepage.id,
            is_default_site=True
        )

        # Improv Type Index
        improv_type_index = ImprovisationTypeIndexPage(
            title='Improvisation Types'
        )
        homepage.add_child(instance=improv_type_index)
        improv_type_index.save_revision().publish()

        # Improv Types
        for improv_type in IMPROV_TYPE_LIST:
            improv_type_page = ImprovisationTypePage(
                title=improv_type,
                body=[('rich_text', RichText('<p>TBD</p>'))]
            )
            improv_type_index.add_child(instance=improv_type_page)
            improv_type_page.save_revision().publish()

        # Ear training
        ear_training_index = EarTrainingIndexPage(
            title='Ear Training'
        )
        homepage.add_child(instance=ear_training_index)
        ear_training_index.save_revision().publish()

        # ET 1
        et_one = EarTrainingLevelPage(
            title='Introduction to Ear Training One',
            body=[('rich_text', RichText('<p>TBD</p>'))]
        )
        ear_training_index.add_child(instance=et_one)
        et_one.save_revision().publish()

        et_one_elements = [
            'Tempo', 'Dynamics', 'Texture', 'Meter', 'Rhythm', 'Scales',
            'Interval', 'Melody', 'Triads'
        ]
        create_ear_training_elements(et_one, et_one_elements)

        # ET 2
        et_two = EarTrainingLevelPage(
            title='Introduction to Ear Training Two',
            body=[('rich_text', RichText('<p>TBD</p>'))]
        )
        ear_training_index.add_child(instance=et_two)
        et_two.save_revision().publish()

        et_two_elements = [
            'Tempo', 'Dynamics', 'Meter', 'Rhythm', 'Scales',
            'Interval', 'Melody', 'Triads'
        ]
        create_ear_training_elements(et_two, et_two_elements)

        # ET 3
        et_three = EarTrainingLevelPage(
            title='Introduction to Ear Training Three',
            body=[('rich_text', RichText('<p>TBD</p>'))]
        )
        ear_training_index.add_child(instance=et_three)
        et_three.save_revision().publish()

        et_three_elements = [
            'Tempo', 'Meter', 'Rhythm', 'Scales',
            'Interval', 'Melody', 'Triads'
        ]
        create_ear_training_elements(et_three, et_three_elements)

        # ET 4
        et_four = EarTrainingLevelPage(
            title='Introduction to Ear Training Four',
            body=[('rich_text', RichText('<p>TBD</p>'))]
        )
        ear_training_index.add_child(instance=et_four)
        et_four.save_revision().publish()

        et_four_elements = [
            'Tempo', 'Meter', 'Rhythm', 'Scales',
            'Interval', 'Melody', 'Triads'
        ]
        create_ear_training_elements(et_four, et_four_elements)

        # Improv combinations
        improv_combo_index = ImprovisationCombinationIndexPage(
            title='Improvisation Combinations'
        )
        homepage.add_child(instance=improv_combo_index)
        improv_combo_index.save_revision().publish()

        improv_combos = [
            'Beginins Layering', 'Intermediate Layering', 'Advanced Layering']
        for i in improv_combos:
            combo_page = ImprovisationCombinationPage(
                title=i,
                body=[('rich_text', RichText('<p>TBD</p>'))]
            )
            improv_combo_index.add_child(instance=combo_page)
            combo_page.save_revision().publish()
