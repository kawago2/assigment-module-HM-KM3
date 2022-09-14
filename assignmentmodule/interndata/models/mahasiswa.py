from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError


class DaftarMahasiswa(models.Model):
    _name = 'interndata.mahasiswa'
    # _inherit = 'res.partner'
    _description = 'Model untuk daftar mahasiswa'

    tanggal_cetak = fields.Date.today()
    avatar = fields.Image(string="Image")
    name = fields.Char(string='Nama Mahasiswa')
    jurusan = fields.Char(string='Jurusan')
    nim = fields.Char(string='NIM', size=20)
    daerah_asal = fields.Char(string='Daerah Asal')
    kepala_jurusan = fields.Char(string='Kepala Jurusan')
    semester = fields.Integer(string='Semester')
    ipk = fields.Float(string='IPK')
    jumlah_sks = fields.Integer(string='Jumlah SKS')
    jenis_kelamin = fields.Selection(
        [
            ('Laki-laki', 'Laki-laki'),
            ('Perempuan', 'Perempuan'),
        ],
        string='Jenis Kelamin',
        required=True,
    )

    state = fields.Selection(string="Seleksi", selection=[
        ('draft', 'Administrasi'),
        ('confirm', 'Interview'),
        ('done', 'Lolos'),
        ('cancelled', 'Tidak Lolos'),
    ],
        default='draft',
        required=True,
        readonly=True,
    )

    program_id = fields.Many2one('interndata.program', string='Program')

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

    @api.constrains('semester')
    def _check_semester(self):
        for record in self:
            if record.semester >= 8:
                raise UserError(
                    'Semester tidak boleh lebih dari sama dengan 8')

    @api.model
    def create(self, vals):
        line = super(DaftarMahasiswa, self).create(vals)
        if line.nim:
            self.env['interndata.perusahaan'].search(
                [('id', '=', line.perusahaan_id.id)]
            ).write({'kuota': line.perusahaan_id.kuota - 1})

            self.env['interndata.universitas'].search(
                [('id', '=', line.universitas_id.id)]).write(
                    {'total_mahasiswa': line.universitas_id.total_mahasiswa + 1})

        return line

    @api.ondelete(at_uninstall=False)
    def _ondelete_mahasiswa(self):
        for xx in self:
            ew = self.env['interndata.universitas'].search(
                [('id', '=', xx.universitas_id.id)])
            for apo in ew:
                apo.total_mahasiswa -= 1

        b = []
        for a in self:
            b = self.env['interndata.perusahaan'].search(
                [('id', '=', a.perusahaan_id.id)])
            for ob in b:
                ob.kuota += 1
                print('ini kouta', ob.kuota)
        print('Kuota bertambah')

    def write(self, vals):
        for x in self:
            obj_now = self.env['interndata.perusahaan'].search(
                [('id', '=', x.perusahaan_id.id)])
            print('debug', obj_now)

            for a in obj_now:
                a.kuota += 1

        for y in self:
            onfix = self.env['interndata.universitas'].search(
                [('id', '=', y.universitas_id.id)])

            for data in onfix:
                data.total_mahasiswa -= 1

        x = super(DaftarMahasiswa, self).write(vals)
        y = super(DaftarMahasiswa, self).write(vals)

        for x in self:
            obj_after = self.env['interndata.perusahaan'].search(
                [('id', '=', x.perusahaan_id.id)])
            print(obj_now)
            print(obj_after)

            for a in obj_after:
                a.kuota -= 1

        for y in self:
            onafter = self.env['interndata.universitas'].search(
                [('id', '=', y.universitas_id.id)])

            for data in onafter:
                data.total_mahasiswa += 1

        return x

    @api.onchange('universitas_id')
    def __onchange_total(self):
        self.universitas_id.total_mahasiswa = len(
            self.universitas_id.mahasiswa_id)

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancelled(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})
