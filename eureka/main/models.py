from django.http import Http404
from django.db import models
from django.shortcuts import redirect
from eureka.main.blocks import (
    EarTrainingElementBlock, ImageBlock, AccessibleTextBlock, VideoEmbedBlock
)
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.blocks import (
    RichTextBlock
)
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_panel


def pack_nav_pages(page_list, active_page):
    """This takes a list of pages and an active page, and returns a list
    of type {'page': SubclassedPage, 'active': Bool}
    This is used to build lists of links for navigation elements where the
    link for one of these pages needs to be marked active so that it can
    be represented differently on the front end.

    NOTE: the items in page_list and page must be of the same type
    """
    return [
        {
            'page': el,
            'active': True if el == active_page else False
        } for el in page_list
    ]


class HomePage(Page, MenuPageMixin):
    home_page_link = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Homepage"

    content_panels = Page.content_panels + [
       PageChooserPanel('home_page_link')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['wagtailcore.Page']
    max_count = 1


class BasicPage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock(features=[
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
            'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed'
        ])),
        ('image', ImageBlock()),
        ('video', VideoEmbedBlock(required=False))
    ], use_json_field=True)

    class Meta:
        verbose_name = "Basic Page"

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]


# Improv Types
class ImprovisationTypeIndexPage(Page, MenuPageMixin):
    def serve(self, request):
        """Override to redirect to child page"""
        child = self.get_first_child()
        if child:
            return redirect(
                child.get_url(request=request, current_site=self.get_site()))

        raise Http404

    class Meta:
        verbose_name = "Improvisation Type Index Page"

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.HomePage']
    max_count = 1


class ImprovisationTypePage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock(features=[
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
            'ol', 'hr', 'link', 'document-link', 'image', 'embed'
        ])),
        ('image', ImageBlock()),
        ('video', VideoEmbedBlock(required=False))
    ], use_json_field=True)

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx['improv_type_pages'] = pack_nav_pages(
            [p.specific for p in self.get_siblings()], self)
        return ctx

    class Meta:
        verbose_name = "Improvisation Type Page"

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.ImprovisationTypeIndexPage']


# Ear Training
class EarTrainingIndexPage(Page, MenuPageMixin):
    class Meta:
        verbose_name = "Ear Training Index Page"

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.HomePage']
    max_count = 1


class EarTrainingLevelPage(Page, MenuPageMixin):
    tab_title = models.CharField(max_length=32)
    body = StreamField([
        ('rich_text', RichTextBlock(features=[
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
            'ol', 'hr', 'link', 'document-link', 'image', 'embed'
        ])),
        ('image', ImageBlock()),
        ('video', VideoEmbedBlock(required=False))
    ], use_json_field=True)

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        siblings = [el.specific for el in self.get_siblings()]
        ctx['et_level_nav'] = pack_nav_pages(siblings, self)
        return ctx

    class Meta:
        verbose_name = "Ear Training Level Page"

    content_panels = Page.content_panels + [
        FieldPanel('tab_title'),
        FieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.EarTrainingIndexPage']


class EarTrainingElementContainerPage(Page, MenuPageMixin):
    """This model serves as a container for the Ear Training
    element pages. It redirects to its first child.
    """
    class Meta:
        verbose_name = "Ear Training Level Page"

    def serve(self, request):
        """Override to redirect to child page"""
        child = self.get_first_child()
        if child:
            return redirect(
                child.get_url(request=request, current_site=self.get_site()))

        raise Http404

    parent_page_types = ['main.EarTrainingLevelPage']


class EarTrainingElementPage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock(
            features=[
                'bold', 'italic', 'ol',
                'hr', 'link', 'document_link'
            ]
        )),
        ('accessible_text', AccessibleTextBlock()),
        ('topic', EarTrainingElementBlock()),
        ('video', VideoEmbedBlock(required=False))
    ], use_json_field=True)

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)

        et_level_parent = self.get_parent().get_parent()
        ctx['et_level_nav'] = pack_nav_pages(
            et_level_parent.get_siblings(), et_level_parent)

        et_element_container = self.get_parent()
        ctx['et_elements_nav'] = pack_nav_pages(
            et_element_container.get_siblings(), et_element_container)

        return ctx

    class Meta:
        verbose_name = "Ear Training Element Page"

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.EarTrainingElementContainerPage']


# Improv Combinations
class ImprovisationCombinationIndexPage(Page, MenuPageMixin):
    class Meta:
        verbose_name = "Improvisation Combination Index Page"

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.HomePage']
    max_count = 1


class ImprovisationCombinationPage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock(features=[
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic',
            'ol', 'hr', 'link', 'document-link', 'image', 'embed'
        ])),
        ('table', TableBlock(template='main/blocks/table_block.html')),
        ('image', ImageBlock()),
        ('video', VideoEmbedBlock(required=False))
    ], use_json_field=True)

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx['improv_combo_pages'] = pack_nav_pages(
            [p.specific for p in self.get_siblings()], self)
        return ctx

    class Meta:
        verbose_name = "Improvisation Combination Page"

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.ImprovisationCombinationIndexPage']
