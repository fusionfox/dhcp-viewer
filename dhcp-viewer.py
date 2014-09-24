from flask import Flask, render_template
import dhcpd_leases_parser

app = Flask(__name__)
leases_file_path = 'C:\dhcp.leases'

#TODO read this from file
mac_addresses = ['00:17:f2:9b:d8:19']

@app.route("/")
def dhcp_viewer():
    leases_text = ''
    with open(leases_file_path) as file_object:
        for line in file_object:
            leases_text += line
    leases = dhcpd_leases_parser.parse(leases_text, mac_addresses)
    return render_template('dhcp-viewer.html', leases=leases)


if __name__ == "__main__":
    app.run(debug=True)