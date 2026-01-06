from odoo import fields, models #type: ignore

class bookGenre(models.Model):
    _name = "library.genre"
    _description = "Book Genres"

    name = fields.Char(string = "Genre ")
    book_ids = fields.Many2many("library.book", string="Books")
