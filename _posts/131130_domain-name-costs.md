Been on a bit of a domain name buying frenzy lately :P

Cheapest was $4.99 at crazydomains.

It was annoying me that I could work out how much the increments cost per annum in my head.

Per Guido's immortal words: it makes a great calculator:

    ## Hand typing in the prices
    ## apparently get progressively more expensive per annum.
    >>> +13.98/2
    6.99
    >>> 22.97/3
    7.656666666666666
    >>> 40.95/5
    8.190000000000001
    >>> 8.59
    8.59

    ## There must be a pattern here. Thaaank you python.

    ## OK, all the prices in a list of tuples:
    >>> a = [(13.98,2),(22.97,3),(40.95,5),(85.90, 10)]

    ## process them per year, excluding the initial $4.99
    >>> for x in a:
    ...   (x[0]-4.99)/x[1]
    ...
    4.495
    5.993333333333332
    7.192
    8.091000000000001

    # whoops need to divide by num years excluding first *year* as well. der.

    >>> for x in a:
    ...   (x[0]-4.99)/(x[1]-1)
    ...

    ## BOOM!

    8.99
    8.989999999999998
    8.99
    8.990000000000002
    >>>

So they don't tell you it's 4.99 for the first year and 8.99 thereafter but it is.

---

As an aside it seems as though godaddy has "changed".

I used to rely on them to be OTT in throwing options and waaay too many suggestions at me, mainly I hated this but it was good for a purpose. Like now when I'm domain-storming.

Also, I seem to be locked in to either the Canadian (?!) site while normally browsing, or the Australian site when I'm in <span title="something which I am more and more these days">incognito</span> mode.