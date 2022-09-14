from odoo import models, fields


class PerusahaanExcel(models.AbstractModel):
    _name = 'report.interndata.report_perusahaan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tanggal_cetak = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, perusahaan):
        #  workbook
        sheet = workbook.add_worksheet('Daftar Mahasiswa')
        bold = workbook.add_format({'bold': True})
        # format
        sheet.write(0, 0, str(self.tanggal_cetak), bold)
        sheet.write(1, 1, 'Nama Perusahaan', bold)
        sheet.write(1, 2, 'Alamat', bold)
        sheet.write(1, 3, 'No. Telp', bold)
        sheet.write(1, 4, 'Total Kuota', bold)
        sheet.write(1, 5, 'No', bold)
        sheet.write(1, 6, 'Nama Mahasiswa', bold)
        sheet.write(1, 7, 'Jurusan', bold)
        sheet.write(1, 8, 'NIM', bold)
        sheet.write(1, 9, 'Jenis Kelamin', bold)
        sheet.write(1, 10, 'Semester', bold)
        sheet.write(1, 11, 'Daerah Asal', bold)
        sheet.write(1, 12, 'Universitas', bold)
        sheet.write(1, 13, 'Seleksi', bold)

        row = 2
        for x in perusahaan:
            col = 1
            sheet.write(row, col, x.name)
            sheet.write(row, col+1, x.alamat)
            sheet.write(row, col+2, x.no_telp)
            sheet.write(row, col+3, x.total_kuota)
            sheet.set_column(row, col, 20)

            count = 1
            for y in x.mahasiswa_id:
                sheet.write(row, col + 5, y.name)
                sheet.write(row, col + 4, count)
                sheet.write(row, col + 6, y.jurusan)
                sheet.write(row, col + 7, y.nim)
                sheet.write(row, col + 8, y.jenis_kelamin)
                sheet.write(row, col + 10, y.daerah_asal)
                sheet.write(row, col + 9, y.semester)
                sheet.write(row, col + 11, y.universitas_id.name)
                sheet.write(row, col + 12, y.state.selection)  # noqa
                sheet.set_column(row, col, 20)
                count += 1
                row += 1

            row += 1

        sheet.set_column(row, col, 20)
