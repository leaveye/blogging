#!/bin/sh

OUTDIR=${1:-output}
TMPFILE=$1.tmpfile

# all files to be replaced
grep -r '\.googleapis\.com\>' $OUTDIR | cut -d : -f 1 | uniq |
while read SRCFILE
do
	sed -e 's|\(//[a-z][a-z\.]*\.\)googleapis\.com\>|\1useso.com|g' \
	    -e 's|\<https:\(//[a-z\.]*\.useso\.com\>\)|http:\1|g' \
	    $SRCFILE > $TMPFILE &&
	{ mv -f $TMPFILE $SRCFILE; echo "Done: replaced $SRCFILE"; } ||
	{ rm $TMPFILE; echo "Err: replace $SRCFILE failed"; }
done
