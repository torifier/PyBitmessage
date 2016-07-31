


########
        ###################################                                                begin of filter regex part to put in       src/class_objectProcessor.py 
        # USEROPTION SpamFilter   -   enable or disable any options 
        #                             by commenting them out with the letter '#'
        # test spamfilter with provided tool     /bitmessage-API/SPAMfilter_test.py



        '''
        file /pyBitmessage__torifier/src/class_objectProcessor.py patched   to add a spam filter below line 507+ of the original source file.

        to modify your pyBM , just (backup and) replace the original class_objectProcessor.py with this patched class_objectProcessor.py
        Also delete class_objectProcessor.pyc , it will be recompiled
  
        '''

                                                                                         #  b2 bl err
        
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
                    if b100s.isupper() and bl > 30 : s=True                              # uppercase SPAM e.g. A1   or  ASSUZTGFGHZUJTHZTGWEHRJUZHTG more than 30 letters
        
        # if not s:                                                                      # FIXME filter cyrillic & China charsets
        
        if not s:    
           #su=string.upper(subject)
            su=str.upper   (subject)
            c =str.count   (su, 'E')                             
            p = c / sl
            if p < 0.05 and sl > 20                          : s = True                  # 5% is too few letters 'E' for English, average is ~ 13%
#            print "\n percentage letter E occurance = "   , c , "% "                     # FIXME remove (#) this line in production version
        
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
            found = re.search(r'SPAMxxxx\w\w\w', b100)                                   # search a spam regex                
            if     found : s = True                                                      # after search() tests if it succeeded     \w  means  A-z  (word char)
        #   if     found : s=True      #print '\n SPAM*** found'        , found.group()  # 'found SPAMabc'                
        #   else:          s=False     #print '\n did not find SPAM***'
#            print "\n regex true or false : " , s                                        # FIXME remove after testing those 3 lines for performance if you wish   
        
        
                                                                                         # End of SPAM evaluation - now the BM will be killed on individual SPAM policy.
        if  s:    # SPAM was found                                                       
            subject="sf. " + subject                                                     # prefix subject line with  'sf. ' or a prefix of your choosing
        #   subject=''                                                                   # delete subject line or just prefix
        #   body=''                                                                      # FIXME remove the '#' to actually delete body at python runtime
            blockMessage = False # = demo mode    True = Block-Mode              
                                                                                         # demo mode with  blockMessage = False  will
                                                                                         # be good for testing, let's you see what is
                                                                                         # being filtered
                                       
        ###############################################################                    end of filter regex part to put in       src/class_objectProcessor.py 
        




