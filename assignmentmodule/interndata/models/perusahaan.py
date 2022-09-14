from odoo import api, fields, models


class Perusahaan(models.Model):
    _name = 'interndata.perusahaan'
    _description = 'Model Perusahaan'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telp')
    kuota = fields.Integer(string='Kuota Sisa')
    total_kuota = fields.Integer(string='Total Kuota')

    mahasiswa_id = fields.One2many(
        'interndata.mahasiswa',
        'perusahaan_id',
        string='Daftar Mahasiswa',
    )
    
