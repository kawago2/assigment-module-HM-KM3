from odoo import api, fields, models


class Karyawan(models.Model):
    _inherit = 'res.partner'
    _description = 'Model untuk daftar karyawan'

    is_karyawan = fields.Boolean(string='Karyawan')
