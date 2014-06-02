#!/usr/bin/python 

"""     shellargs.py
        """

import sys

#def sh(script, stdin=None):
#    """Returns (stdout, stderr)"""
#    import subprocess
#    # This function was originally found on this page: 
#    # https://stackoverflow.com/questions/2651874/embed-bash-in-python
#    # by user: Ian Bicking
#    # Thanks Ian!
#    ##########################################################################
#    # Note: by using a list here (['bash', ...]) you avoid quoting 
#    # issues, as the arguments are passed in exactly this order (spaces,
#    # quotes, and newlines won't cause problems):
#    proc = subprocess.Popen(['bash', '-c', script],
#    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#    stdin=subprocess.PIPE)
#    stdout, stderr = proc.communicate()
#    return stdout, stderr

##############################################################################


def arg_parser(arg_list):
    # Expects sys.argv - parses arguments into a list specifying class as
    # 0 for no -, 1 for one - where each letter is individually added with
    # a 0 value, and 2 for two dashes. 
    if not type(arg_list) is list: 
        # input sanitization, returns None, allows caller to handle bad input
        # don't know if good practice
        return
    out = []
    #print arg_list
    for i in arg_list[1:]:
        #print i
        if i[0:2] == "--":
            #print "double-dash argument"
            out.append([2, i[2:]])
        elif i[0] == "-":
            #print "single-dash arguments:"
            for a in i[1:]:
                #print a
                out.append([1, a])
        else: 
            #print "dashless argument"
            out.append([0, i])
        #print out
    return out

# testing
print arg_parser(sys.argv)
print arg_parser("bad input")

