#!/bin/bash
(echo "### Running Git Clone"; git clone $CIRCLE_REPOSITORY_URL $HOME/$CIRCLE_PROJECT_REPONAME)
(echo "### Find AWSCLI"; out="$(which aws)"; echo $out)
(echo "### Make Zip Folder"; sudo mkdir $HOME/upload; )
(echo "### Download cli53"; sudo wget -O $HOME/cli53-linux-amd64 https://github.com/barnybug/cli53/releases/download/0.8.7/cli53-linux-amd64; sudo chmod +x $HOME/cli53-linux-amd64)
(echo "### Copying AWSCLI"; sudo rsync -va "$VIRTUAL_ENV/bin/aws" "$HOME/aws/"; sudo perl -pi -e '$_ = "#!/usr/bin/python\n" if $. == 1' $HOME/aws/aws)
(echo "### Rename and move cli53"; sudo mv $HOME/cli53-linux-amd64 $HOME/aws/cli53)
(echo "### Zipping AWSCLI and CLI53"; cd $HOME/aws; sudo zip -r9 $zipfile *)
(echo "### Zipping Lambda Files";cd ~/aws-cfn-route53backup/functions/; sudo zip -r9 $zipfile *)
(echo "### Zipping Site-Packages"; cd $VIRTUAL_ENV/lib/python2.7/site-packages; sudo zip -r9 $zipfile *)
echo "### Good or bad im done. $zipfile Created."
