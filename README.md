# auto-recon-ng
---------------------------------------------------------------------------------------------------------------
AUTO RECON-NG - Automated script to run all modules for a specified list of domains, netblocks or company name
---------------------------------------------------------------------------------------------------------------

**Source:** https://bitbucket.org/LaNMaSteR53/recon-ng

**Usage:** auto_recon-ng.py [-h] -w WORKSPACE [-i FILENAME] [-m MODULENAME] [-company DBNAME1] [-domain DBNAME2] [-netblock DBNAME3]

**Optional arguments:**

  -h, --help            show this help message and exit
  
  -w, --workspace WORKSPACE Workspace name
  
  -i FILENAME           Set the recon-ng source using this list
  
  -m MODULENAME         Specify the modules list
  
  -company DBNAME1      Specify the file containing company names
  
  -domain DBNAME2       Specify the file containing domain names
  
  -netblock DBNAME3     Specify the file containing netblocks
  
**Example:**
python auto-recon-ng -w tjx_recon_2018 -m modules.txt -domain domains.txt

  
**Setting up Auto-recon-ng for sub-domain enumeration:**

1.	Add API keys to Recon-ng:

i.	Launch recon-ng
ii.	Run the command keys list to view all the existing keys
iii.	Add new API key using the command: keys add shodan_api <paste_key_here>
iv.	Run keys list again and confirm that the keys were added

2.	List of API keys to be added for sub-domain enumeration:

Recon-ng will require API keys for using the below 3rd party services, register a new account and generate a new API key each time. Most of these services have rate limiting and will only allow certain number of requests per day. 

•	Shodan: https://shodan.io/
•	Bing API: https://azure.microsoft.com/en-us/services/cognitive-services/bing-web-search-api/
•	Google API key: https://code.google.com/apis/console
•	Censys API ID and Secret:  https://censys.io/account/api


**Domain list:**
Create a text file containing the list of top domains in the working directory of auto-recon-ng. For example:
bing.com
microsoft.com

**Modules list:**

a.	Subdomain Enumeration:

Create a text file containing the list of modules, for subdomain enumeration use the below list. When using the below list the “domain” option must be used with auto-recon-ng.

•	recon/domains-domains/brute_suffix
•	recon/domains-hosts/bing_domain_api
•	recon/domains-hosts/bing_domain_web
•	recon/domains-hosts/brute_hosts
•	recon/domains-hosts/builtwith
•	recon/domains-hosts/certificate_transparency
•	recon/domains-hosts/google_site_api
•	recon/domains-hosts/google_site_web
•	recon/domains-hosts/hackertarget
•	recon/domains-hosts/mx_spf_ip
•	recon/domains-hosts/netcraft
•	recon/domains-hosts/shodan_hostname
•	recon/domains-hosts/ssl_san
•	recon/domains-hosts/theharvester_xml
•	recon/domains-hosts/threatcrowd
•	recon/hosts-hosts/bing_ip
•	recon/hosts-hosts/ssltools
•	recon/hosts-ports/shodan_ip

b.	Netblock to host discovery:

Create a text file containing the list of modules, for host enumeration use the below list. When using the below list the “netblock” option must be used with auto-recon-ng.

•	recon/netblocks-hosts/reverse_resolve
•	recon/netblocks-hosts/shodan_net
•	recon/netblocks-ports/census_2012
•	recon/netblocks-ports/censysio
