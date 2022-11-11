# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class DepartmentDepartment(models.Model):
	_name = "department.department"  # in postgres sql table name is department_department
	_description = "Department"

	name = fields.Char("Department Name")
	department_id = fields.Char("Department ID", readonly=1)
	doctor_ids = fields.One2many("doctor.doctor", "department", string="Doctor")

	@api.model
	def create(self, vals):
		vals['department_id'] = self.env['ir.sequence'].next_by_code('department.department') or _('New')
		return super(DepartmentDepartment, self).create(vals)
