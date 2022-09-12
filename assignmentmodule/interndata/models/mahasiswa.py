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

    perusahaan_id = fields.Many2one(
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

    @api.model
    def create(self, vals):
        line = super(DaftarMahasiswa, self).create(vals)
        if line.nim:
            self.env['interndata.perusahaan'].search(
                [('id', '=', line.perusahaan_id.id)]
            ).write({'kuota': line.perusahaan_id.kuota - 1})

        return line

    @api.ondelete(at_uninstall=False)
    def _ondelete_mahasiswa(self):
        b = []
        for a in self:
            b = self.env['interndata.perusahaan'].search(
                [('id', '=', a.perusahaan_id.id)])
        for ob in b:
            ob.kuota += 1
            print('ini kouta', ob.kuota)
        print('Kuota bertambah')
