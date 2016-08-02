



        ################################### begin of filter regex part to put in       src/class_objectProcessor.py 
        # USEROPTION SpamFilter   -   enable or disable any options 
        #                             by commenting them out with the letter '#'
        # test spamfilter with provided tool     /bitmessage-API/spamfilter/spamfilter-test-offline.py




        '''
        file /pyBitmessage__torifier/src/class_objectProcessor.py patched   to add a spam filter below line 507+ of the original source file.

        to modify your pyBM , just (backup and) replace the original class_objectProcessor.py with this patched class_objectProcessor.py
        Also delete class_objectProcessor.pyc , it will be recompiled
  
        '''

        criterion = " none - "                                                           # re

        s=False # SPAM ? true or false
        c=0     # count


        if not s: 
            sl=len(subject)
            bl=len(body)





        if sl > 5 :
            if not s : s = subject.isdigit()                                             # numbers only, a common BM SPAM format for a while
            if s :  criterion  = " isdigit - "
        
            if not s : s = subject.isupper()                                             # catch CAPS SPAM   and s length > 5
            if s : criterion   = " isupper - "




        
        if not s:
            b100 =body[0:100]                                                            # first 100 chars to test for performance reasons. Increase to your liking!
            s= str.isspace(b100)                                                         # only whitespace?         s= b100.str.isspace()  
            if s : criterion = " b SPACE - " 
        if not s : 
            b100s=     b100.strip(None)   # ' '                                          # strip lead+end whitespace
            s =        b100s.isdigit()                                                   # pure number spam without SPACE remaining after stripping?
            if s : criterion = " b digit - " 

            if not s :
                b100s=     b100.replace(' ', '')                                         # kill whitespace to possibly find:
                s =        b100s.isdigit()                                               # number spam with SPACEs               +
                if s : criterion = " b # SPACE - " 

                if not s : 
                    if b100s.isupper() and bl > 30 : s=True                              # uppercase SPAM e.g. A1   or  ASSUZTGFGHZUJTHZTGWEHRJUZHTG more than 30 letters
                    if s : criterion = " b UPPER  - "


        # if not s:                                                                      # FIXME filter cyrillic & China charsets  

        #if not s:    
           ##su=string.upper(subject)                                                    # short subj poss without 'E'
            #su=str.upper   (subject)
            #c =str.count   (su, 'E')   
            #if sl <> 0:								 # div by zero
	        #p   = c / sl
            #else: p = 0.999								 
            #if    p < 0.020 and sl > 20 :                                               # 2%
                #s = True                                                                # 5% is too few letters 'E' for English, average is ~ 13% 
                #if s : criterion = " subj %E " + str(p) + " - " 
##               print "\n % letter E occurance = "   , p , "% "                         # FIXME remove (#) this line in production version



        #if not s and bl > 30 :
            #bu=str.upper   (b100)
            #c =str.count   (bu, 'E')   
            #if bl <> 0:								 # div by zero
	        #p   = c / sl
            #else: p = 0.999					                         # / 0			 
            #if    p < 0.012  :                                                          # 1.2 % E in body longer than 30 chars
                #s = True                                                                # 1.2 % is too few letters 'E' for English, average is ~ 13% 
                #if s : criterion = " body E = " + str(p) + " % - "                      # 1.25% one E in 80 char



        if not s and bl > 30 :                                                           # one E in 30 letters in body
            b100u=str.upper   (b100)
            c    =str.count   (b100u, 'E')   
            if c < 1 :                                                                   # minimum = one E in body longer than 30 chars
                s = True                                   
                if s : criterion = " body100 without E - "                               # 1.25% one E in 80 char
















        if not s or s :
            if            bl >  (9*6)    :   c=str.count(b100, ' ', 1 , (9*6))           # 9 groups of 6 letters = 1 line tested ; increase, if You like.  
            if             c ==  9       :
                s=True                                                                   # group of 5 then space = length of 6  --- 3 groups with exactly 3 whhitespaces
                if s : criterion = " grp of 5 - "
                if s :
                    if  b100[5]   != ' ' or b100[11] != ' ' or b100[17] !=  ' ' or  b100[23]  != ' ' or b100[29] != ' ' or b100[35] !=  ' ' or  b100[41]  != ' ' or b100[47] != ' ' or  b100[53] !=  ' ' :
                        s=False                                                          # 3 ... 9 groups tested: 5 11 17 inc(6) 3-->9    # inc 6
                        if not s       : criterion = " no grp spam -      "              # 5 chars then SPACE , a common SPAM format!
                        elif bl == 40  : criterion = " grp 40 decodable - "              # use spam decoder to obtain Limerick spam




        if not s:
            if sl > 0 :
#               if   subject[0]  =='0' and subject[-1] == '0'    : s = True              # 0...0 actually quite an arbitrary filter. Comment out if you wish with #
#               elif subject[0]  =='}'                           : s = True              # FIXME kills non spam   } as first character alone will kill a BM 
                if   subject[0:5]== '::cp::'                     : s = True              # FIXME token for c-porn - is it ever gonna happen ?                                                                                         
                if s : criterion = " ::token::  - "                                      # 0...0  and  }   deactivated



                                                                                         # print t[0]  during testing with Spyder python GUI
        if not s:
#           if            sl        ==          40               : s = True              # FIXME  40 is decodable - kills nonspam too easily!   
            if                   bl  >        8000               : s = True              # want small BM only, less than 8000 letters, thank you very much!
#           elif                 bl ==      0                    : s = True              # 1 or zero letter spam  - subject line only , maybe nonspam                                                                                      
            if s : criterion = " bl length >  8000 "                                     # a=string.count(s, sub[, start[, end]])


                                                                                         # idea : decode sl-40 msg & prefix , put code at bottom , 
                                                                                         #        use ::spam-40:: token to trigger decode
        if not s:
#           b100  = 'a SPAMword    FIXME  comment / remove this line after testing'      # FIXME we need improved SPAMword finder REGEX that trigger on **** stuff and whatever
            found = re.search       (r'SPAMxxxx\w\w\w', b100)                            # search a spam regex                
            if     found : 
                s = True  
                if s: criterion = " regexpr. SPAMxxxx\w\w\w - "
                                                                                         # after search() tests if it succeeded     \w  means  A-z  (word char)
        #   if     found : s=True      #print '\n SPAM*** found'        , found.group()  # 'found SPAMabc'                
        #   else:          s=False     #print '\n did not find SPAM***'
        #   print "\n regex true or false : " , s                                        # FIXME remove after testing those 3 lines for performance if you wish        
        
                                                                                         # End of SPAM evaluation - now the BM will be killed on individual SPAM policy.
        if  s:      # SPAM was found                                                       
            subject="{sf. " + criterion + subject                                        # prefix subject line with  'sf. ' or a prefix of your choosing
        #   subject=''                                                                   # delete subject line or just prefix
        #   body=''                                                                      # FIXME remove the '#' to actually delete body at python runtime
            blockMessage = False # = demo mode                                           # True = Block-Mode , msg disappears totally from messagbebase             
                                                                                         # demo mode with  blockMessage = False  will be good for testing, 
                                                                                         # let's you see what is being filtered under which criterion
                                       
        ###############################################################                    end of filter regex part to put in       src/class_objectProcessor.py 


