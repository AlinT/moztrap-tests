#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.base_test import BaseTest
from pages.manage_suites_page import MozTrapManageSuitesPage


class TestManageSuitesPage(BaseTest):

    def test_that_user_can_create_and_delete_suite(self, mozwebqa_logged_in):
        manage_suites_pg = MozTrapManageSuitesPage(mozwebqa_logged_in)

        suite = self.create_suite(mozwebqa_logged_in)

        manage_suites_pg.filter_suites_by_name(name=suite['name'])

        Assert.true(manage_suites_pg.is_element_present(*suite['locator']))

        manage_suites_pg.delete_suite(name=suite['name'])

        Assert.false(manage_suites_pg.is_element_present(*suite['locator']))

        self.delete_product(mozwebqa_logged_in, product=suite['product'])
