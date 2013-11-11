Access Control & management
===========================

#. Access rules where Group is left blank apply to everyone.
#. If contradictory access rules apply to a single user, the most permissive
   applies.
#. For models/fields which have no access rules, everyone by default has
   access. But once a model/field has an associated access rule, the default
   rule becomes no-access. The existence of an access rule implicitly restricts
   users not explicitly given access.
#. Access "rules" can be set for Groups. These make access dependent on whether
   the circumstances meet administrator-specified tests. Using these may hurt
   system speed.

Menuitems Access
----------------

These simplify the interfaces for affected users by hiding menuitems that they
have no need to access. They do not, however, necessarily keep data safe. If
model 'X' is used as an associative field of model 'Y', then a user with access
to model 'Y' can access model 'X' through a pop-up, even if the menuitem to
access model 'X' is hidden. Further, a sophisticated user could access the
Tryton server with a tool other than the Tryton client and thereby have access
to such hidden data.



