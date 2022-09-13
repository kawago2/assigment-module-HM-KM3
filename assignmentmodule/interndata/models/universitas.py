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
    )

    total_mahasiswa = fields.Integer()

    # @api.onchange('mahasiswa_id')
    # def on_change_mahasiswa(self):
    #     a = self.env['interndata.perusahaan'].search(
    #         [('id', '=', self.mahasiswa_id.id)])
    #     self.total_mahasiswa = len(a)
