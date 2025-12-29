from odoo import fields, models #type: ignore

class libraryBook(models.Model):
    _name = "library.book"
    _description = "Books Description"
    _rec_name = "bookName"

    bookName = fields.Char(string = "Book Name", required = True)
    description = fields.Text(string = "About Book", required = True)
    date_published = fields.Date(string = "Date Published")
    author = fields.Char(string = "Author Name", required = True)
    status = fields.Selection(string = "Status", 
                              selection = [("available", "Available"),
                                           ("reserved", "Reserved")])
    isbn = fields.Text(string = "ISBN", copy = False)
    pages = fields.Integer(string = "Number of Pages")
    genre = fields.Many2many("book.genre",string = "Genre")
    borrower_id = fields.Many2one("res.partner", string="Borrower")
    available_stocks = fields.Integer(default=1, compute="_compute_availability", string="Available Stock: ")