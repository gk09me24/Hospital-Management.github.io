# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date


class DoctorDoctor(models.Model):
	_name = "doctor.doctor"  			# in postgres sql table name is doctor_doctor
	_description = "Doctor Details"

	name = fields.Char("Doctor Name", translate=True)
	doctor_id = fields.Char("Doctor ID", readonly=1)
	address = fields.Text("Address")
	dob = fields.Date("DOB")
	age = fields.Integer("Age", compute='_calculate_age_doctor')
	contact_number = fields.Char("Mobile")
	department = fields.Many2one('department.department', string='Department')
	opd_count_doctor = fields.Integer("OPD Count", compute="_compute_opd_count")
	color = fields.Integer("Color Index")
	email_id = fields.Char('Email Id')
	user_id = fields.Many2one('res.users', string='Related Name')



	# Overriding Create Method for Sequences

	@api.model
	def create(self, vals):
		vals['doctor_id'] = self.env['ir.sequence'].next_by_code('doctor.doctor') or _('New')
		return super(DoctorDoctor, self).create(vals)


	# Calculate number of OPD count for Active Doctor

	def _compute_opd_count(self):
		for rec in self:
			rec.opd_count_doctor = self.env['opd.details'].search_count([('doctor_id', '=', rec.id)])


	# Calculate Age of Doctor depends on "DOB"

	@api.depends('dob')
	def _calculate_age_doctor(self):
		for rec in self:
			rec.age = rec.dob and date.today().year - rec.dob.year or 0


	# action for open OPD

	def action_open_opd_doctor(self):
		self.ensure_one()
		action = self.env["ir.actions.actions"]._for_xml_id("hospital_management.action_opd_details")
		action['domain'] = [('id', 'in', self.env['opd.details'].search([('doctor_id', '=', self.id)]).ids)]
		return action


	# create user for active doctor's record-set

	def create_user_doctor(self):
		for rec in self:
			doctor_user = self.env['res.users'].create({
				'name': rec.name,
				'login': rec.email_id,
				'sel_groups_1_9_10': 1,
				'in_group_12': True
			})
			rec.user_id = doctor_user.id

