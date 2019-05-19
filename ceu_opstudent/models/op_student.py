# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3. 0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class OpStudent(models.Model):
    _inherit = 'op.student'

    cedula = fields.Integer(string='Cédula', help='Ingrese su cédula en el formato 16123123')
    is_ucevista = fields.Boolean(string='¿Es Ucevista?')
    start_year = fields.Integer(string='Año de Ingreso')    
    enfermedades_alergias = fields.Text('Enfermedades y Alergias', help='Ingrese su historial de enfermedades y alergias')
    
