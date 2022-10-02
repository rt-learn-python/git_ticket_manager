"""
TODO:
"""

import logging

instance = logging.getLogger("ticket_manager")
instance.setLevel(logging.INFO)
instance.setLevel(logging.DEBUG)  # comment this out when not debugging.

ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG) # this line don't seem to work.

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s {%(pathname)s:%(lineno)d} - %(message)s",
    "%Y-%m-%d %H:%M:%S",
)


# add formatter to ch
ch.setFormatter(formatter)
instance.addHandler(ch)
