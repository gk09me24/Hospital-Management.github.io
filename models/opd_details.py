# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class OpdDetails(models.Model):
	_name = "opd.details"  # in postgres sql table name is opd_details
	_description = "OPD Details"
	_rec_name = "opd_id"

	opd_id = fields.Char('OPD Id', readonly=True)
	opd_date = fields.Date('OPD Date', default=fields.Date.context_today)
	medicine_ids = fields.One2many('medicine.line', 'medicine_line_id', string='Medicine Name')
	prescription = fields.Html('Prescription')
	patient_id = fields.Many2one('patient.details', string='Patient Name')
	address = fields.Text('Address', related='patient_id.address')
	dob = fields.Date("DOB", related='patient_id.dob')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender",
							  related='patient_id.gender')
	age = fields.Integer(string='Age', related='patient_id.age', tracking=True)
	contact_number = fields.Char(string="Mobile", related='patient_id.contact_number')
	department_id = fields.Many2one('department.department', string='Department')
	doctor_id = fields.Many2one('doctor.doctor', string='Doctor Name')
	color = fields.Integer('Color')

	company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
	currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')
	total = fields.Monetary('Total Amount', compute="_compute_total")

	priority = fields.Selection([
		('0', 'Normal'),
		('1', 'Low'),
		('2', 'High'),
		('3', 'Very High')], string="Priority")

	state = fields.Selection([
		('draft', 'Draft'),
		('confirm', 'Confirm'),
		('done', 'Done'),
		('cancel', 'Cancel'),
	], string='Status', copy=False, index=True, tracking=3, default='draft', readonly=True)

	def goto_confirm(self):
		self.state = 'confirm'

	def goto_done(self):
		self.state = 'done'

	def goto_cancel(self):
		self.state = 'cancel'

	def goto_draft(self):
		self.state = 'draft'

	@api.model
	def create(self, vals):
		vals['opd_id'] = self.env['ir.sequence'].next_by_code('opd.details') or _('New')
		return super(OpdDetails, self).create(vals)

	@api.depends('medicine_ids')
	def _compute_total(self):
		for rec in self:
			if rec.medicine_ids:
				rec.total = sum(rec.medicine_ids.mapped('sub_total_price'))
			else:
				rec.total = 0

# below onchange method is optional with related filed

# @api.onchange('patient_id')
# def onchange_patient_id(self):
# 	for rec in self:
# 		rec.update({
# 			'address': rec.patient_id.address,
# 			'dob': rec.patient_id.dob,
# 			'gender': rec.patient_id.gender,
# 			'age': rec.patient_id.age,
# 			'contact_number': rec.patient_id.contact_number
# 		})
