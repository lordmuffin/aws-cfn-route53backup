#!/bin/bash
(echo "### Running Git Clone"; git clone $CIRCLE_REPOSITORY_URL ~/aws-cfn-route53backup)
(echo "### Find AWSCLI"; out="$(which aws)"; echo $out)
(echo "### Copying AWSCLI"; sudo rsync -va "$VIRTUAL_ENV/bin/aws" "$HOME/"; perl -pi -e '$_ = "#!/usr/bin/python\n" if $. == 1' ~/aws)
(echo "### Zipping AWSCLI"; sudo zip -r9 $zipfile $HOME/aws)
(echo "### Zipping Lambda Files"; sudo mkdir $HOME/upload; cd ~/aws-cfn-route53backup/functions/; sudo zip -r9 $zipfile *)
(echo "### Zipping Site-Packages"; cd $VIRTUAL_ENV/lib/python2.7/site-packages; sudo zip -r9 $zipfile *)
echo "### Good or bad im done. $zipfile Created."
