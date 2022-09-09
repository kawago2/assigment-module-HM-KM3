from odoo import api, fields, models


class DaftarMahasiswa(models.Model):
    _name = 'interndata.mahasiswa'
    _inherit = ['res.partner',]
    _description = 'Model untuk daftar mahasiswa'

    name = fields.Char(string='Nama Mahasiswa', required=True)
    jurusan = fields.Char(string='Jurusan', required=True)
    nim = fields.Char(string='NIM', required=True, size=20)
    universitas = fields.Char(string='Universitas', required=True)

    program_id = fields.Many2one(
        comodel_name='interndata.program', string='Program', ondelete='cascade')

    perusahaan_id = fields.Many2many(
        string='Perusahaan',
        comodel_name='interndata.perusahaan',
    )
    _sql_constraints = [
        ('nim_mahasiswa_unik', 'UNIQUE (nim)', 'NIM mahasiswa tidak boleh sama'),
    ]