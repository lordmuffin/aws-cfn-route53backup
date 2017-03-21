import subprocess
command = ["./aws", "s3", "sync", "--acl", "public-read", "--delete",
           source_dir + "/", "s3://" + to_bucket + "/"]
print(subprocess.check_output(command, stderr=subprocess.STDOUT))
