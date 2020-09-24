# Generated by Django 2.2.14 on 2020-09-24 03:35

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200831_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eartrainingelementpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'hr', 'link', 'document_link'])), ('accessible_text', wagtail.core.blocks.StructBlock([('visible_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document_link'], icon='pilcrow', label='Visible text')), ('screen_reader_text', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'link', 'document_link'], icon='fa-universal-access', label='Screen reader text'))])), ('topic', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('musical_elements', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('element_title', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.StreamBlock([('rich_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document_link'], required=False)), ('accessible_text', wagtail.core.blocks.StructBlock([('visible_text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document_link'], icon='pilcrow', label='Visible text')), ('screen_reader_text', wagtail.core.blocks.RichTextBlock(features=['ol', 'ul', 'link', 'document_link'], icon='fa-universal-access', label='Screen reader text'))], required=False)), ('sr_only_text', wagtail.core.blocks.TextBlock(icon='fa-universal-access', label='SR text', required=False, template='main/blocks/screen_reader_block.html')), ('image', wagtail.core.blocks.StructBlock([('image_file', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(help_text='Title for the image', required=False)), ('caption', wagtail.core.blocks.CharBlock(help_text='Caption for the image', required=False))], required=False)), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('description', wagtail.core.blocks.CharBlock(required=False))], required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='main/blocks/table_block.html'))], icon='cogs', required=False))]), required=False))]))]),
        ),
    ]
