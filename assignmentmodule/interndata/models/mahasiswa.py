from odoo import api, fields, models


class DaftarMahasiswa(models.Model):
    _name = 'interndata.mahasiswa'
    _description = 'Model untuk daftar mahasiswa'

    name = fields.Char(string='Nama Mahasiswa', required=True)
    jurusan = fields.Char(string='Jurusan', required=True)
    nim = fields.Char(string='NIM', required=True, size=20)

    _sql_constraints = [
        ('nim_mahasiswa_unik', 'UNIQUE (nim)', 'NIM mahasiswa tidak boleh sama'),
    ]
