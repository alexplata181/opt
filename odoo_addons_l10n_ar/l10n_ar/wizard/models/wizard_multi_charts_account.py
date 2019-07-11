# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api


class WizardMultiChartsAccounts(models.TransientModel):

    _inherit = 'wizard.multi.charts.accounts'

    @api.multi
    def execute(self):
        country_ar = self.env.ref('base.ar')
        self.env['ir.values'].sudo().set_default(
            'res.partner', 'country_id', country_ar.id, for_all_users=True, company_id=self.company_id.id
        )
        return super(WizardMultiChartsAccounts, self).execute()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
