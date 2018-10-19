# DreamDMI
This repository holds the source code for **DreamDMI**, a command-line tool for Disease Module Identification in molecular networks, levereging the top performing methods of the **Disease Module Identification (DMI) DREAM Challenge** (https://www.synapse.org/modulechallenge)

## Methods
* **K1**: Kernel clustering optimisation algorithm, https://www.synapse.org/#!Synapse:syn7349492/wiki/407359
* **M1**: Modularity optimization algorithm, https://www.synapse.org/#!Synapse:syn7352969/wiki/407384
* **R1**: Random-walk-based algorithm, https://www.synapse.org/#!Synapse:syn7286597/wiki/406659


## SOURCE CODE
The source code is hosted at: https://github.com/mattiat/DREAM_DMI_Tool

## PREREQUISITES
The tool was tested on *Ubuntu Linux 18.04* and *CentOS Linux 7.5*.

Either ```docker``` or ```singularity``` must be installed. Please visit https://www.docker.com or http://singularity.lbl.gov

Some of the Methods may require large amount of resources, depending on your input.

## INSTALLATION
To install: ```./install```

To uninstall: ```./uninstall```

## RUNNING
To run, invoke, from any location: ```dream_dmi --help```

## INPUT
The format for the input network is the following, tab-separated:
One line for each edge, connecting two nodes nodeA and nodeB with weight weight_AB
[nodeA]	[nodeB] weight_AB

For an example, see the contents of test/input
