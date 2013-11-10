Access Control & management
===========================
[This is not documentation ... just a request that documentation answer certain questions.]

1. What rules define when access is granted?
My presumption had been that it was granted unless explicitly restricted.  However, a recent experience makes me
suspect that granting explicit permission to one user may implicitly restrict other users.  What logic governs
this?

2. What are some typical best practices?
The two use cases I am aware of are (1) a company where management seeks to apply a "need to know/change" policy 
where only those employees who have need to make certain changes (or see certain information) are able to; (2)
certain computerized functions need their own users (eg Nereid).  (I will assume case 2 to be a developer issue,
not for an administrator.)

In implementing case 1 in my company, I ended up creating a relatively restrictive "general" group that all
employees go into.  Employees who need additional access are then added also to more permissive groups.  This
does not feel like a good approach because forgetting to add the new guy to "general" may mean that she/he
gets too many.  Is there a better way.

3. Limiting access on fields vs models.
Limiting access to fields or menuitems is very concrete and understandable.  Model-level restrictions are more
difficult to understand.  Any tips?
