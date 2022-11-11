# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date


class PatientDetails(models.Model):
	_name = "patient.details"  # in postgres sql table name is patient_details
	_description = "Patient Details"

	name = fields.Char("Patient Name")
	patient_id = fields.Char("Patient ID", readonly=1)
	address = fields.Text("Address")
	dob = fields.Date("DOB")
	gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
	age = fields.Integer("Age", compute='_calculate_age_patient')
	contact_number = fields.Char("Mobile")
	opd_count_patient = fields.Integer("OPD Count", compute="_compute_opd_count", readonly=1)
	email_id = fields.Char('Email ID')
	user_id = fields.Many2one('res.users', string='Related Name')

	# Overriding Create Method for Sequences

	@api.model
	def create(self, vals):
		vals['patient_id'] = self.env['ir.sequence'].next_by_code('patient.details') or _('New')
		return super(PatientDetails, self).create(vals)

	# Calculate number of OPD count for Active Patient

	def _compute_opd_count(self):
		for rec in self:
			rec.opd_count_patient = self.env['opd.details'].search_count([('patient_id', '=', rec.id)])

	# Calculate Age of Patient depends on "DOB"

	@api.depends('dob')
	def _calculate_age_patient(self):
		for rec in self:
			rec.age = rec.dob and date.today().year - rec.dob.year or 0

	# action for open OPD

	def action_open_opd_patient(self):
		self.ensure_one()
		action = self.env["ir.actions.actions"]._for_xml_id("hospital_management.action_opd_details")
		action['domain'] = [('id', 'in', self.env['opd.details'].search([('patient_id', '=', self.id)]).ids)]
		return action

	# create user for active patient's record-set

	def create_user_patient(self):
		for rec in self:
			# print(">>>>>>>>>>>rec>>>>", rec)
			patient_user = self.env['res.users'].create({
				'name': rec.name,
				'login': rec.email_id,
				'sel_groups_1_9_10': 1,
				'in_group_14': True,
			})
			# print(">>>>>>>>>>>>>patient_user>>>>>>>>>>", patient_user)
			rec.user_id = patient_user
