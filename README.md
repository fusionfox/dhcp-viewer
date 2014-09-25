# dhcp-viewer
### Display dhcp.leases as a list of IP addresses in a HTML table
Web application using Python and Flask to parse the contents of dhcp.leases and display a list of IP addresses that have been assigned, with optional filtering by MAC address

######Dependencies
[pyparsing](https://pypi.python.org/pypi/pyparsing)

###### In progress
* Currently dhcp.leases is read from the root of the `C:` drive, should be `/var/lib/dhcpd/dhcpd.leases`
* MAC address filter is hard-coded into `dhcp-viewer.py`, should be provided by proxmox-scraping shell script