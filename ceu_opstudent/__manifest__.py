# -*- coding: UTF-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the Odoo plugin for Dia !
{
    'name': 'CEU student',
    'version': '1.0.0',
    'category': 'Various',
    'author': u'Maury Isasis',
    'website': '',
    'license': 'GPL-3',
    'sequence': 15,
    'summary': 'modulo de registro de miembros',
    'depends': [
            'base',
            'openeducat_core',
        ],
    'data': [            
            "views/op_student_view.xml"
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False
}
