#!/bin/sh

OUTDIR=${1:-output}
TMPFILE=$1.tmpfile

# all files to be replaced
grep -r googleapis $OUTDIR | cut -d : -f 1 | uniq |
while read SRCFILE
do
    sed -e 's|googleapis\.com|useso.com|g' $SRCFILE > $TMPFILE &&
    { mv -f $TMPFILE $SRCFILE; echo "Done: replaced $SRCFILE"; } ||
    { rm $TMPFILE; echo "Err: replace $SRCFILE failed"; }
done
