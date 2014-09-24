# dhcp-viewer
## Display dhcp.leases as a list of IP addresses in a HTML table
Web application using Python and Flask to parse the contents of dhcp.leases and display a list of IP addresses that have been assigned, with optional filtering by MAC address

Requires [pyparsing](https://pypi.python.org/pypi/pyparsing)

###### Dev Note: 
Currently dhcp.leases is read from the root of the C: drive and the MAC address filter is hard-coded into dhcp-viewer.py