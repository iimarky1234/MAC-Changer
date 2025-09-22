#!bin/py
import subprocess
import optparse
from optparse import OptionParser
import re
def get_arguments():
    parser=OptionParser()
    parser.add_option('-m','--mac',dest='new_mac',help="New MAC address to change")
    parser.add_option('-i','--interface',dest='iface',help="Choose interface to change MAC address")
    opts, args = parser.parse_args()
    #print(opts.iface)
    if (opts.iface is None):
        parser.error("[#] Please specify interface. Type -h for more help")
    elif (opts.new_mac is None):
        parser.error("[#] Please specify MAC Adress. Type -h for more help")
    return opts

def change_mac(mac,iface):
    print("[*] Changing MAC address "+ iface + " to "+ mac)
    subprocess.run(['ifconfig',iface,'down'])
    check_re=subprocess.call(['ifconfig',iface,'hw','ether',mac])
    subprocess.run(['ifconfig',iface,'up'])

 
def current_mac(iface):
    output=subprocess.check_output(['ifconfig',iface])
    check_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(output))
    if check_mac:
        return check_mac.group(0)


        
option=get_arguments()
cur_mac=current_mac(option.iface)
print("[+] Your current MAC Address is: "+str(cur_mac))
output=change_mac(option.new_mac,option.iface)
new_mac=current_mac(option.iface)
if (cur_mac!=new_mac):
    print("[+] Your new MAC address is: "+str(new_mac))
else:
    print("[-] Nothing has changed")