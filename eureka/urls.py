from django.conf import settings
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.static import serve
import os.path
from eureka.main.views import S3DocumentServe
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

site_media_root = os.path.join(os.path.dirname(__file__), "../media")


redirect_after_cms_logout = getattr(settings, 'LOGOUT_REDIRECT_URL', None)
auth_urls = url(r'^accounts/', include('django.contrib.auth.urls'))
logout_cms_page = path(
    'accounts/logout/',
    logout,
    {'next_page': redirect_after_cms_logout})
if hasattr(settings, 'CAS_BASE'):
    from djangowind.views import logout as windlogout
    auth_urls = url(r'^accounts/', include('djangowind.urls'))
    logout_cms_page = path(
        'accounts/logout/',
        windlogout,
        {'next_page': redirect_after_cms_logout})


urlpatterns = [
    auth_urls,
    path('admin/', admin.site.urls),
    path('stats/', TemplateView.as_view(template_name="stats.html")),
    path('smoketest/', include('smoketest.urls')),
    path('infranil/', include('infranil.urls')),
    re_path(r'^uploads/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/(?P<document_id>\d+)/(.*)$',
            S3DocumentServe.as_view(),
            name='wagtaildocs_serve'),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
