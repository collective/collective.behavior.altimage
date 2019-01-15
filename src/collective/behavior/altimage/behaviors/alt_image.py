# -*- coding: utf-8 -*-

from collective.behavior.altimage import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IAltImage(model.Schema):
    """
    """

    project = schema.TextLine(
        title=_(u'Project'),
        description=_(u'Give in a project name'),
        required=False,
    )


@implementer(IAltImage)
@adapter(IDexterityContent)
class AltImage(object):
    def __init__(self, context):
        self.context = context

    @property
    def project(self):
        if hasattr(self.context, 'project'):
            return self.context.project
        return None

    @project.setter
    def project(self, value):
        self.context.project = value