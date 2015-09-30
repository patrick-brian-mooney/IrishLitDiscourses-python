#! /usr/bin/env python
"""Script to post to AutoIrishLitDiscourses.tumblr.com. Really rough sketch of a script here. Not really meant for public use.
"""


# Thanks to https://epicjefferson.wordpress.com/2014/09/28/python-to-tumblr/ for first steps here

import pytumblr
import datetime

# Authenticate via OAuth
the_client = pytumblr.TumblrRestClient(
  'FILL ME IN', #consumer_key
  'FILL ME IN', #consumer_secret
  'FILL ME IN', #token_key
  'FILL ME IN' #token_secret
)

the_title = "Discourse of " + datetime.date.today().strftime("%A, %d %B %Y")
the_slug = "discourse-of-" + datetime.date.today().strftime("%Y-%B-%d")
the_blog_name = "AutoIrishLitDiscourses"
the_content_path = "/150/extras.txt"
the_tags = ['Irish literature', 'automatically generated text', 'Patrick Mooney', 'dadadodo']
the_content = open(the_content_path, 'r').read()

if len(the_content) > 3000:
    the_tags = ['Irish literature', 'automatically generated text', 'Patrick Mooney', 'dadadodo']
    the_content = open(the_content_path, 'r').read()
    the_text.seek(0)
    the_text.truncate(0)
    the_text.close()