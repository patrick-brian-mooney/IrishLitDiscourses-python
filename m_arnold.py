#! /usr/bin/env python3
"""Script to post to AutoIrishLitDiscourses.tumblr.com. Really rough sketch of a
script here. Not really meant for public use.

There are multiple scripts that post to this Tumblr account. This particular
script is meant to impersonate Matthew Arnold, based on his book /Celtic
Literature/.

The fact that there isn't real documentation here is intentionally meant to
reinforce that this is a rough draft not meant for public use. Use at your own
risk. My hope is that this script is helpful, but I explicitly disclaim ANY
RESPONSIBILITY for the behavior of this piece of work. If you don't have the
expertise to evaluate its risks, it's not for you. To put it more bluntly: THIS
SOFTWARE IS OFFERED WITHOUT WARRANTY OF ANY KIND AT ALL.
"""


# Thanks to https://epicjefferson.wordpress.com/2014/09/28/python-to-tumblr/ for first steps here

import datetime
import random
import pprint
import sys
import subprocess

from discourse_post import post_to_tumblr
import patrick_logger # From https://github.com/patrick-brian-mooney/personal-library

# Set up default values
patrick_logger.verbosity_level = 2


# Functions

def print_usage():
    """Print the docstring as a usage message to stdout"""
    patrick_logger.log_it("INFO: print_usage() was called")
    print(__doc__)


the_title = "Matthew Arnold's Guest Lecture of " + datetime.date.today().strftime("%A, %d %B %Y")
the_blog_name = "AutoIrishLitDiscourses"
the_content_path = "/150/extras.txt"
the_tags = ['Matthew Arnold', 'Celtic Literature', 'guest lecture', 'Irish literature', 'automatically generated text', 'Patrick Mooney', 'dadadodo']
the_content = ''

patrick_logger.log_it('INFO: Constants and variables set up; generating content', 2)

story_length = random.choice(list(range(80, 120)))
the_content = subprocess.check_output(["dadadodo -c " + str(story_length) + " -l sources/m.arnold/CelticLiterature.dat -w 10000"], shell=True).decode()
the_lines = ["<p>" + the_line.strip() + "</p>" for the_line in the_content.split('\n\n')]
the_content = "\n\n".join(the_lines)
patrick_logger.log_it('INFO: Attempting to post the content', 2)
patrick_logger.log_it("the_content: \n\n" + the_content)

post_to_tumblr(type='text', tags=the_tags, title=the_title, body=the_content)

patrick_logger.log_it('INFO: We\'re done', 2)
