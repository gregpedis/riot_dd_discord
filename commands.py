import configparser as cp
import sys
import os
import cmd.cmd_champion as cmd_champion
import cmd.cmd_champions
import cmd.cmd_help
import cmd.cmd_item
import cmd.cmd_items
import cmd.cmd_kraken
import cmd.cmd_spell
import cmd.cmd_tags

this = sys.modules[__name__]

cfg = cp.ConfigParser()
cfg.read("config.ini")

PREFIX = cfg["client"]["prefix"]


def parse_input(message):
    msg = message.lower().split()
    if msg[0].startswith(PREFIX):
        cmd = msg[0].replace(PREFIX, "", 1)
        args = msg[1:]
        return (cmd, args)
    return ("", [])


def execute_command(message):
    cmd, args = parse_input(message)
    command = getattr(this, f"{cmd}_command")
    result = command(args)
    return result


def champion_command(args):
    cmd_champion.champion_command(args)
    return ""


def spell_command(args):
    pass
