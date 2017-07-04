#!/usr/bin/python
"""This module provides a controller for the NFV infrastructure."""

import sys
import os
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from docker import Client

CLI = Client(base_url='unix://var/run/docker.sock')
SERVER = "LOCAL"
# SERVER = "REMOTE"


class NfvControllerService(ServiceBase):
    """Class that provides the RPC service for the controller."""

    @rpc(Unicode, Unicode, _returns=bool)
    def deploy(ctx, pop, nf_type="default"):
        if nf_type == 'Firewall':
            path = os.getcwd()+"/mininet/nf_files/firewall.tar"
            _file = open(path)
        elif nf_type == 'Load Balancer':
            path = os.getcwd()+"/mininet/nf_files/balancer.tar"
            _file = open(path)
        elif nf_type == 'Traffic Shaper':
            path = os.getcwd()+"/mininet/nf_files/ts.tar"
            _file = open(path)
        else:
            print "<NFV_SERVICE:deploy:28> invalid nf_type"
            return False
        if CLI.put_archive(container="mn.%s" % (pop), path="/root/",
                            data=_file):
            return True
        else:
            return False

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=bool)
    def enable(ctx, pop, server1=None, server2=None, nf_type="default"):
        if nf_type == 'Firewall':
            process = CLI.exec_create(container="mn.%s" % (pop),
                                      cmd="sudo ./Click -j4 firewall.click "
                                          "DEV=%s" % (pop))
        elif nf_type == 'Load Balancer':
            pop_host = pop[1:-1]
            process = CLI.exec_create(
                            container="mn.%s" % (pop),
                            cmd="sudo ./Click -j4 load-balancer.click "
                            "DEV=%s LB=%s MLB=%s S1=%s M1=%s S2=%s M2=%s"
                                % (pop, pop_host,
                                   str(pop_host).zfill(2), server1,
                                   str(server1).zfill(2), server2,
                                   str(server2).zfill(2)))
        elif nf_type == 'Traffic Shaper':
            process = CLI.exec_create(container="mn.%s" % (pop),
                                      cmd="sudo /root/Click -j4 "
                                          "ts.click DEV=%s" % (pop))
        else:
            print "<NFV_SERVICE:enable:45> invalid nf_type"
            return False
        if CLI.exec_start(process, detach=True) == '':
            return True
        else:
            return False


application = Application([NfvControllerService], 'nfvsdn.api.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    if os.getuid() != 0:
        print "%s must run as root" % sys.argv[0]
        sys.exit(-1)
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.INFO)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.INFO)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()