# - coding: utf-8 -*-
##############################################################################
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

{

    'name': 'Opyme currency rate wizard',

    'version': '1.0',

    'category': '',

    'summary': '',

    'author': 'OPENPYME S.R.L',

    'website': 'openpyme.com.ar',

    'depends': [

        'base',
        'others'

    ],

    'data': [

        'wizard/views/currency_rate_wizard.xml',
        'views/res_currency.xml',

    ],

    'installable': True,

    'auto_install': False,

    'application': True,

    'description': """Creates a wizard to write currency rates.""",

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: