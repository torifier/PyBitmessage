#!/bin/python2.7
from __future__ import division
# -*- coding: utf-8 -*-
'''
  Torifier's spam filter test tool


https://github.com/torifier/PyBitmessage/blob/torifier-spamfilter/bitmessage-API/SPAMfilter_test.py

https://beamstat.com/chan/general

  insert filter part after   line 507+    in  pyBitmessage   src/class_objectProcessor.py 
  but the 2. and 3. line are necessary too (i.e. import, coding)

'''


import re
import string


subject = 'subjectline-1 -- some_SPAM_or_whatever eeeee EEEEEEEEEEE xxxx cut off at 500 or so'
body    = 'Gr1----11 22222 33333 44444 55555 SPAMwordwww  00000000000000000000000000000000000'

blockMessage = False

# copy & paste real spam from BM to test filter with
t='''
BODYB WLIRQ SPOVA GHGBM EDSPU GMWVB OLVKB XZXCX LCHIX UNNEP
FWRLD TZEJC ULNLB KMVFW TKQVK PFUWY XXHJK MFEHF TMFXS PAYWC
WRCYQ QCUEX NLXEG NYZQO MSPBM FCJCU YXOKE FUUFG CBSLJ QYZYT
ITQBF KKYUJ OCAJH ZLLOC JDOAE PIILN ELKKA BYRCR YWNSZ OMODN
UWKPY HCLGP FWAGX QBSGO IBHFR WADMI WOTYA JTNXN GQLIO VFWUQ
MXNVY IPNSG PWCEA FTUBX BVBRT VERSI VKVGI PLECI NCGTD VRHGA
UOYNX TUYKJ GHURA NOEAD KNBHG IQOSI YPDFZ LNXSZ UBUMG NQOVQ
MVUVV JCZAF XZTTT OFJSG JFDQP ZCTQD QJIYH HCPYS MBRGP LUBDX
RATQU WKWZA QZZXR CVNCD DCTKW XWLNL NLBQD SEGBZ CCSGJ HHBUZ
NECKC XERRI BCCBX XMXLC QUTJL XWHJB YAKZL SQEEM NZRRJ INOJL
WWYBQ WJFBR EWUYG CVOOC HYOBL SCKNQ YIXUG RAAOV TPJRX FOLSM
PWWAL PSNBF WBUFG YTTIQ MTKFA DZGCD ISVHV EHCGI MCTMV HNMCZ
LMKYQ EXMNE HWNEZ BTSDG MAKXS FDGBW XNMQV TJRON YAWJR NSBTB
WAKQG EMASM QQTAF JMAJW SMMCX PTSDX BGWMI LXHKT KPSBG FVLRT
VAORS SDFHT HIBCO MPKFT WWVWC WFOGN GUHYB AONXQ GONAP KELVJ
ZTNFL TNCFB FPIOP FGQAS YRLZS SHBMV NUQIW FKXNJ QMPVS TCGVJ
TKJOP DUYQM NNKWZ KPNHZ VTZLT JGUPB LEGKZ WATEV AWHAT EVER0
'''

t="t nothing"                                                               # text to filter now

#print t

a=0
b=0
c=0
s2=0    # len subj
p=0.0
s=False # = SPAM

b100='---'

print " "
print "subj is " ,  subject
print " "
print "body is " ,  body
print " "

#print string.octdigits
#print string.digits
#print string.uppercase



################################### begin of filter regex part to put in       src/class_objectProcessor.py 

# USEROPTION SpamFilter   -  enable or disable any options by commenting them out with the letter '#'

s=False # SPAM ? true or false
c=0     # count

if not s: s = subject.isdigit()                                                # numbers only

#                     isupper()       # catch CAPS SPAM   and len > 20  


if not s: 
    s2=len(subject)
    b2=len(body)

if not s:
    b100 =body[0:100]             # first 100 chars to test
    s= str.isspace(b100)          # only whitespace                            s= b100.str.isspace()  

if not s : 
    b100s=     b100.strip(None)   # ' '          # strip lead+end whitespace
    s =        b100s.isdigit()                   # pure number spam without SPACE
    if not s :
        b100s=     b100.replace(' ', '')         # kill whitespace
        s =        b100s.isdigit()               # number spam with SPACEs  +
        if not s : 
            if b100s.isupper() and b2 > 30 : s=True          # uppercase SPAM e.g. A1 


#FIXME                                                                         # filter cyrillic & China charsets



if not s:    
    #s3=string.upper(subject)
    s3=str.upper    (subject)
    c =str.count    (s3, 'E')                             
    p = c / s2
    if p < 0.05 and s2 > 20        :     s=True                                  # 5% is too few 'E' for English, average is 13%
    print "percentage letter E is present "   , c 


if not s:
    if            b2 >= (3*6)    :   c=str.count(b100, ' ', 1 , (3*6))           # both 3 *  9++   -- if min len = 50 char ,  uppercase body
    if             c ==  3       :   s=True                                      # group of 5 then space = length of 6  --- 3 groups with 3 whhitespaces
    if s:
        if b100[5] != ' ' or b100[11] != ' ' and b100[17] !=  ' ' : s=False      # 3 groups only -    5 11 17  inc(6) 3-->9  #  groups of 5 char + SPACE
                           #      +6
if not s:
    if   subject[0]  =='0' and subject[-1] == '0'    : s=True                    #  0...0 
    elif subject[0]  =='}'                           : s=True                    # FIXME kills non spam
    elif subject[0:5]=='::cp::'                      : s=True                    # FIXME token for c-porn




    #print t[0] 

if not s:
    if            s2 == 32           :   s = True  # FIXME kills too easily nonspam  # a=string.count(s, sub[, start[, end]])
    elif          b2  > 4000         :   s = True                                    # want small BM only, less than 4KByte

                                  
if not s:
    b100  = 'a SPAMword    FIXME  remove this line after testing'
    found = re.search(r'SPAM\w\w\w', b100)                                                       # search a spam regex
    if     found : s = True                                                                      # after search() tests if it succeeded     \w  means  A-z  (word char)
#   if     found : s=True      #print 'SPAM:___ found', match.group()                            # 'found SPAM:abc'
#   else:          s=False     #print 'did not find SPAM:___'

    print "regex true or false : " , s    
    

                                                                               # end of SPAM evaluation
if  s:    # SPAM was found
    subject="SPAMfilter kicked in here " + subject                             # prefix subject line
#   subject=''                                                                 # delete subject line or just prefix
#   body=''             #  FIXME remove the '#'                                # delete body
    blockMessage = True
###############################################################                # end of filter regex to copy & paste

print "subj: " , subject
print " "
print " s = spamTrigger is --> " , s
print " "
if blockMessage       :     print 'msg blocked by SPAMfilter'
elif not blockMessage :     print 'msg not blocked'
print " "
 
                                                                               
"""
regular expressions, re , regex :
Here are basic patterns which match single chars:

a, X, 9, <  
ordinary characters just match themselves exactly. 
The meta-characters which do not match themselves because they have 
special meanings are:

. ^ $ * + ? { [ ] \ | ( ) 

(details below)


. (a period) 
matches any single character except newline '\n'


\w (lowercase w) 
matches a "word" character: 
a letter or digit or underbar [a-zA-Z0-9_] 
Note that although "word" is the mnemonic for this, 
it only matches a single word char, not a whole word. 


\W (upper case W) matches any non-word character.


\b -- boundary between word and non-word


\s  (lowercase s) 
matches a single whitespace character 
space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.


\t, \n,      \r 
tab, newline, return


\d decimal digit [0-9] 
(some older regex utilities do not support but \d, but they all support \w and \s)


^ = start, $ = end 
match the start or end of the string


\ 
inhibit the "specialness" of a character. 
for example, use \. to match a period or \\ to match a slash. 
If you are unsure if a character has special meaning, 
such as '@', you can put a slash in front of it  \@ 
to make sure it is treated just as a character or a "literal"

"""
