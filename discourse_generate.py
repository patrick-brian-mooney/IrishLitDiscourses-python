#! /usr/bin/env python3
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
import sys

import patrick_logger    # From https://github.com/patrick-brian-mooney/personal-library
import social_media      # From https://github.com/patrick-brian-mooney/personal-library
from social_media_auth import Irish_lit_discourses_client

# Set up default values
patrick_logger.verbosity_level = 3


# Functions

def print_usage():
    """Print the docstring as a usage message to stdout"""
    patrick_logger.log_it("INFO: print_usage() was called")
    print(__doc__)

def weighted_probability(the_length):
    """Make it more likely to post when more text is built up"""
    return 1 - math.e ** (-2.5e-05 * (the_length-3000))


the_title = "Discourse of " + datetime.date.today().strftime("%A, %d %B %Y")
the_blog_name = "AutoIrishLitDiscourses"
the_content_path = "/150/extras.txt"
normal_tags = ['Irish literature', 'automatically generated text', 'Patrick Mooney', 'dadadodo']
temporary_tags = []
the_content = ''

patrick_logger.log_it('INFO: Constants and variables set up; trying to read content', 2)

try:
    the_file = open(the_content_path)
    the_content = the_file.read()
    the_file.close()
except IOError:
    patrick_logger.log_it("ERROR: Couldn't open, or couldn't read, or couldn't close, the content file", 0)
    sys.exit(2)

the_maximum_roll = weighted_probability(len(the_content))
the_dice_roll = random.random()
patrick_logger.log_it('INFO: Length of content is ' + str(len(the_content)) + '\n   and the dice roll was ' + str(the_dice_roll) + '\n   And the maximum score to post at that length is ' + str(the_maximum_roll), 2)
if the_dice_roll < the_maximum_roll:
    # Make the request
    patrick_logger.log_it('INFO: Attempting to post the content', 2)
    the_lines = ["<p>" + the_line.strip() + "</p>" for the_line in the_content.split('\n\n')]
    patrick_logger.log_it("the_lines: " + pprint.pformat(the_lines))
    the_content = "\n\n".join(the_lines)
    patrick_logger.log_it("the_content: \n\n" + the_content)
    the_status = social_media.tumblr_text_post(Irish_lit_discourses_client, normal_tags + temporary_tags, the_title, the_content)
    # Empty the existing content file.
    try:
        patrick_logger.log_it('INFO: Opening the file for writing', 2)
        the_file = open(the_content_path, 'w')
        patrick_logger.log_it('INFO: About to truncate file; file position is ' + str(the_file.tell()), 2)
        the_file.truncate(0)
        patrick_logger.log_it('INFO: About to close file', 2)
        the_file.close()
    except IOError:
        patrick_logger.log_it('ERROR: unable to fully empty ' + the_content_path, 0)
        patrick_logger.log_it('... the_file is' + pprint.pformat(the_file), 2)
else:
    patrick_logger.log_it("INFO: Not posting; length of accumulated content is currently " + str(len(the_content)), 2)

patrick_logger.log_it("INFO: We're done", 2)
