from odoo import api, fields, models


class InputMahasiswa(models.TransientModel):
    _name = 'interndata.inputmahasiswa'

    program_id = fields.Many2one('interndata.program', string='Program')
    perusahaan_id = fields.Many2one(
        string='Perusahaan',
        comodel_name='interndata.perusahaan',
    )
    universitas_id = fields.Many2one(
        string='Universitas',
        comodel_name='interndata.universitas',
    )
    mahasiswa_id = fields.Many2one(
        comodel_name='interndata.mahasiswa', string='Nama Mahasiswa', required=True)

    def button_input_mahasiswa(self):
        # filter = []
        # mahasiswa_id = self.mahasiswa_id
        # if mahasiswa_id:
        #     filter += [('state', '=', mahasiswa_id.state)]
        for x in self:
            obj_id = self.env['interndata.program'].search(
                [('id', '=', x.program_id.id)])
            print('debug', obj_id)
            for a in obj_id:
                a.mahasiswa_id += x.mahasiswa_id
                print('debug', a.mahasiswa_id)

            for x in self:
                obj_id = self.env['interndata.perusahaan'].search(
                    [('id', '=', x.perusahaan_id.id)])
                print('debug', obj_id)
                for a in obj_id:
                    a.mahasiswa_id += x.mahasiswa_id
                    print('debug', a.mahasiswa_id)

            for x in self:
                obj_id = self.env['interndata.universitas'].search(
                    [('id', '=', x.universitas_id.id)])
                print('debug', obj_id)
                for a in obj_id:
                    a.mahasiswa_id += x.mahasiswa_id
                    print('debug', a.mahasiswa_id)

        #     a.mahasiswa_id.program_id.id += self.mahasiswa_id

    @api.onchange('mahasiswa_id')
    def __onchange_mahasiswa(self):
        self.program_id = self.mahasiswa_id.program_id
        self.perusahaan_id = self.mahasiswa_id.perusahaan_id
        self.universitas_id = self.mahasiswa_id.universitas_id
