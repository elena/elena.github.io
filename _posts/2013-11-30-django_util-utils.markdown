---
layout: post
title: "Django: Util/Utils 2013 redux"
date: "2013-11-30 13:12:14 +1100"
categories: django
---


Quick update now we're happily living in version 1.6 thought I would double check progress since [Jacob's](http://jacobian.org/writing/util/) famous post from 8-Jun-2010.


As at 30-Nov-2013:

    u:django 18:12:45$ find . -name "util.py"
    ./contrib/admin/util.py
    ./contrib/gis/db/backends/util.py
    ./db/backends/util.py
    ./forms/util.py
    ./utils/unittest/util.py

    u:django 18:12:47$ find . -name "utils.py"
    ./contrib/admindocs/utils.py
    ./contrib/auth/tests/utils.py
    ./contrib/comments/views/utils.py
    ./contrib/formtools/utils.py
    ./contrib/gis/tests/utils.py
    ./contrib/messages/utils.py
    ./contrib/staticfiles/utils.py
    ./core/cache/utils.py
    ./core/files/utils.py
    ./core/mail/utils.py
    ./core/management/utils.py
    ./db/utils.py
    ./http/utils.py
    ./test/utils.py


---

[http://jacobian.org/writing/util/](http://jacobian.org/writing/util/)


<div style="width: 350px; float: left;">
<p>Jacob&#39;s June 2010 list for the record:</p>

<div class="highlight"><pre><code class="text language-text" data-lang="text">django/contrib/admin/util.py
django/contrib/admindocs/utils.py

django/contrib/comments/views/utils.py
django/contrib/formtools/utils.py
django/contrib/gis/db/backends/util.py
django/contrib/gis/tests/utils.py
django/contrib/localflavor/it/util.py
django/contrib/localflavor/se/utils.py
django/contrib/localflavor/uy/util.py
django/contrib/messages/utils.py
django/core/files/utils.py
django/core/mail/utils.py
django/db/backends/util.py
django/db/utils.py
django/forms/util.py
django/http/utils.py
django/test/utils.py
tests/regressiontests/forms/util.py
</code></pre></div>
</div>

<div style="width: 350px; float: right;">
<p>Nov 2013 list formatted <a title="through the wonder of emacs">similarily</a>:</p>

<div class="highlight"><pre><code class="text language-text" data-lang="text">django/contrib/admin/util.py
django/contrib/admindocs/utils.py
django/contrib/auth/tests/utils.py
django/contrib/comments/views/utils.py
django/contrib/formtools/utils.py
django/contrib/gis/db/backends/util.py
django/contrib/gis/tests/utils.py
django/contrib/messages/utils.py
django/contrib/staticfiles/utils.py
django/core/cache/utils.py
django/core/files/utils.py
django/core/mail/utils.py
django/core/management/utils.py
django/db/backends/util.py
django/db/utils.py
django/forms/util.py
django/http/utils.py
django/test/utils.py
django/utils/unittest/util.py
</code></pre></div>
</div>