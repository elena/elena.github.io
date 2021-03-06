---
layout: base
---

Welcome to Django's News and Updates podcast, the accompanying podcast to Django's blog and updates email.

These are the update for the 28 days up to 29th December 2013

    The latest release of Django is: 1.6.1
    The latest release of Python is: 3.3.3


---

# 0. Security

## Security advisory: ImageField abuse

Posted by Tim Graham on December 2, 2013


    https://www.djangoproject.com/weblog/2013/dec/02/image-field-advisory/

`ImageField` expects a valid image file, but it may allow uploads on non-image content, such as HTML or JavaScript.

Unfortunately, we cannot offer a solution in Django itself.

Rather, you need to take some steps in how you serve static files in order to mitigate this type of attack.

These steps are now outlined in our security guide in the *Django online documentation*:

    https://docs.djangoproject.com/en/dev/topics/security/#user-uploaded-content

We recommend that if you allow image uploads that you check your server's configuration against the online guide.

As always with web development: Always take care with any user uploaded files.

Thanks Rolo Mawlabaux for reporting this vulnerability.

---

# 1. Upcoming cut-off and closing dates:

	1-Jan-2014 (Wed): PyCon 2014, Financial Aid Applications close, Montreal Canada in starting April 9
    6-Jan-2014 (Mon): Django Weekend Cardiff, call for papers deadline for submissions, Cardiff starting February 7
	20-Jan-2014 (Mon): Django 1.7 major feature cut-off

---

# 2. Releases

## Minor Releases ##

    Django 1.6.1 -- 12-Dec-2013

Follow-up bug fix release to the last major release, `Django 1.6` on 6-Nov-2013.

About 2 dozen minor bug and regression fixes, all with ticket numbers greater than #21350 and related mainly to corner-case or environment setup variations.

---

## Major Releases ##

The next major release of Django is 1.7 scheduled for May 2014.

The 1.7 Roadmap schedule is:

-  1.7 alpha -- January 20th (major feature freeze) -- which is to say that 1.7 will be comprised of whatever is in by this date.
-  1.7 beta -- March 6th (complete feature freeze)
-  1.7 release candidate -- May 1st (translations freeze)
-  Final release -- May 15th (assuming a second release candidate is not needed)

Andrew Godwin has stepped up to be the release manager for 1.7, he says:

> We will feature-freeze and branch off a release branch as we roll the beta, and any features that aren't in by this date _will_ have to wait.

More details can be found at Version1.7Roadmap on the wiki.

Posted (in Django Dev) by Andrew Godwin on December 10, 2013

---

# 3. Conferences/Events

### Announcing Django Weekend Cardiff, the UK's first Django conference

Posted by Daniele Procida on December 2, 2013

djangoweekend.org

7 - 9th February

In 2014 Cardiff will host the first-ever Django conference in the UK.

Django Weekend Cardiff will take place at Cardiff University in Wales, from the 7th to the 9th February, for three days of talks, tutorials, code sprints and clinics.

Registration for the event is currently open, as well as a Call for Papers.

Our call for papers is open (deadline for submissions: Monday 6th January 2014)

**Django Weekend Sponsorship**

Django Weekend Cardiff is looking for more sponsors, to help make this event even more memorable and enjoyable for its attendees.

This event has sponsorship from Divio and BullionByPost among others, so please encourage any sponsors you know to help the success of this event.

Please get in touch with Daniele at info@ if you want to ask or discuss anything at all about the event.



Daniele Procida, on behalf of Django Weekend Cardiff.

---

### Announcing DjangoCon EU 2014: "Django Island"

2014.djangocon.eu

13 - 17th May 2014

Hashtag: #DjangoIsland

Tickets aren't on sale yet but should go on sale soon.

Price of the ticket will include meals and accommodation, and the boat to and from the island. Partners are welcome to attend with accommodation and meal rates becoming available for them soon too.

For children up to four-years-old attendance is free, including accommodation and food. They'll be providing rates for children over four soon.

Talks for the conference will begin on Tuesday 13th May at 10am.

---

### Other Conferences/Events

	2014 Feb 7-9 -- Django Weekend Cardiff
	2014 Feb 22-23 -- PyCon Philipines (tickets not announced yet)
	2014 Apr 9-17 -- PyCon 2014, Montreal Canada (early bird sold out)
	(2014 Apr 9-10 -- Tutorials)
	(2014 Apr 11-13 -- Conference)
	(2014 Apr 14-17 -- Sprints)

    2014 May 13-17 -- DjangoConEU, L'île des Embiez is located on the Côte d'Azur, between Toulon and Marseille. (no tickets announced yet, should be this week)
	2014 Jul 21-27 -- Euro Python 2014 in Berlin Germany. (no tickets announced yet)
	2014 Aug 1-5 -- PyCon AU
	2014 Labor-Day weekend September -- DjangoCon 2014, Portland Oregon

---

# 4. News

## Kogan donates A$10,000 to the DSF

Posted by Russell Keith-Magee on December 16, 2013

The Django Software Foundation (DSF) is proud to announce that we have just received an A$10,000 (around US$9,000) donation from Kogan.com.

Kogan.com is one of Australia's most recognisable entrepreneurial brands and values technology at its core.

Kogan selected Django as its website platform in 2006 because of it’s scalable design, flexibility and burgeoning open source community. Django has been (and still is) Kogan’s platform of choice throughout the company’s rapid growth as Australia’s largest online retailer.

Kogan & its software engineering team give a big shout out to everyone in the Django community and extend a special thanks to the team behind significant ORM speed improvements in the Django 1.6 release!

The team is excited to have built several world-first e-commerce innovations on a platform that is so enjoyable to work with!

The DSF will use these funds to help support Django development sprints, to provide financial aid to people in the Django community to attend Django and Python events, and to support any other activities that benefit the Django community.

A huge thanks to Ruslan Kogan and his team for this generous contribution!

---

## Other News

The esteemed British core contributors Andrew Godwin and Simon Willison are looking to be based in the USA in the new year.

Simon recently having moved back and Andrew announcing on Django Dev that he's "moving to the USA during this release cycle (January most likely)".

---

# 5. Community requests


## Call for Volunteers: DjangoCon US 2014 Website

Posted by Russell Keith-Magee on December 16, 2013

It might be 9 months away, but work is already underway planning DjangoCon US 2014. One of the first pieces of work required is the conference website. Last year's website design was met with some criticism, so this year, The Open Bastion (the organizers of DjangoCon US) is calling for volunteers.

If you are interested in helping out with the design of this year's conference website, jump onto the DjangoCon organizers mailing list, or email Steve Holden from Open Bastion directly (steve@holdenweb.com).

If website design isn't your thing, but you're still interested in volunteering, you're also welcome to join the organisers mailing list -- we'll need lots more volunteers before the big event arrives!

---

If you have any community requests for volunteers, support, sponsorship or other projects, please email scoop@djangoproject.com to be posted here.

---

These show notes are "open source" on github so please be sure to make any corrections or additions at: github.com/elena/django-news

---

# Lastly: Summary of Django Dev this month

Brief and loose summary of what was discussed on the Django Development mailing list during the last 28 days (excluding announcements and support enquiries).

This is very much a summary so please go and read and contribute to the actual threads if there's anything mentioned in your field of interest.

---

### 3-Dec-2014 Security Advisory: ImageField abuse

Jacob Kaplan-Moss

An HTML file can be uploaded as an image if that file contains a valid PNG header followed by malicious HTML.

This file will pass verification of the libraries that Django uses for ImageField image processing (PIL or Pillow).

When this file is subsequently displayed to a user, it may be displayed as HTML depending on the type and configuration of your web server.

No bulletproof technical solution exists at the framework level to safely validate all user uploaded file content, however, there are some other steps you can take to mitigate these attacks:

One class of attacks can be prevented by always serving user uploaded content from a distinct Top Level Domain (TLD). This will protect against same-origin policy protections such as cross site scripting.


Beyond this, applications may choose to define a whitelist of allowable file extensions for user uploaded files and configure the web server to only serve such files.

---

### 25-Nov-2013 Using setuptools to make django-admin.py runnable on Windows (#21340)

Remram

Discussing django-admin.py being problematic, particularly on Windows and setup tools.

Florian Apolloner, Donald Stufft () and Vernon Cole all weigh in wiht different points of view pertaining to django setup.

Discussion ensues regarding:

- Wheels with Python 3.3 alleviating a lot of this pain
- the use of `setuptools` is not recommended
- needing a windows specific Wheel

---

### 4-Dec-2013 Problem with number format when not using L10N

Yonel Ceruto González

Related Ticket: #21544 Problem with number format when not using L10N (closed won't fix)

Discussion threshing out the use of thousands separator in L10N.

---

### 7-Dec-2013 Self-referenced template recursion handling

Unai Zalakain

Related Ticket: #15053 Make templates more reusable by Improving template loading algorithm to avoid extending infinite recursion (11-Jan-2011, Accepted)

> Pablo Martín (goinnn[0]) and I have been working on self-referenced template
> recursion handling for the past few weeks. The idea is that when a template
> references itself when extending, recursion is avoided by skipping the current
> template loader (ticket #15053[1]).

This discussion reinforces that this would be a really nice feature to have but this is a non-straightforward feature that has interesting consequences.

To quote Pablo Martin (Goinnn):

> ... if we allow that a app template
> overwrite with self-reference another app template the template
> development will be a chaos ...

24 posts/9 authors

Unai and Pablo still seem to be working on this ticket and this discussion will undoubtedly continue.

---

### 10-Dec-2013 Enable longer wait in StoppableWSGIServer.shutdown / hardcoded parameter

is_null

Shai Berger and Russ Magee

Proposing a feature to make StoppableWSGIServer.shutdown wait time configurable, as it's currently hard-coded to being 2 seconds.

---

### 16-Dec-2013 App-loading reloaded

Aymeric Augustin

Related ticket: #3591 add support for custom app\_label and verbose\_name February 2007

Summary: As he says there isn't really any tldr here, it's too detailed a project to gloss over as Many related issues have been closed as duplicates of #3591. As a consequence, its scope has become frighteningly ambitious over the years. This is certainly one of the reasons why it hasn’t been resolved yet.

Aymeric has broken the ticket up and his pre-Xmas goals have been as follows:

- 1) Allow apps without a models module or package
- 2) Provide verbose\_name for the admin
- 6) Clarify the app cache population sequence
- 7) Enforce consistency between the contents of INSTALLED_APPS and the AppCache

These patches will be merged for 1.7 alpha.

He is trying to `Provide a reliable initialization signal` also during this period.

He has a range of other ideas and goals also which are worth reading.

Relatedly Curtis Maloney asked on 22-Dec about signal handling and circular imports.

charettes (Simon) responds:

> Since Django 1.7 you can lazily reference model signal sender, it might help solving your circular import issues.
>
> It seems providing a reliable initialization signal is one of Aymeric's main goal.

---

## South/Migration Database discussions

---

### 18-Dec-2013 Django ORM support for NoSql databases

parisrocks

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

---

### 19-Dec-2013 LiveServerTestCase, and override_settings(DEBUG=True)

Harry Percival

TestRunner forces DEBUG=False

The discussion surrounded some unusual behaviour that was being caused by the TestRunner's debug setting being `False` by default.

Russell instead explained that it had to do with the layers of serving

Aymeric

Related ticket: #21451 16-Nov-2013 (6 weeks ago)

---

### 20-Dec-2013 SchemaEditor Enhancements (3)

Michael Manfre

He's working on MSSql support for 1.7 and there is a discussion regarding a range of schema details.

---

### 21-Dec-2013 Improving aggregate support (#14030)

Josh Smeaton

Related Ticket: #14030 September 2010 -- Use F() objects in aggregates

Anssi Kääriäinen
> A lot has already been done. The main part of the work has been bug fixing, code cleanup and join generation changes.
>
> The next part is introducing custom lookups for 1.7, and later on in 1.8 allow usage of custom lookups in every part of the ORM

Josh has submitted a patch to simplify the existing F() evaluation and is looking for feedback.

4 posts 95 views -- Improve annotation and aggregation (4)

---

### 23-Dec-2013 Getting user's real IP address in Django

Val Neekman

Proposing including `django-ipware` in core.

IP addresses can be spoofed

> It makes sense not to provide a formal API

---

### 23-Dec-2013 Saving deleted code from Django source code

Vajrasky Kok

Proposing Recapitalisation filter, he's posted this on activestate recipes.

Russ reminds us when doing this to include the correct licensing

You can include a snippet like this:

	\# This is derived from code provided by the Django Project.
	\# Original code is licensed under the terms of the BSD license.
	\# See https://github.com/django/django/blob/master/LICENSE for full original license terms

---

### 24-Dec-2013 Django 1.7 - Named migration directory

Val Neekman

Andrew Godwin confirmed that a setting called `MIGRATION_MODULES` already exists
