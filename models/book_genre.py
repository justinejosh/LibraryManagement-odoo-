from odoo import fields, models #type: ignore

class bookGenre(models.Model):
    _name = "book.genre"
    _description = "Book Genres"

    name = fields.Char(string = "Genre ")