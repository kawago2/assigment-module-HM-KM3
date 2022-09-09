from odoo import api, fields, models


class Perusahaan(models.Model):
    _name = 'interndata.perusahaan'
    _description = 'Model Perusahaan'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telp')

    mahasiswa_id = fields.Many2many(
        comodel_name='interndata.mahasiswa', string='Daftar Mahasiswa')
