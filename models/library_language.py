from odoo import models, fields #type: ignore

class BookLanguage(models.Model):
    _name = "library.language"
    _description = "This is used to group the books using different languages."

    name = fields.Char(string = "Language", required = True)
    code = fields.Char(string = "ISO Code")
