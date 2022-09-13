from odoo import api, fields, models


class Program(models.Model):
    _name = 'interndata.program'
    _description = 'Model untuk daftar kelompok pemagang'

    name = fields.Char(string='Nama Program', required=True)
    kode_program = fields.Char(string='Kode')

    mahasiswa_id = fields.Many2many(
        comodel_name='interndata.mahasiswa',
        string='Daftar Mahasiswa',
    )