"""
Overview of all settings which can be customized.
"""
from django.conf import settings
from django.utils.translation import ugettext as _

# Allow old Django 1.2 MEDIA_URL, but prefer STATIC_URL if it's set.
MEDIA_PREFIX = getattr(settings, 'STATIC_URL', settings.MEDIA_URL) + "ecms_dashboard/oxygen/"

ECMS_DASHBOARD_APP_ICONS = {
    'fiber/page': MEDIA_PREFIX + 'internet-web-browser.png',
    'fiber/contentitem': MEDIA_PREFIX + 'folder-txt.png',
    'fiber/image': MEDIA_PREFIX + 'folder-image.png',
    'fiber/file': MEDIA_PREFIX + 'folder.png',
    'ecms/cmsobject': MEDIA_PREFIX + 'internet-web-browser.png',
    'ecms/cmslayout': MEDIA_PREFIX + 'view-choose.png',
    'ecms/cmssite':   MEDIA_PREFIX + 'preferences-system-network.png',
    'ecms_media/file': MEDIA_PREFIX + 'folder.png',
    'auth/user':  MEDIA_PREFIX + 'system-users.png',
    'auth/group': MEDIA_PREFIX + 'resource-group.png',
    'sites/site': MEDIA_PREFIX + 'applications-internet.png',
    'registration/registrationprofile': MEDIA_PREFIX + 'list-add-user.png'
}

ECMS_DASHBOARD_DEFAULT_ICON = MEDIA_PREFIX + 'unknown.png'


ECMS_DASHBOARD_APP_ICONS.update(getattr(settings, 'ECMS_DASHBOARD_APP_ICONS', {}))

ECMS_DASHBOARD_APP_GROUPS = getattr(settings, 'ECMS_DASHBOARD_APP_GROUPS', (
    (_('CMS'), ('*',)),
    (_('Administration'), ('django.contrib.*', 'registration.*',)),
    #(_('Developer tools'), ()),
))