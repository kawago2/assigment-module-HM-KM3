# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request
import json


class Interndata(http.Controller):
    @http.route('/interndata/getmahasiswa', auth='public', method=['GET'])
    def getMahasiswa(self, **kw):
        mahasiswa = request.env['interndata.mahasiswa'].search([])
        datas = []

        for data in mahasiswa:
            obj1 = []
            obj2 = []
            for xx in data.program_id:
                obj1.append({
                    'name': xx.name,
                })
            for yy in data.perusahaan_id:
                obj2.append({
                    'name': yy.name,
                })

            datas.append({
                'nama': data.name,
                'nim': data.nim,
                'universitas': data.universitas_id.name if bool(data.universitas_id.name) is True else '-',
                'jurusan': data.jurusan,
                'program_id': obj1,
                'perusahaan_id': obj2,
            })

        return json.dumps(datas)

    @http.route('/interndata/getprogram', auth='public', method=['GET'])
    def getProgram(self, **kw):
        program = request.env['interndata.program'].search([])
        datas = []

        for data in program:
            datas.append({
                'nama_program': data.name,
                'kode_program': data.kode_program,
            })
        return json.dumps(datas)

    @http.route('/interndata/getperusahaan', auth='public', method=['GET'])
    def getPerusahaan(self, **kw):
        perusahaan = request.env['interndata.perusahaan'].search([])
        datas = []

        for data in perusahaan:
            obj1 = []
            for xx in data.mahasiswa_id:
                obj1.append({
                    'nama': xx.name,
                    'nim': xx.nim,
                    'jurusan': xx.jurusan,
                    'daerah_asal': xx.daerah_asal,
                })

            datas.append({
                'nama_perusahaan': data.name,
                'alamat': data.alamat,
                'no_telp': data.no_telp,
                'kuota': data.kuota,
                'mahasiswa': obj1,
            })
        return json.dumps(datas)

    @http.route('/interndata/getuniversitas', auth='public', method=['GET'])
    def getUniversitas(self, **kw):
        universitas = request.env['interndata.universitas'].search([])
        datas = []

        for data in universitas:
            obj1 = []
            for xx in data.mahasiswa_id:
                obj1.append({
                    'nama': xx.name,
                    'nim': xx.nim,
                    'jurusan': xx.jurusan,
                    'daerah_asal': xx.daerah_asal,
                })

            datas.append({
                'nama_universitas': data.name,
                'alamat': data.alamat,
                'no_telp': data.no_telp,
                'mahasiswa': obj1,
            })
        return json.dumps(datas)

    @http.route('/interndata/getkaryawan', auth='public', method=['GET'])
    def getUniversitas(self, **kw):
        karyawan = request.env['res.partner'].search([])
        datas = []

        for data in karyawan:
            if bool(data.is_karyawan) is True:

                datas.append({
                    'nama': data.name,
                    'phone': data.phone,
                    'email': data.email,
                    'city': data.city,

                })
        return json.dumps(datas)
