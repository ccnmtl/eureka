from django.db import models
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from wagtail.admin.edit_handlers import (
    StreamFieldPanel, FieldPanel, InlinePanel
)
from wagtail.core.blocks import (
    RichTextBlock, StructBlock, StreamBlock, BlockQuoteBlock, CharBlock
)
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.core.url_routing import RouteResult
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_panel


class HomePage(Page, MenuPageMixin):
    class Meta:
        verbose_name = "Homepage"

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['wagtailcore.Page']
    max_count = 1


class BasicPage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    class Meta:
        verbose_name = "Basic Page"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]


# Improv Types
class ImprovisationTypeIndexPage(Page, MenuPageMixin):
    class Meta:
        verbose_name = "Improvisation Type Index Page"

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.HomePage']
    max_count = 1


class ImprovisationTypePage(Page, MenuPageMixin):
    body = StreamField([
        ('rich_text', RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    class Meta:
        verbose_name = "Improvisation Type Page"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
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
    body = StreamField([
        ('rich_text', RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    class Meta:
        verbose_name = "Ear Training Level Page"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
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
        ('rich_text', RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    class Meta:
        verbose_name = "Ear Training Element Page"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
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
        ('rich_text', RichTextBlock()),
        ('image', ImageChooserBlock())
    ])

    class Meta:
        verbose_name = "Improvisation Combination Page"

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    settings_panels = Page.settings_panels + [
        menupage_panel
    ]

    parent_page_types = ['main.ImprovisationCombinationIndexPage']
