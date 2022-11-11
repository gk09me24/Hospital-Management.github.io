# -*- coding: utf-8 -*-
from odoo import models


class PatientDetailsXlsx(models.AbstractModel):
	_name = "report.hospital_management.report_patient_details_xls"
	_inherit = "report.report_xlsx.abstract"

	def generate_xlsx_report(self, workbook, data, patient):
		sheet = workbook.add_worksheet('Patient List')
		bold = workbook.add_format({'bold': True, 'bg_color': '#dee6ef', 'align': 'center'})
		format_1 = workbook.add_format({'bold': True, 'bg_color': '#FF9933', 'align': 'center', 'size': 12})
		sheet.set_column('A:A', 11)
		sheet.set_column('B:B', 18)
		sheet.set_column('C:C', 8)
		sheet.set_column('D:D', 12)
		sheet.set_column('E:E', 10)
		sheet.set_column('F:F', 4)
		sheet.set_column('G:G', 20)
		sheet.set_column('H:H', 58)
		sheet.set_column('I:I', 12)

		row = 1
		col = 0

		sheet.merge_range(row - 1, col, row - 1, col + 8, 'LIST OF THE PATIENT', format_1)
		sheet.write(row, col, 'PATIENT ID', bold)
		sheet.write(row, col + 1, 'PATIENT NAME', bold)
		sheet.write(row, col + 2, 'GENDER', bold)
		sheet.write(row, col + 3, 'MOBILE NO', bold)
		sheet.write(row, col + 4, 'DOB', bold)
		sheet.write(row, col + 5, 'AGE', bold)
		sheet.write(row, col + 6, 'EMAIL ID', bold)
		sheet.write(row, col + 7, 'ADDRESS', bold)
		sheet.write(row, col + 8, 'OPD COUNT', bold)

		for rec in patient:
			row += 1
			sheet.write(row, col, rec.patient_id)
			sheet.write(row, col + 1, rec.name)
			sheet.write(row, col + 2, rec.gender)
			sheet.write(row, col + 3, rec.contact_number)
			sheet.write(row, col + 4, rec.dob.strftime('%d/%m/%Y'))
			sheet.write(row, col + 5, rec.age)
			sheet.write(row, col + 6, rec.email_id)
			sheet.write(row, col + 7, rec.address)
			sheet.write(row, col + 8, rec.opd_count_patient)
