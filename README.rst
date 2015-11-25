pyki
====

A Python based, gitit inspired wiki

Motivation
==========

```gitit`` <http://www.gitit.net/>`__ is great, but I miss some features
and don't have time to learn Haskell, while on the other hand I want to
hack this myself...

About the name
--------------

Python + Wiki = pyki. Short, yet apparently unused. The only apparent
meaning seems to be `wiktionary.org's
pyki <https://en.wiktionary.org/wiki/pyki>`__, which states it's a
conjugation of the `Finish
"pyki?" <https://en.wiktionary.org/wiki/pyki%C3%A4#Finnish>`__, a verb
meaning

    1. To chap (of the skin, to split or flake due to cold weather or
       dryness).
    2. To crack (to form cracks due to drying, shrinking or other such
       process).

Ok, so the project can use a crack as icon at some point...

Components and Packages that can be used
----------------------------------------

Obviously there's no point in reinventing everything, so existing
projects will be integrated as best as possible:

-  A web framework, obviously. Probably
   `flask <http://flask.pocoo.org/>`__, though maybe
   `Django <https://www.djangoproject.com/>`__
-  `pandoc <http://pandoc.org/>`__ and a Python wrapper for it, probably
   `pypandoc <https://github.com/bebraw/pypandoc>`__
-  A template system? Ideally it would work for any input format
   ``pandoc`` understands
-  `git <https://git-scm.com/>`__ and a Python wrapper, maybe
   `GitPython <https://github.com/gitpython-developers/GitPython>`__

   -  possibly additional support for other RCS such as DARCS, SVN,
      Mercurial...

-  An editor with live preview would be nice. Maybe
   `retext <https://github.com/retext-project/retext>`__ can be used for
   this, or at least serve as inspiration
