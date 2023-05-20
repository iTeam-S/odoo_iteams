# Copyright 2023 Iteam-$ CO
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

GENDER_SELECTION = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]
SIZE_SELECTION = [
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    is_member = fields.Boolean(
        string="Is Member",
        default=True
    )
    last_name = fields.Char(
        string="Last Name",
    )
    poste = fields.Char(
        string="Poste",
    )
    sector_university = fields.Char(
        string="Sector University",
    )
    level_universty = fields.Char(
        string="Level University",
    )
    gender = fields.Selection(
        GENDER_SELECTION,
        string='Gender',
    )
    size = fields.Selection(
        SIZE_SELECTION,
        string='Size'
    )
    university_id = fields.Many2one(
        comodel_name="res.partner",
        string="University",
        domain=[('is_member', '=', False)],
    )
    enterprise_id = fields.Many2one(
        comodel_name="res.partner",
        string="Enterprise",
        domain=[('is_member', '=', False)],
    )







    @ api.depends(
        'is_member',
    )

    def _compute_company_type(self):
        for partner in self:
            if partner.is_member:
                partner.company_type = 'person'
            else:
                partner.company_type = 'company'

    @api.onchange('name')
    def _update_last_name(self):
        if self.name:
            last_word = self.name.split()[-1]
            self.last_name = last_word
        else:
            self.last_name = False
