import subprocess
command = ["./cli53", "list", "|", "grep", "'Name:*'", "|",
           source_dir + "/", "s3://" + to_bucket + "/"]
print(subprocess.check_output(command, stderr=subprocess.STDOUT))


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
