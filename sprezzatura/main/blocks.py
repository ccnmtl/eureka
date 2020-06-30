from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    CharBlock, TextBlock, RichTextBlock, StructBlock, StreamBlock, ListBlock
)
from wagtail.contrib.table_block.blocks import TableBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image_file = ImageChooserBlock(required=True)
    caption_block = RichTextBlock(
                        help_text='Caption block for the image',
                        required=False)
    caption = CharBlock(
                        help_text='Caption for the image',
                        required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "main/blocks/image_block.html"


class MusicBlock(StructBlock):
    file = DocumentChooserBlock()
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "main/blocks/music_block.html"


class EarTrainingElementBlock(StructBlock):
    title = CharBlock()
    musical_elements = ListBlock(
        StructBlock([
            ('element_title', CharBlock()),
            ('content', StreamBlock([
                ('rich_text', RichTextBlock()),
                ('image', ImageChooserBlock()),
                ('music_example', MusicBlock())
            ], icon='cogs'))
        ])
    )


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize for content body
    """
    text = RichTextBlock(icon='pilcrow')
    image = ImageBlock()
    table_caption = CharBlock(
                        required=False,
                        help_text='Table caption',
                        icon='fa-thumb-tack')
    table = TableBlock(template='main/blocks/table_block.html')
    sr_text = TextBlock(
                        required=False,
                        icon='fa-universal-access',
                        label='SR text',
                        template='main/blocks/screen_reader_block.html')
