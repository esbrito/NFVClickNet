#!/usr/bin/python

"""
This example shows how to create a simple network and
how to create docker containers (based on existing images)
to it.
"""
import os
from mininet.net import Containernet
from mininet.node import RemoteController, Docker, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link
from mininet.util import dumpNodeConnections2


def topology():

    "Create a network with some docker containers acting as pops."

    net = Containernet(controller=RemoteController)

    info('*** Adding controller\n')
    c0 = RemoteController('c0', ip='127.0.0.1', port=6633)
    net.addController(c0)

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h3 = net.addHost('h3', ip='10.0.0.3')

    info('*** Adding docker containers\n')
    d1 = net.addPop('d1', ip='10.0.0.251', dimage="gmiotto/click")


    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addPopLink(s2, d1)
    net.addLink(s2, s3)
    net.addLink(s3, h3)

    info('*** Starting network\n')
    net.start()

        # Dumping topology to file
    topofile = open('topology.txt', mode="w")
    output = dumpNodeConnections2(net.values())
    topofile.write(output)
    topofile.close()


    info('*** Running CLI\n')
    CLI(net)

    os.system("rm topology.txt")
if __name__ == '__main__':
    setLogLevel('info')
    topology()
