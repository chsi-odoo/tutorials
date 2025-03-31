from odoo import Command
from odoo.tests import tagged, Form
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.properties = cls.env['estate.property'].create([
            {'name': 'test estate a', 'expected_price': 3, 'garden_area': 5, 'offer_ids': [Command.create({
                'partner_id': cls.env.ref('base.res_partner_12').id,
                'price': 60000,
                'validity': 14
            }),
                Command.create({
                    'partner_id': cls.env.ref('base.res_partner_2').id,
                    'price': 80000,
                    'validity': 14,
                    'status': 'accepted'
                })]},
            {'name': 'test estate b', 'expected_price': 3, 'garden_area': 15},
        ])

    def test_creation_area(self):
        self.properties.living_area = 20
        self.assertRecordValues(self.properties, [
            {'name': 'test estate a', 'total_area': 25},
            {'name': 'test estate b', 'total_area': 35},
        ])

    def test_action_sell(self):
        self.properties[0].action_set_state_sold()
        self.assertEqual(self.properties[0].state, 'sold')
        self.assertRecordValues(self.properties, [
            {'name': 'test estate a', 'state': 'sold'},
            {'name': 'test estate b', 'state': 'new'}
        ])

        with self.assertRaises(UserError):
            self.properties[1].action_set_state_sold()

        with self.assertRaises(UserError):
            self.properties[0].write({'offer_ids': [Command.create({
                'partner_id': self.env.ref('base.res_partner_2').id,
                'price': 80000,
                'validity': 14,
                'status': 'accepted'
            })]})

    def test_is_garden_uncheck_field_reset(self):
        f = Form(self.env['estate.property'])
        f.expected_price = 5
        f.name = 'test estate from form'
        f.garden = True
        f.garden_area = 10
        f.garden_orientation = 'south'
        f.save()
        f.garden = False
        self.assertEqual(f.garden_area, 0)
        self.assertEqual(f.garden_orientation, False)

