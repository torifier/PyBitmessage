#!/bin/bash


#      run   this  file   on Linux  in order to post a picture  on   BITmessage !   works very cool !



for file in ./payload/*
do
      ./BM-API-client.py  -e"${file}"   -s 'pic sent via API :   '  --es  --ttl='60*24*1'   -uUSER1 -pPASSWORD2
#     echo "${file}"

done

#  send any binary file e.g. a picture via Bitmessage
#  max. file size approx. 130 KBytes
#
#
#  --embed ./binary-payloads/*
#  multi pic post
#
#  'This text line will appear above the picture in the Bit-Message'
# --en=1   vs.   for file in * do pp done

# --eor=20 --eoc=99    --eory=100 --eorx=100    --edetect     ## did not quite work here...

# 

# --ttl 4 day default  TIME TO LIVE = storage time on BM before post will be dropped by BM network

# or use clipboard method with Klipper
#
#
#                -t BM-some-chan-address to post into
#       Politics -t BM-2cVE8v7L4qb14R5iU2no9oizkx8MpuvRZ7
#
