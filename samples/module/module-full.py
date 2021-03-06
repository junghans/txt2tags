#!/usr/bin/env python
#
# Sample of txt2tags being used as a module (http://txt2tags.org)
#
# Details:
#   The full marked text is a string with headers, config and body.
#   No post config or setting is made.
#

from __future__ import print_function

# Remember to place the 'txt2tags.py' file on the same dir
import txt2tags

# Here is the marked text, it must be a list.
txt = "Header1\nHeader2\nHeader3\n%!target: html\nBody line 1."
txt = txt.split("\n")

# Let's do the conversion
try:
    # First we parse the text, splitting parts and getting config.
    data = txt2tags.process_source_file(contents=txt)
    # Then we convert it, dumping results to the 'tagged' list.
    tagged, config = txt2tags.convert_this_files([data])
    # Show the tagged file on the screen.
    print("\n".join(tagged))
except txt2tags.error as err:
    # Txt2tags error, show the message to the user
    print(err)
except Exception:
    # Unknown error, show the traceback to the user
    print(txt2tags.getUnknownErrorMessage())
