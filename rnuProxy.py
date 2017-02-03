"""
Reverse proxy with DDNS(NOIP) and UPnp(Port Forwarding) features
"""
import argparse
import base64
import urllib2
import tornado.ioloop
import maproxy.proxyserver
import miniupnpc

def set_noip(hostname, username, password):
    """
        Set Domain IP
    """
    try:
        request = urllib2.Request("http://dynupdate.no-ip.com/nic/update?hostname=" + hostname)
        base64string = base64.b64encode('%s:%s' % (username, password))
        request.add_header("Authorization", "Basic %s" % base64string)
        urllib2.urlopen(request).read()
    except Exception:
        print "Unable to update DDNS"


def port_fwd(external_port, internal_port, protocol, name):
    u = miniupnpc.UPnP()
    if u.discover() > 0:
        u.selectigd()
        u.deleteportmapping(external_port, protocol)
        u.addportmapping(external_port, protocol, u.lanaddr, internal_port, name, '')
    else:
        print "No UPnP Device found"

def port_type(p):
    p =int(p)
    if p>0 and p<65536:
        return p
    raise argparse.ArgumentError('Port number should be greater than 0 and less than 65536')

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser("Runs a proxy on a specific port.")
    PARSER.add_argument('lport', metavar='Local_Port', help='Listening port')
    PARSER.add_argument('rhost', metavar='Remote_Host', help='Remote host')
    PARSER.add_argument('rport', metavar='Remote_Port', help='Remote port')
    G_U = PARSER.add_argument_group('upnp')
    G_U.add_argument('-f','--upnp', action='store_true', default=False)
    G_U.add_argument("-e", "--external-port", dest='external_port', type=port_type)
    G_U.add_argument("-i", "--internal-port", dest='internal_port', type=port_type)
    G_U.add_argument('-t', '--protocol', choices=['TCP','UDP'])
    G_U.add_argument('-n', '--name')
    U_U = PARSER.add_argument_group('noip')
    U_U.add_argument('-d', '--noip' , action='store_true', default=False)
    U_U.add_argument('-l', '--local-host', dest='local_host')
    U_U.add_argument('-u', '--username')
    U_U.add_argument('-p', '--password')
    ARGS = PARSER.parse_args()
    if ARGS.upnp:
        if ARGS.external_port is None or ARGS.internal_port is None or ARGS.protocol is None or ARGS.name is None:
            PARSER.error('if -f is set then provide -e, -i, -t and -n')
        port_fwd(ARGS.external_port,ARGS.internal_port,ARGS.protocol,ARGS.name)
    if ARGS.noip:
        if ARGS.local_host is None or ARGS.username is None or ARGS.password is None:
            PARSER.error('if -d is set then provide -l, -u and -p')
        set_noip(ARGS.local_host, ARGS.username, ARGS.password)
    
    S = maproxy.proxyserver.ProxyServer(ARGS.rhost, ARGS.rport)
    S.listen(ARGS.lport)
    print "Running..."
    tornado.ioloop.IOLoop.instance().start()
