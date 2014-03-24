Basic Concepts
==============

**Models** 


:py:class:`~trytond.model.Model([id[,**kwargs]])`
This is the base class that every kind of model inherits. It defines
common attributes of all models.
For details description about Models in tryton refer to `Tryton Model Docs <http://doc.tryton.org/3.0/trytond/doc/ref/models/models.html/>`_
A complete library model is explained in the previous chapter.

**Views** 

The views are used to display records of an object to the user.
In tryton, models can have several views, it is the action, that opens
the window, that tells which views must be used. The view are built using
XML that is stored in the module's view diectory or can be stored in
database with the object.ir.ui.view. So generally, they are defined in xml 
files with this kind of xml:

.. code-block:: xml
   :linenos:

    <record model="ir.ui.view" id="view_id">
        <field name="model">model name</field>
        <field name="type">type name</field>
        <field name="inherit" ref="inherit_view_id"/>
    </record>

Active Records
--------------

TODO


Transactions
------------

TODO

Extending Tryton (Inheritance)
------------------------------

Tryton modules can be easily extended. Models and Views need to be
extended using Inheritence.

**Extending Models** : To extend an existing model (like Company), one need to
instantiate a class with the same __name__ attribute:

.. code-block:: python
    
    from trytond.model import fields
    from trytond.pool import PoolMeta

    __all__=['Company']
    __metaclass__ = PoolMeta


    class Company:
        __name__ = 'company.company'
        company_code = fields.Char('Company Code')


**Extending Views** : Each inherit view must start with data tag.
**xpath** tag is used which specifies the location where the field is to be 
added.

* expr : the xpath expression to find a node in the inherited view.
* position : Define the position from the found node, it can be before,
after, replace, inside or replace_attributes which will change the
attributes.

**Example**

.. code-block:: xml
   :linenos:

    <data>
        <xpath
            expr="/form/notebook/page/separator[@name=&quot;signature&quot;]"
            position="before">
            <label name="company_code"/>
            <field name="company_code"/>
            <label name="company"/>
            <field name="company"/>
            <label name="employee_code"/>
            <field name="employee_code"/>
        </xpath>
    </data>

Wizard
------------------------------------------------------------------
A wizard is a fine state machine.

:py:class:`~trytond.wizard.Wizard(session_id)`
This is the base for any wizard. It contains the engine for the finite
state machine. A wizard must have some state instance attributes that the
engine will use.


Class attributes are:
**Wizard.__name__**
It contains the unique name to reference the wizard throughout the platform.


**Wizard.start_state**
   It contains the name of the starting state.

**Wizard.end_state**
   It contains the name of the ending state.

**Wizard.__rpc__**
   Same as trytond.model.Model.__rpc__.

**Wizard.states**
   It contains a dictionary with state name as key and State as value


.. code-block:: python

   from trytond.wizard import Wizard, StateView, StateTransition, Button
   
   class PrintLibraryReportStart(ModelView):
       'Print Library Report'
        __name__ = 'library.print_report.start'

   class PrintLibraryReport(Wizard):
       'Print Library Report'
        __name__ = 'library.print_report'

        start = StateView(
            'library.print_report.start', 'library.print_view_form',
            [
                Button('Cancel', 'end', 'tryton-cancel'),
                Button('Print', 'print_', 'tryton-print', default=True),
            ]
        )
        print_ = StateAction('library.book')

        def do_print_(self, action):
            data = {
                'library': self.start.book.id,
            }
            return action, data

        def transition_print_(self):
            return 'end'

Register the  Wizard model name in __init__.py and add the xml
files in tryton.cfg file.

.. code-block:: python

   #Register type_='wizard' in __init__.py
   Pool.register(
      PrintLibraryReport,
      module='library', type_='wizard'
   )

Add the record tag for the wizard in library.xml

.. code-block:: xml

    <record model="ir.action.wizard" id="book_print">
        <field name="name">Print Library Book</field>
        <field name="wiz_name">library.print_report</field>
    </record>  
WebServices
-----------

TODO
