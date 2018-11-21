Using the tools of scientific computing
=======================================

An important part of the MPECDT is scientific computing, and doing
scientific computing efficiently and robustly to obtain reliable
results requires some familiarity with the tools of the trade.

Revision control with git and Bitbucket
---------------------------------------

Revision control is a mechanism for recording and managing different
versions of changing software. This enables changes to be tracked and
helps in the process of debugging code, and in managing conflicts when
more than one person is working on the same project. Revision control
can be combined with online hosting to provide secure backups and to
enable you to work on code from different locations.

We will be using the revision control system `git
<http://git-scm.com/>`_, which is the current state of the art and is
widely adopted. We'll be combining git with the online hosting service
`Bitbucket <http://bitbucket.org>`_. Bitbucket is one of the two
leading revision control hosting services, the other is `GitHub
<http://github.org>`_. Bitbucket has the advantage that it offers
unlimited private repositories if you register with a university email
address.


Getting started with git and Bitbucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The good folks over at Bitbucket have fortunately provided a good
tutorial for getting started with the tools. The tutorial is called
`Bitbucket 201
<https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+201+Bitbucket+with+Git+and+Mercurial>`_
and you'll want to work through that first. Bitbucket supports two
revision control systems: git and mercurial. We'll be exclusively
using git so you can ignore the instructions in the tutorial for using
mercurial.

Using git and Bitbucket for your MPECDT work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The way to do your computational coursework is to create your own fork
of the MPECDT repository on bitbucket. 

* Navigate to `https://bitbucket.org/mpecdt/mpecdt
  <https://bitbucket.org/mpecdt/mpecdt>`_.
* Click on the ellipsis (...) on the left of the screen, and then
  `Fork`.
* On the next page you can choose if you want your fork to be private
  or publicly visible, and then create the fork.
* Clone a copy of your fork onto your machine using::

    git clone <link>
   
  where `<link>` is the ssh link for your clone.

You're going to need to update your fork from time to time for new
material the lecturer uploads during the module. For this reason
you'll need to tell your local clone of the `MPECDT` repository about
the original fork as well as your fork. From inside the your
repository, type::

  git remote add mpecdt https://bitbucket.org/mpecdt/mpecdt.git

Now you can update your fork to the current version of the original::

  git checkout master
  git fetch mpecdt
  git merge mpecdt/master

You should now push the change back to your own fork on Bitbucket::

  git push

More git resources
~~~~~~~~~~~~~~~~~~

There is a handy cheat sheet of git commands `here
<https://www.atlassian.com/dms/wac/images/landing/git/atlassian_git_cheatsheet.pdf>`_
as well as much more git documentation `at the official site
<https://git-scm.com/documentation/external-links>`_.

Sharing your problems with gists
--------------------------------

At some points during the module, you're sure to create bugs in your
code that you don't know how to fix. Since the whole class is not
located in one place, you'll need a convenient way to share a piece
of code or output with the lecturer and the class. GitHub (the other
hosting service) provides this facility, which they call `gists`. For
this you'll want a GitHub account so head over there and `sign up
<https://github.com>`_.

Once you've signed up and logged in, you can navigate to
`https://gist.github.com <https://gist.github.com>`_ and there's a very simple webpage into which
you can paste your code or output. You should also set the language so
that GitHub formats your gist correctly. Click `create public gist`
and you're done. You can then paste the URL of your gist page into an
email or into the IRC chat channel (see below).

Chatting with the class on IRC
------------------------------

An internet chat channel is a great way to communicate about ongoing
work, to post gists and to ask others for help. We'll be using IRC
(internet relay chat) for this purpose and there are instructions on
how to do this :doc:`here <irc>`.
