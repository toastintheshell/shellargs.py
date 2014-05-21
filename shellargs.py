#!/usr/bin/python 

"""     shellargs.py
        """

import sys

def sh(script, stdin=None):
    """Returns (stdout, stderr)"""
    import subprocess
    # Note: by using a list here (['bash', ...]) you avoid quoting 
    # issues, as the arguments are passed in exactly this order (spaces,
    # quotes, and newlines won't cause problems):
    proc = subprocess.Popen(['bash', '-c', script],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout, stderr

##############################################################################

print sys.argv

def argparser(arg_list):
    #add stuff here
    return 
