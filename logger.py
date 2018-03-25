import logging

instance = logging.getLogger('ticket_manager')
instance.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

# add formatter to ch
ch.setFormatter(formatter)
instance.addHandler(ch)
