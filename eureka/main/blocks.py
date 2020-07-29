from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    CharBlock, TextBlock, RichTextBlock, StructBlock, StreamBlock, ListBlock,
    URLBlock
)
from wagtail.contrib.table_block.blocks import TableBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """
    image_file = ImageChooserBlock(required=True)
    title = CharBlock(
                        help_text='Title for the image',
                        required=False)
    caption = CharBlock(
                        help_text='Caption for the image',
                        required=False)

    class Meta:
        icon = 'image'
        template = "main/blocks/image_block.html"


class VideoEmbedBlock(StructBlock):
    url = URLBlock()
    description = CharBlock(required=False)

    class Meta:
        icon = 'media'
        template = "main/blocks/video_block.html"


class EarTrainingElementBlock(StructBlock):
    title = CharBlock(required=False)
    musical_elements = ListBlock(
        StructBlock([
            ('element_title', CharBlock(required=False)),
            ('content', StreamBlock([
                ('rich_text', RichTextBlock(
                    features=[
                        'bold', 'italic', 'ol', 'ul',
                        'hr', 'link', 'document_link'
                    ],
                    required=False
                )),
                ('image', ImageBlock(required=False)),
                ('video', VideoEmbedBlock(required=False))
            ], icon='cogs', required=False))
        ]),
        required=False
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
