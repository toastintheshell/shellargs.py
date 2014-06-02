#!/usr/bin/python 

"""     shellargs.py
        """

import sys

##############################################################################


def arg_parser(arg_list):
    # Expects sys.argv - parses arguments into a list of lists 
    # [<num of dashes>, "arg"], each 1-dash char added separately
    # 1-dash & 2-dash return string after = as single separate item 
    # *** add case for "-x no_dash" and "--xyc no_dash"? ***
    if not type(arg_list) is list: 
        # input sanitization, returns None, allows caller to handle bad input
        # don't know if best practice
        return
    out = []
    for i in arg_list[1:]: 
        if i[0:2] == "--": # long-form arguments
            if i.find("=") == -1:
                out.append([2, i[2:]])
            else: 
                out.append([2, i[2:i.find("=")]])
                out.append([2, i[i.find("=")+1:]])
        elif i[0] == "-": # parse 1-dash args as separate chars
            a = 1
            while a < len(i):
                if i[a] != "=": # exception for =string
                    out.append([1, i[a]])
                else:
                    out.append([0, i[a+1:]])
                    break
                a += 1
        else: 
            out.append([0, i]) # stand-alone args
    return out

# testing
print arg_parser(sys.argv)
print arg_parser("bad input")

