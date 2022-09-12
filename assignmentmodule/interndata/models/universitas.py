from odoo import api, fields, models


class Universitas(models.Model):
    _name = 'interndata.universitas'
    _description = 'Model untuk daftar universitas'

    name = fields.Char(string='Nama Universitas')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telp')

    mahasiswa_id = fields.One2many(
        'interndata.mahasiswa',
        'universitas_id',
        string='Daftar Mahasiswa',
        readonly=True,
    )
