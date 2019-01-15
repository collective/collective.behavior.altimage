# -*- coding: utf-8 -*-
from collective.behavior.altimage.behaviors.alt_image import IAltImage
from collective.behavior.altimage.testing import COLLECTIVE_BEHAVIOR_ALTIMAGE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class AltImageIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_ALTIMAGE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_alt_image(self):
        behavior = getUtility(
            IBehavior, 'collective.behavior.altimage.alt_image'
        )
        self.assertEqual(behavior.marker, IAltImage)
        behavior_name = (
            'collective.behavior.altimage.behaviors.alt_image.IAltImage'
        )
        behavior = getUtility(IBehavior, behavior_name)
        self.assertEqual(behavior.marker, IAltImage)
