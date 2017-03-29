#!/usr/bin/python
# Written by: Andrew Jackson
# This is used to pull repo from github and drop to S3
import boto3
import json
import cfnresponse
from subprocess import Popen, PIPE
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
    command = event["command"]
    filename = event["hostedZoneId"]
    output, err, exit_code = run(command)
    if exit_code != 0:
        print "Output:"
        print output
        print "Upload to S3:"
        buffer+= output
        s3.Bucket(event["bucket_name"]).put_object(Key=filename, Body=buffer)
        #cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, ".zip pulled to S3 Bucket!")
        print "Error:"
        print err
        # Handle error here
    else:
        # Be happy :D
        print output



#import subprocess
#command = ["./cli53", "list"]
#print(subprocess.check_output(command, stderr=subprocess.STDOUT))
#

#  cli53:
#    branch: master
#    commands:
#      - cli53 list | grep 'Name:*' | cut -f6- -d' ' | while read line; do cli53 export ${line} >> backup/${line}bk; done
#  s3up:
#    branch: master
#    commands:
#      - s3up -source=backup/ -bucket=$BUCKET


#https://github.com/barnybug/cli53/releases/download/0.8.7/cli53-linux-amd64
#$ sudo mv cli53-my-platform /usr/local/bin/cli53
#$ sudo chmod +x /usr/local/bin/cli53
#
