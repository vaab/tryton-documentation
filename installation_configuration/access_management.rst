Access Control & management
===========================

#. For models/fields which have no access rules, everyone by default has
   access.
#. All users are subject to access rules that have group left blank.
   Users are also subject to access rules that apply to groups to
   which they belong.
#. If contradictory access rules apply to a single user, the most permissive
   applies.

   #. Example: If a global (group blank) access rule denies access,
      but a group-specific access rule grants access, then access is
      allowed.
   #. Example: If a global (group blank) access rule allows access,
      then everyone will have access; no group-specific rules can
      block it. (Thus, globally granting access is a bad idea. Better
      to just leave the target alone, in which case the default rule
      will apply, permitting access.)
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



