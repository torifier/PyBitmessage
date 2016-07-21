#!/bin/python2.7
from __future__ import division
# -*- coding: utf-8 -*-
'''
  Torifier's spam filter test tool


https://github.com/torifier/PyBitmessage/blob/torifier-spamfilter/bitmessage-API/SPAMfilter_test.py

https://beamstat.com/chan/general

  insert filter part after   line 507+    in  pyBitmessage   src/class_objectProcessor.py 
  but the 2. and 3. line are necessary too  i.e. import, coding
  Once inserted into pyBitmessage thus, the live spamfilter does not filter spam which you yourself posted to a chan
  locally. To test the *live* filter, you must post test spam from a secondary computer. Or just use this offline test tool instead.

'''


import re
import string  


subject = 'subjectline-1 -- some_SPAM_or_whatever eeeee EEEEEEEEEEE xxxx cut off at 500 or so'
body    = 'Gr5----11 22222 33333 44444 55555 SPAMwordwww  00000000000000000000000000000000000'

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
#print t
t="t nothing"                                                                    # text to filter now
b100='---'

c =0     # count
sl=0     # subject line length
bl=0     # body length
p =0.0   # percentage of 'E' in SPAM
s =False # SPAM ? true or false

print "\n subj is: " ,  subject
print "\n body is: " ,  body

#print    string.octdigits , string.digits  , string.uppercase

###################################                                                begin of filter regex part to put in       src/class_objectProcessor.py 

# USEROPTION SpamFilter   -   enable or disable any options 
#                             by commenting them out with the letter '#'

s=False # SPAM ? true or false
c=0     # count

if not s: s = subject.isdigit()                                                  # numbers only, a common BM SPAM format for a while

#                     isupper()                                                  # catch CAPS SPAM   and length > 20  

if not s: 
    sl=len(subject)
    bl=len(body)

if not s:
    b100 =body[0:100]                                                            # first 100 chars to test for performance reasons. Increase to your liking!
    s= str.isspace(b100)                                                         # only whitespace?         s= b100.str.isspace()  

if not s : 
    b100s=     b100.strip(None)   # ' '                                          # strip lead+end whitespace
    s =        b100s.isdigit()                                                   # pure number spam without SPACE remaining after stripping?
    if not s :
        b100s=     b100.replace(' ', '')                                         # kill whitespace to possibly find:
        s =        b100s.isdigit()                                               # number spam with SPACEs               +
        if not s : 
            if b100s.isupper() and b2 > 30 : s=True                              # uppercase SPAM e.g. A1   or  ASSUZTGFGHZUJTHZTGWEHRJUZHTG more than 30 letters

# if not s:                                                                      # FIXME filter cyrillic & China charsets

if not s:    
   #su=string.upper(subject)
    su=str.upper   (subject)
    c =str.count   (su, 'E')                             
    p = c / sl
    if p < 0.05 and sl > 20                          : s = True                  # 5% is too few letters 'E' for English, average is ~ 13%
    print "\n percentage letter E occurance = "   , c , "% "                     # FIXME remove (#) this line in production version

if not s:
    if            bl >= (3*6)    :   c=str.count(b100, ' ', 1 , (3*6))           # 3 groups of 6 letters tested ; increase, if You like.  FIXME min len = 50 char of msg-body??
    if             c ==  3       :   s=True                                      # group of 5 then space = length of 6  --- 3 groups with exactly 3 whhitespaces
    if s:
        if b100[5] != ' ' or b100[11] != ' ' or b100[17] !=  ' ' : s=False       # 3 groups tested: 5 11 17 inc(6) 3-->9  5 char then SPACE , a common SPAM format!
                           #      +6
if not s:
    if   subject[0]  =='0' and subject[-1] == '0'    : s = True                  # 0...0 actually quite an arbitrary filter. Comment out if you wish with #
    elif subject[0]  =='}'                           : s = True                  # FIXME kills non spam   } as first character alone will kill a BM 
    elif subject[0:5]=='::cp::'                      : s = True                  # FIXME token for c-porn - is it ever gonna happen ?

                                                                                 # print t[0]  during testing with Spyder python GUI
if not s:
    if            sl ==   40                         : s = True                  # FIXME  40 is decodable - kills nonspam too easily!   # a=string.count(s, sub[, start[, end]])
    elif          bl  > 4000                         : s = True                  # want small BM only, less than 4000 letters, thank you very much!
    elif          bl  <    2                         : s = True                  # 1 or zero letter spam
                                                                                 # idea : decode sl-40 msg & prefix , put code at bottom , use ::spam-40:: token to trigger decode
if not s:
    b100  = 'a SPAMword    FIXME  comment / remove this line after testing'      # FIXME we need improved SPAMword finder REGEX that trigger on **** stuff and whatever
    found = re.search(r'SPAM\w\w\w', b100)                                       # search a spam regex                
    if     found : s = True                                                      # after search() tests if it succeeded     \w  means  A-z  (word char)
#   if     found : s=True      #print '\n SPAM*** found'        , found.group()  # 'found SPAMabc'                
#   else:          s=False     #print '\n did not find SPAM***'
    print "\n regex true or false : " , s                                        # FIXME remove after testing those 3 lines for performance if you wish   


                                                                                 # End of SPAM evaluation - now the BM will be killed on individual SPAM policy.
if  s:    # SPAM was found                                                       
    subject="SPAMfilter kicked in here " + subject                               # prefix subject line
#   subject=''                                                                   # delete subject line or just prefix
#   body=''                                                                      # FIXME remove the '#' to actually delete body at python runtime
    blockMessage = True                                                          
###############################################################                    end of filter regex part to put in       src/class_objectProcessor.py 

print "\n subj: " , subject
print "\n s = spamTrigger is --> " , s , " \n "
if       blockMessage :     print '\n msg     blocked by SPAMfilter \n'
elif not blockMessage :     print '\n msg not blocked               \n'
 
                                                                               
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
