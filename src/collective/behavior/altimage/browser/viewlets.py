# -*- coding: utf-8 -*-
from collective.behavior.altimage.behaviors.altimage import IAltImage
from plone.app.layout.viewlets import ViewletBase


class AltImageViewlet(ViewletBase):
    """ A simple viewlet which renders altimage """

    def update(self):
        self.context = IAltImage(self.context)
        self.available = True if self.context.image else False
