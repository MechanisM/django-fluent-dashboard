"""
Custom menu items
"""
from admin_tools.menu import items
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext as _
from ecms_dashboard.utils import sort_cms_models


class CmsModelList(items.ModelList):
    """
    An menu of models, with a strong bias towards sorting CMS apps.
    """
    def init_with_context(self, context):
        listitems = self._visible_models(context['request'])

        # Convert to dictionary items first, like the dashboard icons.
        models = [
            { 'name': model.__name__,
              'title': capfirst(model._meta.verbose_name_plural),
              'url': self._get_admin_change_url(model, context)
            }
            for model, perms in listitems if perms['change']
        ]

        # Sort models.
        sort_cms_models(models)

        # Convert to items
        for model in models:
            self.children.append(items.MenuItem(title=model['title'], url=model['url']))


class ReturnToSiteItem(items.MenuItem):
    """
    A logout button for the menu.
    """
    title = _('Return to site')
    url = '/'
    css_classes = ['ecms-menu-item-tosite']
