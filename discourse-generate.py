#! /usr/bin/env python

# Thanks to https://epicjefferson.wordpress.com/2014/09/28/python-to-tumblr/

import pytumblr
import datetime

# Authenticate via OAuth
the_client = pytumblr.TumblrRestClient(
  'UnEiwRkKrqf9hkAzPtKOpOA1MehBAhhMsdk0wujT7wfnEZBW4M', #consumer_key
  'sIKCOrMFqykmOdoxSMBEhTL7aqIOsIU99tZlOo8SyRFgJ35v6L', #consumer_secret
  'oEf66bgxYDeXneXw1eMDrR5s1nLA8A7r84TxG7Xwp7fPpwIdfY', #token_key
  'KaIAU66YdxX7D5WFvzKXBUeR8O8SoGxiWaIEe60WXYcS1lJGgd' #token_secret
)

the_title = "Discourse of " + datetime.date.today().strftime("%A, %d %B %Y")
the_slug = "discourse-of-" + datetime.date.today().strftime("%Y-%B-%d")
the_blog_name = "AutoIrishLitDiscourses"
the_content_path = "/150/extras.txt"

# Make the request
the_client.create_text(the_blog_name, state="published", slug=the_slug, title=the_title, body=open(the_content_path).read())