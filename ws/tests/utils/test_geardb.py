from datetime import datetime, timedelta
from collections import OrderedDict

from django.test import SimpleTestCase
import mock

from ws.utils import geardb as geardb_utils


class FormatHelpers(SimpleTestCase):
    email = 'tim@mit.edu'

    @classmethod
    def setUp(self):
        self.today = datetime.now().date()
        self.yesterday = self.today - timedelta(days=1)
        self.tomorrow = self.today + timedelta(days=1)

    def _format_membership(self, membership_exp, waiver_exp, email=None):
        email = email or self.email
        return geardb_utils.format_membership(email, membership_exp, waiver_exp)

    def _check_format(self, person, email=None):
        """ Ensure formatted memberships adhere to common principles. """
        self.assertSetEqual(set(person.keys()), {'membership', 'waiver', 'status'})
        self.assertEqual(person['membership']['email'], email or self.email)

        active = person['membership']['active'] and person['waiver']['active']
        self.assertEqual(person['status'] == 'Active', active)


class TestFormattingMemberships(FormatHelpers):
    def test_active_membership(self):
        """ Test active membership and current waiver. """
        formatted = self._format_membership(self.tomorrow, self.tomorrow)
        expected = {
            'membership': {
                'expires': self.tomorrow,
                'active': True,
                'email': self.email,
            },
            'waiver': {
                'expires': self.tomorrow,
                'active': True,
            },
            'status': 'Active',
        }
        self.assertEqual(formatted, expected)

    def expect_status(self, membership_exp, waiver_exp, status):
        formatted = self._format_membership(membership_exp, waiver_exp)
        self.assertEqual(formatted['status'], status)
        self._check_format(formatted)

    def test_expired_membership(self):
        """ Report 'Expired' when both membership & waiver missing """
        self.expect_status(self.yesterday, self.yesterday, 'Expired')

    def test_missing_membership(self):
        """ Test valid waiver, but missing membership. """
        self.expect_status(self.yesterday, self.tomorrow, 'Missing Membership')

    def test_missing_waiver(self):
        """ Test valid membership, but missing waiver. """
        self.expect_status(self.tomorrow, None, 'Missing Waiver')

    def test_expired_waiver(self):
        """ Test valid membership, but expired waiver. """
        self.expect_status(self.tomorrow, self.yesterday, 'Waiver Expired')


class TestMembershipLookups(FormatHelpers):
    @mock.patch('ws.utils.geardb.matching_memberships')
    def test_no_membership_found(self, matching_memberships):
        matching_memberships.return_value = OrderedDict()
        emails = ['not.found@example.com', 'no-membership@example.com']
        self.assertEqual(geardb_utils.repr_blank_membership(),
                         geardb_utils.membership_expiration(emails))

    def test_no_emails_given(self):
        """ Test behavior when we're asking for membership under 0 emails. """
        self.assertEqual(geardb_utils.repr_blank_membership(),
                         geardb_utils.membership_expiration([]))

    @mock.patch('ws.utils.geardb.matching_memberships')
    def test_just_most_recent(self, matching_memberships):
        """ When multiple memberships are found, only newest is used. """
        match_tuples = []

        # Mock matching_memberships: a list of matches, newest last
        for i in range(1, 4):
            email = 'member_{}@example.com'.format(i)
            expires = self.tomorrow + timedelta(weeks=i)
            person = self._format_membership(expires, expires, email)
            match_tuples.append((email, person))

        matches = OrderedDict(match_tuples)
        matching_memberships.return_value = matches
        emails = list(matches)
        newest_membership = match_tuples[-1][1]
        self.assertEqual(newest_membership,
                         geardb_utils.membership_expiration(emails))

    def test_empty_emails(self):
        """ Passing an empty list of emails will return zero matches.

        There's no need to hit the database.
        """
        self.assertEqual(OrderedDict(), geardb_utils.matching_memberships([]))
