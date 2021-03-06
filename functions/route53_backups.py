#!/usr/bin/python
# Written by: Andrew Jackson
# This is used to dump a specific zone to a specified s3 bucket.

import boto3
import json
import cfnresponse
from subprocess import Popen, PIPE
from datetime import datetime
import shlex
s3 = boto3.resource('s3')

def run(cmd):
  """Runs the given command locally and returns the output, err and exit_code."""
  if "|" in cmd:
    cmd_parts = cmd.split('|')
  else:
    cmd_parts = []
    cmd_parts.append(cmd)
  i = 0
  p = {}
  for cmd_part in cmd_parts:
    cmd_part = cmd_part.strip()
    if i == 0:
      p[i]=Popen(shlex.split(cmd_part),stdin=None, stdout=PIPE, stderr=PIPE)
    else:
      p[i]=Popen(shlex.split(cmd_part),stdin=p[i-1].stdout, stdout=PIPE, stderr=PIPE)
    i = i +1
  (output, err) = p[i-1].communicate()
  exit_code = p[0].wait()

  return str(output), str(err), exit_code

def newSplit(value):
    lex = shlex.shlex(value)
    lex.quotes = '"'
    lex.whitespace_split = True
    lex.commenters = ''
    return list(lex)

def lambda_handler(event, context):
    print "event.dump = " + json.dumps(event)
    command = "./cli53 export --full " + event["detail"]["requestParameters"]["hostedZoneId"]
    filename = event["detail"]["requestParameters"]["hostedZoneId"] + datetime.now().isoformat()
    bucket_name = "prod-route53-backups"
    output, err, exit_code = run(command)
    if exit_code != 0:
        print "Output:"
        print output
        print "Error:"
        print err
        # Handle error here
    else:
        # Be happy :D
        print "Output:"
        print output
        print "Upload to S3:"
        s3.Bucket(bucket_name).put_object(Key=filename, Body=output)
