from odoo import api, fields, models


class Program(models.Model):
    _name = 'interndata.program'
    _description = 'Model untuk daftar kelompok pemagang'

    name = fields.Char(string='Nama Program', required=True)

    mahasiswa_id = fields.One2many(
        'interndata.mahasiswa',
        'program_id',
        string='Daftar Mahasiswa',
    )