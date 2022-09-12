from odoo import api, fields, models


class DaftarMahasiswa(models.Model):
    _name = 'interndata.mahasiswa'
    # _inherit = ['res.partner', ]
    _description = 'Model untuk daftar mahasiswa'

    name = fields.Char(string='Nama Mahasiswa', required=True)
    jurusan = fields.Char(string='Jurusan', required=True)
    nim = fields.Char(string='NIM', required=True, size=20)

    program_id = fields.Many2one(
        comodel_name='interndata.program', string='Program', ondelete='cascade')

    perusahaan_id = fields.Many2many(
        string='Perusahaan',
        comodel_name='interndata.perusahaan',
    )

    universitas_id = fields.Many2one(
        string='Universitas',
        comodel_name='interndata.universitas',
    )
    _sql_constraints = [
        ('nim_mahasiswa_unik', 'UNIQUE (nim)', 'NIM mahasiswa tidak boleh sama'),
    ]
