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
        sheet.write(1, 0, 'Nama Perusahaan', bold)
        sheet.write(2, 0, 'Alamat', bold)
        sheet.write(3, 0, 'No. Telp', bold)
        sheet.write(4, 0, 'Total Kuota', bold)

        col = 1
        for x in perusahaan:
            row = 1
            sheet.write(row, col, x.name)
            sheet.write(row + 1, col, x.alamat)
            sheet.write(row + 2, col, x.no_telp)
            sheet.write(row + 3, col, x.total_kuota)

        
        sheet.write(6, 1, 'No', bold)
        sheet.write(6, 2, 'Nama Mahasiswa', bold)
        sheet.write(6, 3, 'Jurusan', bold)
        sheet.write(6, 4, 'NIM', bold)
        sheet.write(6, 5, 'Jenis Kelamin', bold)
        sheet.write(6, 6, 'Semester', bold)
        sheet.write(6, 7, 'Daerah Asal', bold)
        # sheet.write(6, 8, 'Universitas', bold)
        
        
        row = 7
        col = 1
        count = 1

        for x in perusahaan.mahasiswa_id:
            col = 1
            sheet.write(row, col, count)
            sheet.write(row, col + 1, x.name)
            sheet.write(row, col + 2, x.jurusan)
            sheet.write(row, col + 3, x.nim)
            sheet.write(row, col + 4, x.jenis_kelamin)
            sheet.write(row, col + 5, x.semester)
            sheet.write(row, col + 6, x.daerah_asal)
            count += 1
            row += 1
