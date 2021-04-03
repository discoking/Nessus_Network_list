This script generates a list of IP addresses to scan with Tenable Nessus or any other tool that will import a text file of IP addresses.

This script uses two files, networks.txt and exclude.txt.

The format of both networks.txt and exclude.txt are one network per line in network/netmask.

Once the script has run it will output a file call AllIps.txt that conatins all of the IP addresses in the networks.txt file minus those from the exclude.txt file.
