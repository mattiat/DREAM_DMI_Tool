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
import statsmodels.stats.api as sms

def run():
    grid1 = Grid().scores = pd.read_csv("../graphs/grid.tsv", sep='\t')
    grid2 = Grid().scores = pd.read_csv("../graphs/grid.tsv", sep='\t')

    grid = Grid()
    grid.scores = pd.concat([grid1, grid2])
    
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
                    #fig = plt.figure(figsize=(5,5))
                    my_dpi=300
                    fig = plt.figure(figsize=(4, 4))
                    ax = fig.add_subplot(111)
                    ax.set_xlim([0,0.65])
                    ax.set_ylim([-0.05,1.05])
                    '''
                    if N==5000:
                        ax.set_xlim([0.05,0.65])
                        ax.set_ylim([0.95,1.002])
                    else:
                        ax.set_xlim([0.05,0.65])
                        ax.set_ylim([0.75,1.02])
                    '''
                    title = 'N: ' + str(N) + ', γ: ' + str(t1) + ', β:' + str(beta) + ', k: ' + str(k)
                    ax.set_title(title)
                    ax.set_xlabel('μ')
                    ax.set_ylabel('NMI')
                    for method in methods:
                        N_condition = (grid.scores['N'] == N)
                        t1_condition = (grid.scores['t1'] == t1)
                        beta_condition = (grid.scores['beta'] == beta)
                        method_condition = (grid.scores['METHOD'] == method)
                        k_condition = (grid.scores['k'] == k)
                        data = grid.scores[N_condition & t1_condition & beta_condition & method_condition & k_condition]
                        if(method=='K1'): color='r'; label='K1'; marker='^'; 
                        if(method=='M1'): color='g'; label='M1'; marker='<';
                        if(method=='R1'): color='b'; label='R1'; marker='>';
                        # average over multiple runs
                        x = data['mut']
                        y = data['SCORE']
                        mut_01_condition = (x == 0.1); y_01 = y[mut_01_condition]
                        mut_02_condition = (x == 0.2); y_02 = y[mut_02_condition]
                        mut_03_condition = (x == 0.3); y_03 = y[mut_03_condition]
                        mut_04_condition = (x == 0.4); y_04 = y[mut_04_condition]
                        mut_05_condition = (x == 0.5); y_05 = y[mut_05_condition]
                        mut_06_condition = (x == 0.6); y_06 = y[mut_06_condition]
                        ci_01 = sms.DescrStatsW(y_01).tconfint_mean()
                        ci_02 = sms.DescrStatsW(y_02).tconfint_mean()
                        ci_03 = sms.DescrStatsW(y_03).tconfint_mean()
                        ci_04 = sms.DescrStatsW(y_04).tconfint_mean()
                        ci_05 = sms.DescrStatsW(y_05).tconfint_mean()
                        ci_06 = sms.DescrStatsW(y_06).tconfint_mean()
                        # plot average as points
                        y_avg = [np.mean(ci_01), np.mean(ci_02), np.mean(ci_03), np.mean(ci_04), np.mean(ci_05), np.mean(ci_06)]
                        x_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
                        plt.scatter(x_avg, y_avg, color=color, label=label, marker=marker)
                        '''
                        # plot average as a smooth curve
                        xsmooth = np.linspace(x.min(),x.max(),300)
                        f_avg = interpolate.interp1d(x_avg, y_avg, kind='cubic')
                        ysmooth_avg = f_avg(xsmooth)
                        plt.plot(xsmooth, ysmooth_avg,color=color) #label=label)
                        # plot confidence intervals
                        y_lower = [np.mean([min(y_01),y_avg[0]]),np.mean([min(y_02),y_avg[1]]),np.mean([min(y_03),y_avg[2]]),np.mean([min(y_04),y_avg[3]]),np.mean([min(y_05),y_avg[4]]),np.mean([min(y_06),y_avg[5]])] #y_lower = [ci_01[0],ci_02[0],ci_03[0],ci_04[0],ci_05[0],ci_06[0]]
                        f_lower = interpolate.interp1d(x_avg, y_lower, kind='cubic')
                        ysmooth_lower = f_lower(xsmooth)
                        y_upper = [np.mean([max(y_01), y_avg[0]]),
                            np.mean([max(y_02), y_avg[1]]),
                            np.mean([max(y_03),y_avg[2]]),
                            np.mean([max(y_04), y_avg[3]]),
                            np.mean([max(y_05), y_avg[4]]),
                            np.mean([max(y_06),y_avg[5]])]#y_upper = [ci_01[1],ci_02[1],ci_03[1],ci_04[1],ci_05[1],ci_06[1]]
                        f_upper = interpolate.interp1d(x_avg, y_upper, kind='cubic')
                        ysmooth_upper = f_upper(xsmooth)
                        plt.fill_between(xsmooth, ysmooth_lower, ysmooth_upper, alpha=0.3, facecolor=color'
                        '''
                    ax.legend(loc='best')
                    fig.savefig(out_folder_beta + 'k_' + str(k) + '.png', dpi=my_dpi)
                    plt.close()

if __name__ == '__main__':
    print("\n---------------------------PLOTTING DreamDMI BENCHMARKS-------------------------\n")
    run()
    print("\n-------------------------DONE PLOTTING DreamDMI BENCHMARKS-----------------------\n")
