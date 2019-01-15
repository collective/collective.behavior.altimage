# -*- coding: utf-8 -*-

from collective.behavior.altimage import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IAltImageMarker(Interface):
    """Marker interface for objects that have this behavior.
    """


@provider(IFormFieldProvider)
class IAltImage(model.Schema):
    """
    """

    altimage = namedfile.NamedBlobImage(
        title=_(u'Alternative image'), description=u'', required=False
    )


@implementer(IAltImage)
@adapter(IDexterityContent)
class AltImage(object):
    def __init__(self, context):
        self.context = context

    @property
    def altimage(self):
        if hasattr(self.context, 'altimage'):
            return self.context.altimage
        return None

    @altimage.setter
    def altimage(self, value):
        self.context.altimage = value
