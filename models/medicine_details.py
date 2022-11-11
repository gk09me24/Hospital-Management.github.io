# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class MedicineMedicine(models.Model):
	_name = "medicine.medicine"  # in postgres sql table name is medicine_medicine
	_description = "Medicine Details"

	name = fields.Char('Medicine Name')
	medicine_id = fields.Char('Medicine ID', readonly=1)
	department_id = fields.Many2one('department.department', string='Department Name')

	company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
	currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')
	unit_price = fields.Monetary(string='Medicine Price', currency_field='currency_id')

	color = fields.Integer('Color')

	@api.model
	def create(self, vals):
		vals['medicine_id'] = self.env['ir.sequence'].next_by_code('medicine.medicine') or _('New')
		return super(MedicineMedicine, self).create(vals)
