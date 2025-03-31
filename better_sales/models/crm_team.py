from odoo import models, fields, Command, api

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    def _get_teamlead_group_id(self):
        return self.env.ref('better_sales.group_sale_salesman_teamlead').id

    def _update_user_groups(self, old_leader, new_leader):
        teamlead_group_id = self._get_teamlead_group_id()

        if old_leader:
            number_of_leading_teams = self.search([('user_id', '=', old_leader.id)])
            if len(number_of_leading_teams) <= 1:
                old_leader.write({'groups_id': [Command.unlink(teamlead_group_id)]})

        if teamlead_group_id not in new_leader.groups_id.mapped('id'):
            new_leader.write({'groups_id': [Command.link(teamlead_group_id)]})

    def write(self, vals):
        if 'user_id' not in vals:
            return super().write(vals)

        old_leader = self.user_id
        new_leader = self.env['res.users'].browse(vals['user_id'])

        self._update_user_groups(old_leader, new_leader)
        return super().write(vals)

    @api.model
    def create(self, vals):
        new_leader = self.env['res.users'].browse(vals['user_id'])

        self._update_user_groups(None, new_leader)
        return super().create(vals)
