#!/bin/bash
ls
cd output
ls
for i in $( ls ); do
  #echo $i
  ls $i | wc -l
done
