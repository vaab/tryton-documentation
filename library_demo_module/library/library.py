from trytond.pool import *
from trytond.model import fields, ModelSQL, ModelView

# set __meta__ to use Trytons inheritance model
__metaclass__ = PoolMeta
__ALL__ = ['Book', 'Party']



class Book(ModelSQL, ModelView):
    # A model for 'Book'
    "BOOK"
    # Internal class name. Always used as a reference inside Tryton
    # default: <modules name> + . + <class name> on Tryton
    # and on database <modules name> + _ + <class name>
    __name__ = 'library.book'
    title = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    subject = fields.Char('Subject')
    abstract = fields.Text('Abstract')

    # A relational field to point on (one) party
    renter = fields.Many2One('party.party', 'Rented by')


# Example for Tryton model-inheritance
class Party:
    __name__ = 'party.party'

    # Reverse relation for book.renter (reference to all rented books)
    rented_books = fields.One2Many('library.book', 'renter', 'Rented Books')