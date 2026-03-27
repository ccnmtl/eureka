from wagtail import hooks


@hooks.register('construct_explorer_page_queryset')
def order_pages(parent_page, pages, request):
    return pages.order_by('path')
