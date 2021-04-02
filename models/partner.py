from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many('library.book', 'publisher_id',string='Published Books')
    authored_book_ids = fields.Many2many('library.book',string='Authored Books') # relation='library_book_res_partner_rel'  # optional
    count_books = fields.Integer( 'Number of Authored Books',compute='_compute_count_books' )

    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)