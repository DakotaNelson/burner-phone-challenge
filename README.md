# burner-phone-challenge
Can you identify a burner phone from a stream of (fake) AT&amp;T Hemisphere data?

Inspired by Kenneth Lipp on [Twitter](https://twitter.com/kennethlipp/status/848565438061654017).

Specifically, this passage was interesting to me:

> Let's say a narcotics task force is trying to maintain a wiretap on a drug dealer, but the drug dealer uses prepaid "burner" phones and is constantly changing his number.
> However, from each new phone number, this drug dealer makes calls to may of the same people - his mom, girlfriend, a supplier - and also makes most of his calls from a limited range of locations. Because AT&T can analyze so many call-detail records with such well-developed custom software, it can easily track these patterns to infer which unknown number is really the suspect. Since it can do this in real time by mining its live data stream, by the time the suspect burns an old phone and makes a few calls from his new one, he's back in the net.

AT&T can do this. Can you?

First though, you need some data to play with. So I made some up. It's definitely not accurate, because I don't have any AT&T data to work from, but it should be close enough to give you an idea of what AT&T (and law enforcement, by extension) can do. If you have ideas for how to make it more accurate, or some legitimate (anonymized, please!) data to build a generative model with, that would be neat and you should [let me know](https://strikersecurity.com/contact/).


And so,

The Rules
=========
Coming soon


Usage
=====

Install dependencies (using a virtualenv, preferably):
`virtualenv venv --python=python3 && source venv/bin/activate`
`pip install networkx`

Do the thing:
`python src/generate.py`


Big Todos
=========
  -[] make locations/contacts called non-uniformly (i.e call some friends more than others, be in some places more than others)
  -[] make agents coordinate; if someone switches numbers, their friends should stop calling the old one


See Also
========

Example of how law enforcement uses these call records: https://web.archive.org/web/20170621072311/http://wispd.org/attachments/2015Conference/pdf/Mattert_Weitz_Understanding%20and%20Plotting%20Cell%20Phone%20Information.pdf
