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
# This script evaluated performance on the experimental benchmark set up in
# "Directed, weighted and overlapping benchmark graphs for community detection
# algorithms", written by Andrea Lancichinetti and Santo Fortunato
###############################################################################


import pandas as pd
from generate_benchnmarks import Grid
import matplotlib.pyplot as plt
import os
from cProfile import label
import numpy as np
from scipy import interpolate

def run():
    grid = Grid()
    grid.scores = pd.read_csv("../graphs/grid.tsv", sep='\t')
    methods = ['R1', 'M1', 'K1']
    # Plot as in  ##################################################################################################
    for N in grid.N:
        out_folder_N = '../graphs/_N' + str(N) + '/'
        os.system('rm -rf ' + out_folder_N + ' && mkdir ' + out_folder_N)
        for t1 in grid.t1:
            out_folder_t1 = out_folder_N + '_t1' + str(t1) + '/'
            os.system('rm -rf ' + out_folder_t1 + ' && mkdir ' + out_folder_t1)
            for beta in grid.beta:
                out_folder_beta = out_folder_t1 + '_beta' + str(beta) + '/'
                os.system('rm -rf ' + out_folder_beta + ' && mkdir ' + out_folder_beta)
                for k in grid.k:
                    fig = plt.figure()
                    for method in methods:
                        N_condition = (grid.scores['N'] == N)
                        t1_condition = (grid.scores['t1'] == t1)
                        beta_condition = (grid.scores['beta'] == beta)
                        method_condition = (grid.scores['METHOD'] == method)
                        k_condition = (grid.scores['k'] == k)
                        data = grid.scores[N_condition & t1_condition & beta_condition & method_condition & k_condition]
                        if(method=='K1'): color='r'
                        if(method=='M1'): color='g'
                        if(method=='R1'): color='b'
                        
                        x = data['mut']
                        y = data['SCORE']
                        f = interpolate.interp1d(x, y, kind='quadratic')
                        xsmooth = np.linspace(x.min(),x.max(),300)
                        ysmooth = f(xsmooth)
                        plt.plot(x,y, color+'o')
                        plt.plot(xsmooth, ysmooth, color, label='cacca')
                        
                        # PROVA COSI https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible
                        #fig = plt.figure(figsize=(10,5))
                        #ax = fig.add_subplot(111)
                        #ax.set_title('ADR vs Rating (CS:GO)')
                        #ax.scatter(x=data[:,0],y=data[:,1],label='Data')
                        #plt.plot(data[:,0], data[:,0],color='red',label='Our Fitting Line')
                        #ax.set_xlabel('ADR')
                        #ax.set_ylabel('Rating')
                        #ax.legend(loc='best')
                        #plt.show()
                        ####################################################
                        
                    title = 'N: ' + str(N) + ', γ: ' + str(t1) + ', β:' + str(beta) + ', k: ' + str(k)
                    fig.suptitle(title , fontsize=20)
                    plt.xlabel('μ', fontsize=18)
                    plt.ylabel('NMI', fontsize=16)
                    fig.savefig(out_folder_beta + 'k_' + str(k) + '.png')
                    plt.close()

if __name__ == '__main__':
    print("\n---------------------------EVALUATING DreamDMI BENCHMARKS-------------------------\n")
    run()
    print("\n-------------------------DONE EVALUATING DreamDMI BENCHMARKS-----------------------\n")
