#!/usr/bin/env python3
"""Unit that posts discourses to http://autoirishlitdiscourses.tumblr.com/
Abstracted out to another unit largely so the logic doesn't have to be repeated
for every guest lecturer, and so I don't have to keep redacting the
authentication constants. 
"""

import pprint
from tumblpy import Tumblpy
import patrick_logger # From https://github.com/patrick-brian-mooney/personal-library

# OK, set up the constants we'll need.
the_client = Tumblpy(
   'FILL ME IN', #consumer_key
   'FILL ME IN', #consumer_secret
   'FILL ME IN', #token_key
   'FILL ME IN' #token_secret
)

def post_to_tumblr(**kargs):
    blog_url = the_client.post('user/info')
    blog_url = blog_url['user']['blogs'][0]['url']
    the_status = the_client.post('post', blog_url=blog_url, params=kargs)
    patrick_logger.log_it('INFO: the_status is: ' + pprint.pformat(the_status), 2)
    patrick_logger.log_it('INFO: the_client is: ' + pprint.pformat(the_client), 2)

if __name__ == "__main__":
    print("no tests for this unit")
