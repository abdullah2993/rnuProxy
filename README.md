# rnuProxy
WIP together trasparent proxy, Supports noip.com DDNS and UPnP port forwarding. (Tested with Raspberry PI 3)

## Usage
```
usage: Runs a proxy on a specific port. [-h] [-f] [-e EXTERNAL_PORT]
                                        [-i INTERNAL_PORT] [-t {TCP,UDP}]
                                        [-n NAME] [-d] [-l LOCAL_HOST]
                                        [-u USERNAME] [-p PASSWORD]
                                        Local_Port Remote_Host Remote_Port

positional arguments:
  Local_Port            Listening port
  Remote_Host           Remote host
  Remote_Port           Remote port

optional arguments:
  -h, --help            show this help message and exit

upnp:
  -f, --upnp
  -e EXTERNAL_PORT, --external-port EXTERNAL_PORT
  -i INTERNAL_PORT, --internal-port INTERNAL_PORT
  -t {TCP,UDP}, --protocol {TCP,UDP}
  -n NAME, --name NAME

noip:
  -d, --noip
  -l LOCAL_HOST, --local-host LOCAL_HOST
  -u USERNAME, --username USERNAME
  -p PASSWORD, --password PASSWORD
```