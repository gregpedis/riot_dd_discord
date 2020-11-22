import  configparser as cp
import sys

this = sys.modules[__name__]

cfg = cp.ConfigParser()
cfg.read("config.ini")
PREFIXES = cfg["client"]["prefix"].split("_")


def parse_input(message):
    msg = message.lower().split()
    prefix = msg[0]
    for p in PREFIXES:
        if prefix == p:
            cmd = msg[1]
            args = msg[1:]
            return (cmd, args)
    return ("", [])


def execute_command(message):
    cmd, args = parse_input(message)
    command = getattr(this,cmd)
    command(args)
    return ""

