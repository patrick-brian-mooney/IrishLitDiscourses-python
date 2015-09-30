#! /usr/bin/env python
"""Script to post to AutoIrishLitDiscourses.tumblr.com. Really rough sketch of a
script here. Not really meant for public use.

The fact that there isn't real documentation here is intentionally meant to
reinforce that this is a rough draft not meant for public use. Use at your own
risk. My hope is that this script is helpful, but I explicitly disclaim ANY 
RESPONSIBILITY for the behavior of this piece of work. If you don't have the
expertise to evaluate its risks, it's not for you. To put it more bluntly: THIS
SOFTWARE IS OFFERED WITHOUT WARRANTY OF ANY KIND AT ALL.
"""


# Thanks to https://epicjefferson.wordpress.com/2014/09/28/python-to-tumblr/ for first steps here

import math
import datetime
import random
import pprint

import pytumblr

# Set up default values

#Can explicitly set this above zero to force more detailed output
verbosity_level = 2

# Functions

def log_it(message,minimum_level=1):
    """Add a message to the log if verbosity_level is at least minimum_level.
    Currently, the log goes to standard output.
    """
    if verbosity_level >= 4: # set verbosity to at least 4 to get this message output in the debug log
        print "\nDEBUGGING: function log_it() called"
    if verbosity_level >= minimum_level:
        print(message)

def print_usage():
    """Print the docstring as a usage message to stdout"""
    log_it("INFO: print_usage() was called")
    print(__doc__)

def weighted_probability(the_length):
    """Make it more likely to post when more text is built up"""
    return 1 - math.e ** (-2.5e-05 * the_length)

# OK, set up the constants we'll need.
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
normal_tags = ['Irish literature', 'automatically generated text', 'Patrick Mooney', 'dadadodo']
temporary_tags = []
the_content = ''

log_it('INFO: Constants and variables set up; trying to read content',2)

try:
    the_file = open(the_content_path)
    the_content = the_file.read()
    the_file.close()
except IOError:
    log_it('ERROR: Couldn\'t open, or couldn\'t read, or couldn\'t close, the content file',0)
    sys.exit(2)

the_minimum_roll = weighted_probability(len(the_content))
the_dice_roll=random.random()
log_it('INFO: Length of content is ' + str(len(the_content)) + '\n   and the dice roll was ' + str(the_dice_roll) + '\n   And the score necessary to post at that length is ' + str(the_minimum_roll),2)
if len(the_content) > 3000 and the_dice_roll < the_minimum_roll:
    # Make the request
    log_it('INFO: Attempting to post the content', 2)
    the_client.create_text(the_blog_name, state="published", slug=the_slug, tags=normal_tags + temporary_tags, title=the_title, tweet=the_title + ' [URL]', body=the_content)
    log_it('INFO: the_client is: ' + pprint.pformat(the_client),2)
    # Empty the existing content file.
    try:
        log_it('INFO: Opening the file for writing',2)
        the_file = open(the_content_path,'w')
        log_it('INFO: About to truncate file; file position is ' + str(the_file.tell()),2)
        the_file.truncate(0)
        log_it('INFO: About to close file',2)
        the_file.close()
    except IOError:
        log_it('ERROR: unable to fully empty ' + the_content_path,0)
        log_it('... the_file is' + pprint.pformat(the_file),2)
        
else:
    log_it("INFO: Not posting; length of accumulated content is currently " + str(len(the_content)),2)
    
log_it('INFO: We\'re done',2)