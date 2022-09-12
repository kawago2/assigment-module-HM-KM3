from odoo import api, fields, models


class Program(models.Model):
    _name = 'interndata.program'
    _description = 'Model untuk daftar kelompok pemagang'

    name = fields.Char(string='Nama Program', required=True)
    kode_program = fields.Char(string='Kode')

    mahasiswa_id = fields.One2many(
        comodel_name='interndata.mahasiswa',
        inverse_name='program_id',
        string='Daftar Mahasiswa',
    )
