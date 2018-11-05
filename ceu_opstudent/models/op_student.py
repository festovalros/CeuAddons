# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3. 0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class OpStudent(models.Model):
    _inherit = 'op.student'

#    birth_date = fields.Date(string="Fecha de Nacimiento")
    is_ucevista = fields.Boolean(string='¿Es Ucevista?')
#    blood_group = fields.Selection(string="Grupo Sanguíneo", [('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-')])
    start_year = fields.Integer(string='Año de Ingreso', readonly=True)    

    
