from odoo import models, fields, api


class MoneyEntry(models.Model):
    _name = "money.entry"
    _description = "Money Entry"

    name = fields.Char(string="Description", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    amount = fields.Float(string="Amount", required=True)
    type = fields.Selection(
        [
            ('income', 'Income'),
            ('expense', 'Expense')
        ],
        string="Type",
        required=True
    )
    balance = fields.Float(compute='_compute_balance', string="Balance", readonly=True) # Computational field

    @api.depends('type', 'amount')
    def _compute_balance(self):
        for record in self:
            income = sum(self.search([('type', '=', 'income')]).mapped('amount'))
            expenses = sum(self.search([('type', '=', 'expense')]).mapped('amount'))
            record.balance = income - expenses


    # Server Action to Show Total Balance in a Popup
    def get_balance2(self):
        income = sum(self.search([('type', '=', 'income')]).mapped('amount'))
        expenses = sum(self.search([('type', '=', 'expense')]).mapped('amount'))
        balance = income - expenses

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'current_balance',
                'message': f'Current Balance is {balance}',
                'sticky': False
            }
        }