#!/usr/bin/python 

"""     shellargs.py
        """

import sys

##############################################################################


def arg_parser(arg_list):
    # Expects sys.argv - parses arguments into a list of lists 
    # [<num of dashes>, "arg"], each 1-dash char added separately
    # *** need to add case for -x=... and --xyz=... ***
    # *** add case for "-x no_dash" and "--xyc no_dash"? ***
    if not type(arg_list) is list: 
        # input sanitization, returns None, allows caller to handle bad input
        # don't know if good practice
        return
    out = []
    for i in arg_list[1:]: 
        if i[0:2] == "--": # long-form arguments
            out.append([2, i[2:]])
        elif i[0] == "-": # parse 1-dash args as separate chars
            for a in i[1:]:
                out.append([1, a])
        else: 
            out.append([0, i]) # stand-alone args
    return out

# testing
print arg_parser(sys.argv)
print arg_parser("bad input")

