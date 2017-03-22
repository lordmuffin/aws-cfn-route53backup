#!/bin/bash
git clone $CIRCLE_REPOSITORY_URL ~/aws-cfn-route53backup
zip -r9 $zipfile ~/aws-cfn-route53backup/functions/route53_backups.py
perl -pi -e '$_ = "#!/usr/bin/python\n" if $. == 1' $VIRTUAL_ENV/bin/cli53
(cd $VIRTUAL_ENV/lib/python2.7/site-packages; zip -r9 ~/route53_backups.zip *)
