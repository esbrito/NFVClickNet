NFVClickNet
============


### NFVClickNet: Containernet fork that allows to deploy and enable Virtual Network Functions in Docker containers as PoPs in the infrastructure


* Mininet:  http://mininet.org
* Original Mininet repository: https://github.com/mininet/mininet
* Containernet: https://github.com/containernet/containernet
  References:
  * Manuel Peuster, Holger Karl, and Steven van Rossem. "**MeDICINE: Rapid Prototyping of Production-Ready Network Services in Multi-PoP Environments.**" to appear in IEEE Conference on Network Function Virtualization and Software Defined Network (NFV-SDN), 2016.
    * Pre-print online: http://arxiv.org/abs/1606.05995
* Click Router: https://github.com/kohler/click

### Requirements

```apt-get install libxml2-dev libxslt1-dev ```

### What new Features it offers?

* You can create PoPs
* Deploy any VNF into the PoP (a Docker Container running Click Router)
* Run any function that can be created using Click (See here: http://read.cs.ucla.edu/click/elements)
* Supported functions are, and not limited to:
  * Load Balancer
  * Firewall
  * NAT
  * DPI
  * Traffic Shaper
  * Tunnel
  * Multicast
  * BRAS
  * Monitoring
  * DDoS prevention
  * IDS
  * IPS
  * Congestion Control
* Included Firewall and Traffic Shaper already implemented


### Installation
* Go to the root folder of the project
* Run the following command
* `sudo make install`


### Usage / Run
Start example topology

* run: `sudo python examples/pophosts.py`
* use: `NFVClickNet> deploy d1 firewall` to deploy firewall in the PoP
* use: `NFVClickNet> enable d1 firewall` to enable the firewall
* use: `NFVClickNet> disable d1 firewall` to disable the firewall

### Cleaning Containers and Mininet
You can run the following command to clean the processes running:
* run: `./util/clean.sh `


### How to create/use a new Virtual Network Function
To create a new VNF, you need to create a `.click` file, which you specify there the processing and analysis you want to do in the packets.

Look here if you want to learn more about Click: http://read.cs.ucla.edu/click/learning. It is easy and simple to learn and create functions with it!

With the `.click` file created, you need to compress it to a tar file. **Put the name of the `.click` file and the `.tar` with the name of the function you will use in the command line to deploy and enable it.**

After creating the `.tar`, put it in mininet/nf_files folder.

Now you can deploy and enable you function!

If you want to see some examples, you can decompress the .tar files in the nf_file folder to look how they were implemented.

### Important Note
When defining a topology as pophost.py, for example, you **NEED** to set the Docker Image with an image that contains Click Software, so it can run click functions.

Fortunately, we already provide a docker image *dimage="gmiotto/click"* so you can use it in your topologies.

### Contact
Email: eduardo.brito@inf.ufrgs.br, paschoal@inf.ufrgs.br, gustavomiotto@gmail.com
