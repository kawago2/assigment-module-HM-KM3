from odoo import models, fields


class MahasiswaExcel(models.AbstractModel):
    _name = 'report.interndata.report_mahasiswa_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tanggal_cetak = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, mahasiswa):
        #  workbook
        sheet = workbook.add_worksheet('Daftar Mahasiswa')
        bold = workbook.add_format({'bold': True})
        # format
        sheet.write(0, 0, str(self.tanggal_cetak), bold)
        sheet.write(1, 0, 'No', bold)
        sheet.write(1, 1, 'Nama Mahasiswa', bold)
        sheet.write(1, 2, 'Jurusan', bold)
        sheet.write(1, 3, 'NIM', bold)
        sheet.write(1, 4, 'Jenis Kelamin', bold)
        sheet.write(1, 5, 'Perusahaan', bold)
        sheet.write(1, 6, 'Program', bold)
        sheet.write(1, 7, 'Universitas', bold)

        row = 2
        col = 0
        count = 1

        for x in mahasiswa:
            col = 0
            sheet.write(row, col, count)
            sheet.write(row, col + 1, x.name)
            
            sheet.write(row, col + 2, x.jurusan)
            sheet.write(row, col + 3, x.nim)
            sheet.write(row, col + 4, x.jenis_kelamin)
            sheet.write(
                row, col + 5, x.perusahaan_id.name if bool(x.perusahaan_id.name) is True else '')  # noqa
            sheet.write(
                row, col + 7, x.universitas_id.name if bool(x.universitas_id.name) is True else '')  # noqa

            for y in x.program_id:
                sheet.write(row, col + 6, y.name)
                sheet.set_column(row, col, 20)
                row += 1
            count += 1
            row += 1
            sheet.set_column(row, col, 20)
