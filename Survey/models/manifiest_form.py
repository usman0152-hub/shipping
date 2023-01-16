from odoo import fields, models


class ManifiestModel(models.Model):
    _name = "manifiest.model"
    _description = "Manifiest Form"

    tran = fields.Char('Tran #')
    doc = fields.Char('Coc #')
    year = fields.Char('Year #')
    shippingline/agent = fields.Char('Tran #')
    doc = fields.Char('Coc #')
    year = fields.Char('Year #')