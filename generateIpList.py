import ipaddress
import os

#delete output if it exists
if os.path.exists("AllIps.txt"):
  os.remove("AllIps.txt")

#Declare some variables
allNetworks = set()
allExcludes = list()
outFile = open("AllIps.txt", "a")

#Read in the Networks and exclusion
with open('networks.txt') as temp_file:
  Networks = [line.rstrip('\n') for line in temp_file]
print(Networks)

with open('exclude.txt') as temp_file:
  Excludes = [line.rstrip('\n') for line in temp_file]

#Expand Networks
for network in Networks:
  n1 = ipaddress.ip_network(network)
  for ip in n1:
    allNetworks.add(str(ip))

#Expand exclusions
for ips in Excludes:
  n1 = ipaddress.ip_network(ips)
  for ip in n1:
    allExcludes.append(str(ip))
print(allExcludes)

#Remove Excludes from network IPS
for ip in allExcludes:
  allNetworks.discard(ip)

#export results to file
for ip in sorted(allNetworks):
  outFile.write(str(ip) + "\n")
outFile.close()


