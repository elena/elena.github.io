Welcome to Django's News and Updates podcast, the accompanying podcast to Django's blog and updates email.

These are the update for the 28 days up to 29th December 2013

The latest release of Django is: 1.6.1
The latest release of Python is: 3.3.3

I'm Elena Williams.

First thing is upcoming cut-off and closing dates:

1st Jan Application are closing for PyCon


## Security ##

Security advisory: ImageField abuse

There's been a report of a means of allowing an HTML file to be uploaded via Django's ImageField.

This provides an attack vector for a user to upload something malicious like a phishing form or some kind of cookie stealing script.

Unfortunately, a solution cannot be offered within Django itself.

Rather, steps need to be taken in how media files are served in order to mitigate this type of attack.

It's recommended that if you allow image uploads that you check your server's configuration against the official Django security guide in the online docs.

--

An HTML file can be uploaded as an image if that file contains a valid PNG header followed by malicious HTML.

This file will pass verification of the libraries that Django uses for ImageField image processing (PIL or Pillow).

When this file is subsequently displayed to a user, it may be displayed as HTML depending on the type and configuration of your web server.

No bulletproof technical solution exists at the framework level to safely validate all user uploaded file content, however, there are some other steps you can take to mitigate these attacks:

One class of attacks can be prevented by always serving user uploaded content from a distinct Top Level Domain (TLD).

This prevents any exploit blocked by same-origin policy protections such as cross site scripting. For example, if your site runs on example.com, you would want to serve uploaded content (the MEDIA_URL setting) from something like usercontent-example.com.

Beyond this, applications may choose to define a whitelist of allowable file extensions for user uploaded files and configure the web server to only serve such files.

As always with web development: Take care with any user uploaded files.

Thanks Rolo Mawlabaux for the report.
Posted by Tim Graham on December 2, 2013


## Major Releases ##

none.

## Minor Releases ##
---

Django 1.6.1 -- 12-Dec-2013

(Django 1.6 -- 6-Nov-2013)

About 2 dozen minor bug and regression fixes, all with ticket numbers greater than #21350.





Updates
---



Upcoming Conferences/Events
---

Announcing Django Weekend Cardiff, the UK's first Django conference
In 2014 Cardiff will host the first-ever Django conference in the UK.

Django Weekend Cardiff will take place at Cardiff University in Wales, from the 7th to the 9th February, for three days of talks, tutorials, code sprints and clinics.

Registration for the event is now open, as well as a Call for Papers.

Cardiff
Cardiff is the capital city of Wales. It's easy to reach; we've provided some information about how to get here, where to stay and what else you can do while in Cardiff.

Sponsorship
Django Weekend Cardiff is looking for more sponsors, to help make this event even more memorable and enjoyable for its attendees.

Please get in touch if you want to ask or discuss anything at all about the event.

Thanks, and we look forward to welcoming you to Cardiff in 2014.

Daniele Procida, on behalf of Django Weekend Cardiff.

Posted by Daniele Procida on December 2, 2013

--
2014.djangocon.eu
13 - 17TH MAY 2014
@djangocon
#DjangoIsland

Tickets aren't on sale yet but should go on sale soon.

Price of the ticket will include meals and accommodation, and the boat to and from the island. Partners are welcome to attend with accommodation and meal rates becoming available for them soon too.

Everything is completely free for children up to four-years-old, including accommodation and food. They'll be providing rates for children over four soon.

Talks for the conference will begin on Tuesday 13th May at 10am.


News
---
Call for Volunteers: DjangoCon US 2014 Website
It might be 9 months away, but work is already underway planning DjangoCon US 2014. One of the first pieces of work required is the conference website. Last year's website design was met with some criticism, so this year, The Open Bastion (the organizers of DjangoCon US) is calling for volunteers.

If you are interested in helping out with the design of this year's conference website, jump onto the DjangoCon organizers mailing list, or email Steve Holden from Open Bastion directly (steve@holdenweb.com).

If website design isn't your thing, but you're still interested in volunteering, you're also welcome to join the organisers mailing list -- we'll need lots more volunteers before the big event arrives!


Posted by Russell Keith-Magee on December 16, 2013


Community requests
---
Kogan donates A$10,000 to the DSF
The Django Software Foundation (DSF) is proud to announce that we have just received an A$10,000 (around US$9,000) donation from Kogan.com.

Kogan.com is one of Australia's most recognisable entrepreneurial brands and values technology at its core. Kogan selected Django as its website platform in 2006 because of it’s scalable design, flexibility and burgeoning open source community. Django has been (and still is) Kogan’s platform of choice throughout the company’s rapid growth as Australia’s largest online retailer.

Kogan & its software engineering team give a big shout out to everyone in the Django community and extend a special thanks to the team behind significant ORM speed improvements in the Django 1.6 release! The team is excited to have built several world-first e-commerce innovations on a platform that is so enjoyable to work with!

The DSF will use these funds to help support Django development sprints, to provide financial aid to people in the Django community to attend Django and Python events, and to support any other activities that benefit the Django community.

A huge thanks to Ruslan Kogan and his team for this generous contribution!

Posted by Russell Keith-Magee on December 16, 2013




Summary of Django Dev this month
----

## 16th Dec: Aymeric Augustin
App-loading reloaded (12)
#3591 February 2007

Summary: As he says there isn't really any tldr here, it's too detailed a project to gloss over as Many related issues have been closed as duplicates of #3591. As a consequence, its scope has become frighteningly ambitious over the years. This is certainly one of the reasons why it hasn’t been resolved yet.

Aymeric has broken the ticket up and his pre-Xmas goals have been as follows:

1) Allow apps without a models module or package
2) Provide verbose_name for the admin
6) Clarify the app cache population sequence
7) Enforce consistency between the contents of INSTALLED_APPS and the AppCache

These patches will be merged for 1.7 alpha.

3) Provide a reliable initialization signal

He has a range of other ideas and goals also which are worth reading.

DjDev Conversation: App-loading reloaded

Relatedly a question was asked on 22-Dec about signal handling and circular imports, which

 providing a reliable initialization signal is one of Aymeric's main goal

--

### South/Migration Database discussions
3 posts 34 views -- Django 1.7 - Named migration directory (3)
3 posts 34 views -- SchemaEditor Enhancements (3)



--

### Using

4 posts 95 views -- Improve annotation and aggregation (4)
5 posts 92 views -- Improving aggregate support (#14030) (5)
### Use F() objects in aggregates
\#14030 September 2010

--

19 December
Harry Percival
DjDev Conversation: LiveServerTestCase, and override_settings(DEBUG=True)

\#21451 16-Nov-2013 (6 weeks ago)

TestRunner forces DEBUG=False

The discussion surrounded some unusual behaviour that was being caused by the TestRunner's debug setting being `False` by default.

Russell instead explained


### Django ORM support for NoSql databases
16 posts 163 views -- Django ORM support for NoSql databases

parisrocks 18-Dec
Asking about official support for NoSQL databases like Cassandra or MongoDB.

A lively discussion ensued with: Tom Evans, Chris Wilson, Javier Guerra, Aymeric Augustin, Karen Tracey, Alioune Dia

Javier kindly reposted RKMs response to the same question from 26-Mar-2013.

Alex Burgel, a committer to `django-norel` provided some further information:

>We have supported backends for mongodb and google appengine. There are others out there, but they're not part of the nonrel project. So knowing what it takes to use the django ORM to work with a NoSQL DB, I hope I can provide some useful information.
>
> 1. Things you can do on a SQL system that you can't on NoSQL. - The big ones are (conditionally) joins and aggregates,

He says to this:

> My perspective is that this is the trade off you make when choosing your datastore, so you should know this going in.
>
> 2. Things you can do on NoSQL that you can't in SQL.
> 3. Assumptions django makes about the underlying datastore.

Aymeric says:

> Currently, the best option is (probably) `django-nonrel`. We're open to suggestions that help django-nonrel but we aren't working towards a merge.

He goes on to say:
> So, while it's technically possible to implement parts of the ORM's APIs on top of a non-relational database proved by the django-nonrel project isn't much enthusiasm because the APIs are optimized for joins, which SQL databases are good at while NoSQL storage engines aren't.

Russell and Aymeric agree that "the interest has faded" in implementing an ODM in to Django core.

Aymeric adds:

> since there's no such thing as "common NoSQL features", each datastore
> would need its own modifications, so i think the common attitude is
> that most of these features don't belong in the ORM.

Here are some key quotes from Russell's closing of the disucssion:

> I'm not currently confident that NoSQL stores are at a sufficient level of maturity that this sort of abstraction is possible (or plausible) for anything beyond trivial examples. Remember, SQL has been a work in progress for 20 years as a *published* standard (and another 20 prior to that as an informal one) - the common ground in SQL is well understood at this point.
>
> Independent of whether NoSQL gets added to core, _meta would definitely benefit from an implementation cleanup and formalisation as a backwards-compatible API.
>
> (Actually… this might make a good GSoC project…)



1 post 23 views -- Saving deleted code from Django source code (1)
1 post 37 views -- Change Cache Middleware Via Setting? (1)
1 post 41 views -- TestCase can produce surprising failures (1)
1 post 59 views -- [ANNOUNCE] Django 1.6.1 released (1)
1 post 72 views -- Security Advisory: ImageField abuse (1)
2 posts 46 views -- Wizard problem (2)
2 posts 50 views -- Periodic Updates (2)
2 posts 52 views -- How to install Django? (2)
2 posts 55 views -- How to integrate Postgresql db with Django,so that data will be retrieved from that postgresql db table and show browser via html (2)
3 posts 24 views -- Registering signal handlers (3)
3 posts 42 views -- Strange crash with ugettext_lazy when accent letter (3)
3 posts 88 views -- FR: Setting for CSRF Header (pull-request included) (3)
4 posts 176 views -- Travis support (again)
4 posts 51 views -- Getting user's real IP address in Django (4)
4 posts 54 views -- Enable longer wait in StoppableWSGIServer.shutdown / hardcoded parameter (4)
4 posts 63 views -- Django admin, 'Save as new' option, duplicate m2m relations (4)
6 posts 492 views -- RawQuerySet as subquery when used with an __in filter (6)
6 posts 64 views -- LiveServerTestCase, and override_settings(DEBUG=True) (6)
6 posts 66 views -- South data-migration and custom save() method (6)
7 posts 2606 views -- HTTP PUT request (7)
9 posts 164 views -- Creating a minimal custom user model. Seems last_login is required. Should it be? (9)
10 posts 101 views -- Problem with number format when not using L10N (10)
10 posts 481 views -- 1.7 Release Schedule (10)

13 posts 146 views -- Using setuptools to make django-admin.py runnable on Windows (#21340) (13)

24 posts 197 views -- Self-referenced template recursion handling (24)



other "important" packages? Criteria for "important" could be something like:

potential to be integrated
was once part of project
major work by core contributor
