#!/bin/bash
(echo "### Running Git Clone"; git clone $CIRCLE_REPOSITORY_URL ~/aws-cfn-route53backup)
(echo "### Find AWSCLI"; out="$(which aws)"; echo $out)
(echo "### Make Zip Folder"; sudo mkdir $HOME/upload; )
(echo "### Install cli53"; ls -lra $HOME)
(echo "### Copying AWSCLI"; sudo rsync -va "$VIRTUAL_ENV/bin/aws" "$HOME/aws/"; sudo perl -pi -e '$_ = "#!/usr/bin/python\n" if $. == 1' $HOME/aws/aws)
(echo "### Zipping AWSCLI"; cd $HOME/aws; sudo zip -r9 $zipfile *)
(echo "### Zipping Lambda Files";cd ~/aws-cfn-route53backup/functions/; sudo zip -r9 $zipfile *)
(echo "### Zipping Site-Packages"; cd $VIRTUAL_ENV/lib/python2.7/site-packages; sudo zip -r9 $zipfile *)
echo "### Good or bad im done. $zipfile Created."
