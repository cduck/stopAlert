#!/usr/bin/env python

import sys
import time
from datetime import date
from numpy import random
import mail

from alertConfig import *
'''
SUBJ = '.'
MESSAGE = '                    STOP'
RECIPIENTS = ["...@txt.att.net", "...@gmail.com"]

PER_DAY = 8
TIMESTEP = 60  # Minute
'''
TIMESTEPS_PER_DAY = 24*60*60.0/TIMESTEP
PROBABILITY = float(PER_DAY)/TIMESTEPS_PER_DAY

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

def sendStopTo(addrs):
  mail.sendMail(SUBJ, MESSAGE, to=addrs)

def main(msg):
  print 'Probability:', PROBABILITY
  print

  while True:
    for addr in RECIPIENTS:
      A = random.ranf()
      if A < PROBABILITY:
        print
        print '%s : Sending to "%s"' % (time.strftime(DATE_FORMAT), addr),
        sendStopTo((addr,))
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(TIMESTEP)

if __name__ == '__main__':
  msg = 'Email from python'
  if len(sys.argv) > 1:
    msg = sys.argv[1]
  main(msg)

