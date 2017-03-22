#!/bin/bash
(echo "### Running Git Clone"; git clone $CIRCLE_REPOSITORY_URL ~/aws-cfn-route53backup)
(echo "### Zipping Lambda Files"; sudo mkdir $HOME/upload; cd ~/aws-cfn-route53backup/functions/; sudo zip -r9 $zipfile *)
(echo "### Modifying cli53 shebang"; perl -pi -e '$_ = "#!/usr/bin/python\n" if $. == 1' $VIRTUAL_ENV/bin/cli53)
(echo "### Zipping Site-Packages"; cd $VIRTUAL_ENV/lib/python2.7/site-packages; sudo zip -r9 $zipfile *)
echo "### Good or bad im done. $zipfile Created."
