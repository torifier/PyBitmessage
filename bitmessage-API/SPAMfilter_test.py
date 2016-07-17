#!/bin/python2.7
from __future__ import division
# -*- coding: utf-8 -*-
'''
  Torifier's spam filter test tool


https://github.com/torifier/PyBitmessage/blob/torifier-spamfilter/bitmessage-API/SPAMfilter_test.py

https://beamstat.com/chan/general

  insert filter part after   line 507+    in  pyBitmessage   src/class_objectProcessor.py 

'''


import re
import string


subject = 'some_SPAM_or_whatever eeeee EEEEEEEEEEE xxxx'
body    = '11111 22222 33333 44444 55555'

blockMessage = False

# copy & paste real spam from BM to test filter with
t='''
THTWJ WLIRQ SPOVA GHGBM EDSPU GMWVB OLVKB XZXCX LCHIX UNNEP
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

#t=subject                                                                     # text to filter now

#print t

a=0
b=0
c=0
s2=0    # len subj
p=0.0
s=False # = SPAM


print subject
print body

#print string.octdigits
#print string.digits
#print string.uppercase

################################### begin of filter regex part to put in       src/class_objectProcessor.py 
s=False # = SPAM

s2=len(subject)
b2=len(body)

#FIXME                                                                         # filter cyrillic & China charsets

#t2=string.upper(subject)
s3=str.upper   (subject)
c=str.count    (s3, 'E') ## , 1 , (3*5))                                       # both 3 *-  9++
p = c / s2
if p < 0.05                  :     s=True                                      # 5% is too few 'E' for English, average is 13%
print "percentage letter E is present "   , c 

c=0
if          s2 == 32       :   s = True                                        # a=string.count(s, sub[, start[, end]])
elif        b2  > 4000     :   s = True                                        # want small BM only, less than 4KByte

elif        b2 >= (3*5)    :   c=str.count(body, ' ', 1 , (3*5))               # both 3 *-  9++
if           c == (3-1)    :   s=True                                          # group of 5 then space
elif t[1*5]    ==' '       :   s=True     #FIXME ... 5 10 15                   # ... 5er Grp  5 10 15 20 25 30 # if min len = 50 char ,  uppercase body


if not s:
    if   t[0]=='0' and t[-1] == '0'    : s=True                                    #  0...0 
    elif t[0]=='1'                     : s=True                                    #FIXME
    #print t[0]

if not s:
    if               t.isdigit()       : s=True    
    elif t in     string.digits        : s=True                                    # numbers only


spamstr = 'a SPAM:cat example word:cat!! wateva stuff this might be a spamtext'
match = re.search(r'SPAM:\w\w\w', spamstr)
                                                                               # after search() tests if it succeeded     \w  means  A-z  (word char)
if     match: print 'SPAM:___ found', match.group()                            # 'found SPAM:abc'
else:         print 'did not find SPAM:___'


SPAM=s                                                                         # end of eval
if SPAM:
    subject="SPAMfilter kicked in here " + subject
    subject=''                           # delete or just prefix
    body=''
    blockMessage = True
###############################################################                # end of filter regex

print subject

if blockMessage       :     print 'msg blocked by SPAMfilter'
elif not blockMessage :     print 'msg not blocked'

                                                                               
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
