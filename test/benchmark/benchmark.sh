#! /bin/sh -
# Copyright 2018 Bergmann's Lab UNIL <mattia.tomasoni@unil.ch> 
#
# This file is part of DREAM DMI Tool.
#
#    DREAM DMI Tool is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DREAM DMI Tool is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DREAM DMI Tool. If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################
# Mattia Tomasoni - UNIL, CBG
# 2017 DREAM challenge on Disease Module Identification
# https://www.synapse.org/modulechallenge
#
# BENCHMARK  TEST
# This is a benchmark test carreid out on synthetically generated input networks
# using the tools by Santo Fortunato and colleagues (Aalto University)
# https://sites.google.com/site/santofortunato/inthepress2
###############################################################################

# clean previous runs
output=./output_benchmark
rm -rf $output
mkdir $output
mkdir $output/1k
mkdir $output/10k
mkdir $output/100k

# clean all singularity and docker images
#yes | sudo docker system prune -a > /dev/null
#rm -f $HOME/.dream_dmi_tool/containers/*/singularity/*.img

###############################################################################
# BENCHMARK 1k 
# nodes: 1000, average degree 15, max degree 30, max community size 100
# benchmark -N 1000 -k 15 -maxk 30 -muw 0.1 -minc 10 -maxc 100 -beta 1
###############################################################################

# R1 - using symilar parameters as challenge input3
dream_dmi --input=./input/network_N1k.txt --output=$output/1k --method=R1 --container=docker \
  --b=1.7 --c=400 --i=2 --filter=quantile --threshold=1 --post=discard --smallest=10 --largest=100 --b2=1.7 --c2=500 --i2=2
# M1
#dream_dmi --input=./input/1_ppi_anonym_v2.txt --output=$output/1k --method=M1 --container=docker
# K1
#dream_dmi --input=./input/5_cancer_anonym_v2.txt --output=$output/1k --method=K1 --container=docker

###############################################################################
# BENCHMARK 10k
# nodes: 10000, average degree 30, max degree 200, max community size 100
# benchmark -N 10000 -k 30 -maxk 200 -muw 0.1 -minc 10 -maxc 100 -beta 1
###############################################################################

# R1 - using symilar parameters as challenge input2
dream_dmi --input=./input/network_N10k.txt --output=$output/10k --method=R1 --container=docker \
  --b=1.3 --c=500 --i=2 --filter=pageRank --threshold=3 --post=recluster --smallest=10 --largest=100 --b2=1.3 --c2=500 --i2=2
# M1
#dream_dmi --input=./input/network_N10k.txt --output=$output/10k --method=M1 --container=docker
# K1
#dream_dmi --input=./input/network_N10k.txt --output=$output/10k --method=K1 --container=docker

###############################################################################
# BENCHMARK 100k
# nodes: 100000, average degree 50, max degree 500, max community size 100
# benchmark -N 100000 -k 50 -maxk 500 -muw 0.1 -minc 10 -maxc 100 -beta 1
###############################################################################

# R1 - using symilar parameters as challenge input1
dream_dmi --input=./input/network_N100k.txt --output=$output/100k --method=R1 --container=docker \
  --b=2.4 --c=800 --i=2 --filter=double --threshold=4 --post=recluster --smallest=10 --largest=100 --b2=2.4 --c2=800 --i2=2
# M1
#dream_dmi --input=./input/network_N1000k.txt --output=$output/100k --method=M1 --container=docker
# K1
#dream_dmi --input=./input/network_N1000k.txt --output=$output/100k --method=K1 --container=docker
