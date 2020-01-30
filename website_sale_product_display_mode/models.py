# © 2020 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields


class ProductTemplateDisplayMode(models.Model):
    _inherit = "product.template"

    display_mode = fields.Selection(
        [
            ('has_preview', 'Has Preview'),
            ('no_preview', 'No Preview'),
            ('unlocked', 'Unlocked'),
        ],
        string='Display Mode',
        default='no_preview',
        help="Set the display mode of the product"
    )
