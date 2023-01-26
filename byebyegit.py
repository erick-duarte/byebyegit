#!/usr/bin/env python3
from urllib.parse import unquote 
import requests
import argparse
import sys
import time
start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

def main():
     banner = """\u001b[36m

 ######  #     # ####### ######  #     # #######  #####  ### ####### 
 #     #  #   #  #       #     #  #   #  #       #     #  #     #    
 #     #   # #   #       #     #   # #   #       #        #     #    
 ######     #    #####   ######     #    #####   #  ####  #     #    
 #     #    #    #       #     #    #    #       #     #  #     #    
 #     #    #    #       #     #    #    #       #     #  #     #    
 ######     #    ####### ######     #    #######  #####  ###    # \u001b[0m               
                            
          \u001b[32m - by Erick "du0x07te" Duarte\u001b[0m 
     """
     print(banner)

     parser = argparse.ArgumentParser(description='ByeByeGIT parameters')
     parser.add_argument('-d','--domain' , help = 'Domain name of the taget [ex : google.com]')
     parser.add_argument('-r', '--retries', help='Specify number of retries for 4xx and 5xx errors', default=1)
     args = parser.parse_args()

     retries = 0
     gitexposed = 0
     if args.domain:
          while retries < int(args.retries):
               if "https://" in args.domain or "http://" in args.domain:
                    domain = args.domain+"/.git/config"
               else:
                    domain = "https://"+args.domain+"/.git/config"
               # response = requests.get(domain, headers=headers, verify=False)
               response = requests.get(domain, headers=headers)
               retries += 1
               if response.status_code == 200:
                    print(f"\u001b[32m [+] git exposed   :\u001b[31m \u001b[36m"+args.domain+"/.git/config\u001b[31m")
                    gitexposed += 1
          print(f"\n\u001b[32m [*] Total git exposed: {gitexposed}\u001b[0m")
          print("\n\u001b[31m [!] Total execution time      : %ss\u001b[0m" % str((time.time() - start_time))[:-12])
     else:
          if not sys.stdin.isatty():
               for n in sys.stdin:
                    line = n.replace("\n", "")
                    retries = 0
                    while retries < int(args.retries):
                         if "https://" in line or "http://" in line:
                              domain = line+"/.git/config"
                         else:
                              domain ="http://"+line+"/.git/config"
                         try:
                              # response = requests.get(domain, headers=headers, verify=False)
                              response = requests.get(domain, headers=headers)
                              retries += 1
                              if response.status_code == 200 and 'remote "origin"' in str(response.content) or 'repositoryformatversion' in str(response.content):
                                   print(f"\u001b[32m [+] git exposed   :\u001b[31m \u001b[36m"+domain+"\u001b[31m")
                                   gitexposed += 1
                              else:
                                   if response.status_code == 200:
                                        print(f"\u001b[0m [+] {domain}:\u001b[31m[!\u001b[32m{response.status_code}\u001b[31m]\u001b[0m")
                                   else:
                                        print(f"\u001b[0m [+] {domain}:\u001b[32m [{response.status_code}]\u001b[0m")
                         except:
                              print(f"\u001b[31m [+] Connection refused: \u001b[0m"+ domain)
                              retries += 1
                              continue
               print(f"\n\u001b[32m [*] Total git exposed: {gitexposed}\u001b[0m")
               print("\n\u001b[31m [!] Total execution time      : %ss\u001b[0m" % str((time.time() - start_time))[:-12])
          else:
               print(f"\n\u001b[31m [!] Doesn't have the domain argument and no stdin\n\u001b[0m")

if __name__ == "__main__":
     main()
    
