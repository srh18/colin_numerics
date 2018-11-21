Using IRC
=========

IRC is an internet chat channel protocol which we will use to
facilitate cooporation when we're not all in the same room.

In order to use IRC, you need to have an IRC client set up and pointed
at our IRC server. Pidgin is a popular IRC client for Linux and
Windows but you can use any client you like.

For the impatient...
--------------------

For those who know how IRC works, the server is irc.freenode.net and the channel is #mpecdt.

Connecting using Pidgin
-----------------------

These instructions are for Ubuntu Linux but other operating systems
should be similar. For Windows or OS X, visit http://www.pidgin.im/ to
download Pidgin for your operating system.

Check whether Pidgin is installed::

  pidgin

If Pidgin is not installed then (assuming you have sudo; if not, ask your friendly sysadmin)::

  sudo apt-get install pidgin

Now you need to configure pidgin.

* In the Accounts window, choose add account.

  * Select IRC as the protocol.

  * Choose a screen name, for example first initial and surname
    (eg dham for David Ham). Spaces are not allowed.

  * Set the server to irc.freenode.net

  * Select `Auto-login`.

  * Click `Save`.
* In the Accounts window, select `Online` for the IRC account. You should see a new window entitled `irc.freenode.net`.

* In the Buddy List window, select `Add Chat` from the `Buddies` menu.

  * Set the channel to `#mpecdt`

   * Click `Add`.

* In the buddy window:

  * right click `#mpecdt` and select `Auto-join`

  * right click `#mpecdt` again and select `Join`

The main chat window is now titled `#mpecdt` and you can see a chat
window, a typing area and a list of users who are online.

* In the buddy list select `Preferences` from the `Tools` menu.

  * Select `Plugins` and make sure you have the `System Tray Icon` and `Message Notification`
  * Under `Message Notification` select the following items:
    
    * `Chat Windows`

    * `Insert count of new messages into window title`

    * `Set window manager "URGENT" hint`

    * Select any other items you think appropriate.

You can now safely close all the windows except `#mpecdt`, which you
can minimise. You will see a running count of the number of missed
messages in the title bar.

Nicks
-----

A nick is a user name or screen name in irc. Please register the nick
you intend to use with the following instructions. Once you have chosen your nick, you should register it with freenode to make sure it is always available for you.

Checking that your nick is free
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the IRC window, type::

  /msg NickServ identify foo

substituting the nick you are interested in for `foo`. NickServ will
send you a message. If you are lucky, this will be::

  (notice) foo is not registered.

If you get this, proceed to `registering your nick <http://freenode.net/faq.shtml#nicksetup>`_. 

Otherwise, NickServ will say something like::

  (notice) Information on foo (account foo):
  (notice) Registered : Nov 09 14:56:26 2006 (2 years, 12 weeks, 4 days, 21:09:51 ago)
  (notice) Last addr  : n=somsone@server.somewhere.net
  (notice) Last seen  : Nov 09 15:57:36 2006 (2 years, 12 weeks, 4 days, 20:08:41 ago)
  (notice) Email      : noemail

Bad news: someone already owns this nick. Look at the `last seen`
date. Freenode considers that a nick is abandoned if it has not been
seen for 60 days. If the nick has been used in the last two months,
you are probably out of luck and you'll have to choose another
nick. If (as in this case) the nick is out of use for more than 60
days then you can ask a Freenode staffer to free it for you. To do
this, join the `#freenode` channel, which is where the staffers hang
out, and ask politely if the nick can be freed so you can take it
over. Remember that the staffers are all volunteers so in the unlikely
event that nobody is available, you'll have to try again later. Once
they tell you that the nick is clear, you can `register it
<http://freenode.net/faq.shtml#nicksetup>`_.

Identifying
~~~~~~~~~~~

Once you have a registered nick, it is important that you identify
yourself to NickServ every time you log in. Otherwise the system won't
know it's really you and in 60 days time you risk someone else taking
your nick off you. Many irc clients (including Pidgin) will do this
for you automatically if you provide your registered nick password
(incidentally **do not use your Imperial password as your nick
password**). Other clients will allow you to specify commands which
should be run automatically when you log in. You should tell your
client to run::

  /msg NickServ identify passwd 

where `passwd` is your nick password.
