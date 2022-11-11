from odoo import api, fields, models, _


class InputWizard(models.TransientModel):
	_name = 'input.wizard'
	_description = 'Selection Wizard'

	department = fields.Many2one('department.department', string='Department Name')
	doctor_id = fields.Many2one('doctor.doctor', string='Doctor Name')
	opd_date = fields.Date('OPD Date', default=fields.Date.context_today)

	def create_opd(self):
		opd_id = self.env['opd.details'].create({
			'department_id': self.department.id,
			'doctor_id': self.doctor_id.id,
			'opd_date': self.opd_date,
			'patient_id': self.env.context.get('active_ids')[0]
		})
		opd_id.onchange_patient_id()
		# opd_id.state = 'confirm'
		action = {
			'name': _('OPD Details'),
			'type': 'ir.actions.act_window',
			'res_model': 'opd.details',
			'view_mode': 'form',
			'res_id': opd_id.id,
		}
		return action
