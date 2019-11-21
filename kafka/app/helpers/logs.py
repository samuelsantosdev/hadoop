import logging, datetime

def do_log(key:str, value:str)->None:
    logging.warning("{}[{}] - {}".format(datetime.datetime.now(), key, value))