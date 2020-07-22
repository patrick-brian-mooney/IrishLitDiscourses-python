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


import datetime, random, pprint, sys, subprocess

import logger           # From https://github.com/patrick-brian-mooney/personal-library
import social_media             # From https://github.com/patrick-brian-mooney/personal-library

from social_media_auth import Irish_lit_discourses_client   # Unshared module with my authontication constants

import text_generator as tg     # https://github.com/patrick-brian-mooney/markov-sentence-generator


# Set up default values
logger.verbosity_level = 2


def print_usage():
    """Print the docstring as a usage message to stdout"""
    logger.log_it("INFO: print_usage() was called")
    print(__doc__)


the_title = "Matthew Arnold's Guest Lecture of " + datetime.date.today().strftime("%A, %d %B %Y")
the_blog_name = "AutoIrishLitDiscourses"
the_content_path = "/150/extras.txt"
the_tags = ['Matthew Arnold', 'Celtic Literature', 'guest lecture', 'Irish literature', 'automatically generated text', 'Patrick Mooney', 'Python', 'Markov chains']
the_content = ''

logger.log_it('INFO: Constants and variables set up; generating content', 2)

lecture_length = random.randint(80, 120)
the_content = tg.TextGenerator('Matthew Arnold generator', training_texts='/IrishLitDiscourses/sources/m.arnold/CelticLiterature.txt',
                               markov_length=2).gen_text(sentences_desired=lecture_length)

the_lines = ["<p>%s</p>" % the_line.strip() for the_line in the_content.split('\n\n')]
the_content = "\n\n".join(the_lines)
logger.log_it('INFO: Attempting to post the content', 2)
logger.log_it("the_content: \n\n" + the_content)

the_status, the_tumblr_data = social_media.tumblr_text_post(Irish_lit_discourses_client, the_tags, the_title, the_content)

logger.log_it('INFO: We\'re done', 2)
