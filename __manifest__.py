# -*- coding: utf-8 -*-
{
	'name': 'Hospital Management',
	'version': '1.0.0',
	'summary': 'Manage OPD of Hospital',
	'sequence': -110,
	'author': 'Candidroot Solution',
	'description': """
            You can manage Patient & Doctor OPD Shedule for Hospital.
            Testing purpose for git pracrice
    """,
	'website': 'www.candidroot.com',
	'depends': ['base', 'report_xlsx'],
	'data': [
		'security/security.xml',
		'security/ir.model.access.csv',
		'data/ir_sequence_department.xml',
		'data/ir_sequence_doctor.xml',
		'data/ir_sequence_medicine.xml',
		'data/ir_sequence_patient.xml',
		'data/ir_sequence_opd.xml',
		'wizard/input_wizard_view.xml',
		'report/opd_report.xml',
		'report/opd_report_templates.xml',
		'views/main_menu.xml',
		'views/patient_details_views.xml',
		'views/doctor_details_views.xml',
		'views/opd_details_views.xml',
		'views/department_views.xml',
		'views/medicine_views.xml',
	],
	'demo': [
		'data/department_domo.xml',
		'data/medicine_domo.xml',
		'data/doctor_domo.xml',
		'data/patient_domo.xml',
		'data/opd_domo.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}
