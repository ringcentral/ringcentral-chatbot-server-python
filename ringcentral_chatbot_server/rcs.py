
name = 'ringcentral_chatbot_server.rcs'
import argparse
import os
from .cmd import cmd
from os.path import dirname, realpath, join, isabs
import pydash as _
import sys

def main():
  cwd = os.getcwd()
  parser = argparse.ArgumentParser(
    description='''
Cli tool to run RingCentral chatbot.
Example: rcs bot.py
With envs: PORT=9800 HOST=localhost rcs bot.py
    '''
  )
  parser.add_argument(
    'path',
    metavar='p',
    help='Chatbot config file path name like bot.py'
  )

  try:
    args = parser.parse_args()
  except:
    return parser.print_help()

  if not _.predicates.is_string(
    _.get(args, 'path')
  ):
    parser.print_help()
  else:
    p = args.path
    if not isabs(p):
      p = join(cwd, p)

    cmd(p)