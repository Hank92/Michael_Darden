import sys
import subprocess
import os

import logging
import boto3
from botocore.exceptions import ClientError

def process():
    if not os.path.exists('foo'):
        subprocess.call(["gcc", "foo.c", "-ofoo", "-lm"])

def dfModel(*args):
	process()
	subprocess.call(["./foo", args[0], args[1], "30"], stdin = sys.stdin)
	print(args[0])
	print(args[1])
	subprocess.run(["python","moveTos3.py"])	
	print("printing result")
	return 'index.html'

	