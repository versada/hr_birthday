# -*- coding: utf-8 -*-

from odoo.tests import common
from datetime import date, timedelta


class TestOldBirthdays(common.TransactionCase):

    def test_old_birthday_events(self):
        test_casess = [
            (date(2017, 5, 16), date(2017, 5, 2), 14, date(2017, 5, 2)),
            (date(2017, 2, 16), date(2017, 2, 3), 14, date(2017, 2, 2)),
            (date(2017, 3, 16), date(2017, 3, 1), 14, date(2017, 3, 2))
        ]

        employee = self.env['hr.employee'].create({
            'birthday': '2017-02-16',
            'name': 'Jonas Sladkevičius'})

        for i in test_casess:
            today = i[0]
            event = self.env['hr.birthday'].create({
                'birthday_date': i[1],
                'birthday_employee': employee.id,
                'active': True})
            old_event = event.get_old_birthdays(
                i[2], today)
            aa = i[0] - timedelta(days=i[2])
            self.assertEqual(aa,  i[3])