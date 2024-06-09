from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate module Property model"

    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description', required=True)
    postcode = fields.Char('Post Code', required=True)
    date_availability = fields.Date('Availability Date')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('# of Rooms')
    living_area = fields.Integer('Living Area m2')
    facades = fields.Integer('# Facades')
    garage = fields.Boolean('Has Garage')
    garden = fields.Boolean('Has Garden')
    garden_area = fields.Integer('Garden Area m2')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
        help='Defines the garden orientation'
    )
    active = fields.Boolean('Active', default=False)
    state = fields.Selection(
        string='State',
        copy=False,
        default='new',
        help='Defines the garden orientation',
        selection=[
            ('new', 'New'),
            ('received', 'Offer Received'),
            ('accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
    )
