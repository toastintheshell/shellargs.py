#!/usr/bin/python 

""" checknet: checks various network settings on a Cache-A to attempt to
        determine the source of network issues.  """

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

# welcome message 
print "CheckNet network setus analysis tool"

# generate empty output file 
print "generating diagnostic file..."
output_file = "/media/vtape/network-analysis.txt"
sh('touch ' + output_file + ' | chmod 777 ' + output_file)

# preload useful information into output_file
sh('echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IFCONFIG:" >> ' + output_file)
sh('ifconfig -a >> ' + output_file)
sh('echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ROUTE:" >> ' + output_file)
sh('route >> ' + output_file)
sh('echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IFCFG FILES:" >> ' + output_file)
sh('cat /etc/sysconfig/network-scripts/ifcfg-eth0 >> ' + output_file)
sh('cat /etc/sysconfig/network-scripts/ifcfg-eth1 >> ' + output_file)
sh('cat /etc/sysconfig/network-scripts/ifcfg-lo >> ' + output_file)
sh('cat /etc/sysconfig/network-scripts/ifcfg-eth2 >> ' + output_file)
sh('cat /etc/sysconfig/network-scripts/ifcfg-eth3 >> ' + output_file)
sh('echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NETSTAT:" >> ' + output_file)
sh('netstat -alp >> ' + output_file)
sh('echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! MESSAGES:" >> ' + output_file)
sh('tail -n 100 /var/log/messages >> ' + output_file) # prints the last 100 lines of /var/log/messages

# ping loopback to verify IP functionality
print "\n" + "%"*53 + "\nChecking loopback interface..."
loopback = sh('ping -q -c10 127.0.0.1 | tee -a ' + output_file)
loopback_percent = loopback[0].split(',')[-2]
if loopback_percent == " 0% packet loss":
    print "\tloopback _GOOD_, Internet Protocol is functional"
elif loopback_percent == " 100% packet loss":
    print "\tloopback _DOWN_, Internet Protocol is not functional"
else:
    print "\tloopback ping returned " + loopback_percent[1:4] + " _ERRORS_"

# ping default gateway listed in route
print "Checking default gateway..."
gateway = sh('route')[0].split()[-7]
print gateway

# ping support.cache-a.com's IP to verify internet, double check with cache-a.com 

# ping support.cache-a.com and cache-a.com 

# check and print info from ifcfg-... files 


