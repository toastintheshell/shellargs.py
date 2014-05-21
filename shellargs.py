#!/usr/bin/python 

"""     shellargs.py
        """

import sys

def sh(script, stdin=None):
    """Returns (stdout, stderr)"""
    import subprocess
    # This function was originally found on this page: 
    # https://stackoverflow.com/questions/2651874/embed-bash-in-python
    # by user: Ian Bicking
    # Thanks Ian!
    ##########################################################################
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
