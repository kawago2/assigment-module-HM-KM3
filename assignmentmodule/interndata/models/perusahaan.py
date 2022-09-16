
from odoo import api, fields, models


class Perusahaan(models.Model):
    _name = 'interndata.perusahaan'
    _description = 'Model Perusahaan'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telp')
    kuota = fields.Integer(string='Kuota Sisa',)
    total_kuota = fields.Integer(string='Total Kuota')

    mahasiswa_id = fields.One2many(
        'interndata.mahasiswa',
        'perusahaan_id',
        string='Daftar Mahasiswa',
    )

    @api.onchange('total_kuota')
    def _onchange_total_kuota(self):
        self.kuota = self.total_kuota

    @api.model
    def create(self, vals):
        line = super(Perusahaan, self).create(vals)
        if line.total_kuota:
            self.env['interndata.perusahaan'].search(
                [('id', '=', line.id)]
            ).write({'kuota': line.total_kuota})
        return line
