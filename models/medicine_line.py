# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class MedicineMedicine(models.Model):
	_name = "medicine.line"  # in postgres sql table name is medicine_medicine
	_description = "Medicine Details Lines"
	_rec_name = 'medicine_details_id'

	medicine_line_id = fields.Many2one('opd.details', string='Medicine Line')
	medicine_details_id = fields.Many2one('medicine.medicine', string='Medicine Name')
	# sequence_id = fields.Many2one('medicine.medicine', related='medicine_details_id.medicine_id')
	medicine_department_id = fields.Many2one('department.department')
	qty = fields.Integer('Qty', default=1)
	currency_id = fields.Many2one('res.currency', string='Currency', related='medicine_details_id.currency_id')
	unit_price = fields.Monetary('Unit Price', related='medicine_details_id.unit_price')
	sub_total_price = fields.Monetary(string='Sub Total', compute='_compute_sub_total_price')



	@api.depends('unit_price', 'qty')
	def _compute_sub_total_price(self):
		for rec in self:
			rec.sub_total_price = rec.unit_price * rec.qty
