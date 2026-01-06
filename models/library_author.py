from odoo import models, fields #type: ignore

class bookAuthor(models.Model):
    _name = "library.author"
    _description = "Author's description"

    name = fields.Char("Author's name", required=True)
    biography = fields.Text()
    birth_date = fields.Date()
    country_id  = fields.Many2one("res.country", string="Country")

