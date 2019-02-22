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
    grid5 = Grid().scores = pd.read_csv("../graphs/grid5.tsv", sep='\t')
    grid6 = Grid().scores = pd.read_csv("../graphs/grid6.tsv", sep='\t')
    grid6b = Grid().scores = pd.read_csv("../graphs/grid6.tsv", sep='\t') # "6" is the only 8k experiment
    grid7 = Grid().scores = pd.read_csv("../graphs/grid7.tsv", sep='\t')
    grid7b = Grid().scores = pd.read_csv("../graphs/grid7.tsv", sep='\t') # only 10k
    grid8 = Grid().scores = pd.read_csv("../graphs/grid8.tsv", sep='\t')
    grid9 = Grid().scores = pd.read_csv("../graphs/grid9.tsv", sep='\t')
    grid10 = Grid().scores = pd.read_csv("../graphs/grid10.tsv", sep='\t')
    grid10b = Grid().scores = pd.read_csv("../graphs/grid10.tsv", sep='\t') # only 300
    grid11 = Grid().scores = pd.read_csv("../graphs/grid11.tsv", sep='\t')
    grid12 = Grid().scores = pd.read_csv("../graphs/grid12.tsv", sep='\t')
    grid12b = Grid().scores = pd.read_csv("../graphs/grid12.tsv", sep='\t')


    grid = Grid()
    grid.scores = pd.concat([
        grid5, 
        grid6,
        grid6b,
        grid7,
        grid7b,
        grid8,
        grid9,
        grid10,
        grid10b,
        grid11,
        grid12,
        grid12b])

    methods = ['R1', 'M1', 'K1', 'louvain']

    ###################################################################################################################
    # SUMMARY PLOT RESOURCES time vs N  ###############################################################################
    ###################################################################################################################
    out_folder = '../graphs/'
    my_dpi = 300
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)
    #ax.set_xlim([0, 0.65])
    #ax.set_ylim([0.65, 1.02])
    title = 'time (sec) vs N'
    ax.set_title(title)
    ax.set_xlabel('N')
    ax.set_ylabel('sec')
    x = [300, 500, 1000, 2000, 3000, 5000, 7000, 8000]

    #R1
    color = 'b'; label = 'R1'; marker = '>';
    y = [
        np.mean([37,30,26,32,34]),
        np.mean([24]),
        np.mean([50]),
        np.mean([106]),
        np.mean([118,113,117,137]),
        np.mean([198,222,236,276]),
        np.mean([313]),
        np.mean([392])
    ]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)


    #M1
    color = 'g'; label = 'M1'; marker = '<';
    y = [
        np.mean([30,53,64,61,77]),
        np.mean([91]),
        np.mean([90]),
        np.mean([150]),
        np.mean([232,240,235,241]),
        np.mean([504,505,539,618]),
        np.mean([191]),
        np.mean([237])
        ]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    #K1
    color = 'r'; label = 'K1'; marker = '^';
    y = [
        np.mean([5,8,8,9,10,11]),
        np.mean([6]),
        np.mean([14]),
        np.mean([54]),
        np.mean([111,111,118,127]),
        np.mean([433,565,600,402]),
        np.mean([870]),
        np.mean([1260])
        ]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    #louvain
    color='gray'; label='louvain'; marker='o';
    y = [1,1,1,1,1,2,2,2]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    ax.legend(loc='best')
    fig.savefig(out_folder + 'time_vs_N.png', dpi=my_dpi)
    plt.close()

    ###################################################################################################################
    # SUMMARY PLOT RESOURCES max RAM vs N  ############################################################################
    ###################################################################################################################
    out_folder = '../graphs/'
    my_dpi = 300
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)
    #ax.set_xlim([0, 0.65])
    #ax.set_ylim([0.65, 1.02])
    title = 'RAM (max) vs N'
    ax.set_title(title)
    ax.set_xlabel('N')
    ax.set_ylabel('MB')
    x = [300, 500, 1000, 2000, 3000, 5000, 7000, 8000]
 
    #R1
    color = 'b'; label = 'R1'; marker = '>';
    ci_300 = sms.DescrStatsW([46, 106,22,98,36,56]).tconfint_mean()
    ci_500 = sms.DescrStatsW([52,38,36,38,32,29,65,51,38]).tconfint_mean()
    ci_1k = sms.DescrStatsW([45,82,12,36,57,39]).tconfint_mean()
    ci_2k = sms.DescrStatsW([82,60,96,89,84,81]).tconfint_mean()
    ci_3k = sms.DescrStatsW([57,118,131,162]).tconfint_mean()
    ci_5k = sms.DescrStatsW([141,255,341,538]).tconfint_mean()
    ci_7k = sms.DescrStatsW([280,281]).tconfint_mean()
    ci_8k = sms.DescrStatsW([337,338]).tconfint_mean()
    y = [np.mean(ci_300),np.mean(ci_500),np.mean(ci_1k),np.mean(ci_2k),np.mean(ci_3k),np.mean(ci_5k),np.mean(ci_7k),np.mean(ci_8k)]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    #M1
    color = 'g'; label = 'M1'; marker = '<';
    ci_300 = sms.DescrStatsW([89,31,36,81]).tconfint_mean()
    ci_500 = sms.DescrStatsW([36,31,31,46,35]).tconfint_mean()
    ci_1k = sms.DescrStatsW([68,55,64,135,47,41]).tconfint_mean()
    ci_2k = sms.DescrStatsW([46,29,34,42,47,76]).tconfint_mean()
    ci_3k = sms.DescrStatsW([58,70,254,218]).tconfint_mean()
    ci_5k = sms.DescrStatsW([90,91,686,422,1222]).tconfint_mean()
    ci_7k = sms.DescrStatsW([188,189]).tconfint_mean()
    ci_8k = sms.DescrStatsW([37,38]).tconfint_mean()
    y = [np.mean(ci_300),np.mean(ci_500),np.mean(ci_1k),np.mean(ci_2k),np.mean(ci_3k),np.mean(ci_5k),np.mean(ci_7k),np.mean(ci_8k)]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    #K1
    color = 'r'; label = 'K1'; marker = '^';
    ci_300 = sms.DescrStatsW([79,28,27,68,44,62]).tconfint_mean()
    ci_500 = sms.DescrStatsW([17,18,28,18,18,33,26]).tconfint_mean()
    ci_1k = sms.DescrStatsW([41,37,31,19,10,110]).tconfint_mean()
    ci_2k = sms.DescrStatsW([102,72,85,73,122,162]).tconfint_mean()
    ci_3k = sms.DescrStatsW([153,245,297,643]).tconfint_mean()
    ci_5k = sms.DescrStatsW([114,577,310,317]).tconfint_mean()
    ci_7k = sms.DescrStatsW([429,430]).tconfint_mean()
    ci_8k = sms.DescrStatsW([382,383]).tconfint_mean()
    y = [np.mean(ci_300),np.mean(ci_500),np.mean(ci_1k),np.mean(ci_2k),np.mean(ci_3k),np.mean(ci_5k),np.mean(ci_7k),np.mean(ci_8k)]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)


    #louvain
    color='gray'; label='louvain'; marker='o';
    ci_300 = sms.DescrStatsW([6,7]).tconfint_mean()
    ci_500 = sms.DescrStatsW([5,6]).tconfint_mean()
    ci_1k = sms.DescrStatsW([8,9]).tconfint_mean()
    ci_2k = sms.DescrStatsW([10,21]).tconfint_mean()
    ci_3k = sms.DescrStatsW([10,7,8,3]).tconfint_mean()
    ci_5k = sms.DescrStatsW([8,4,4]).tconfint_mean()
    ci_7k = sms.DescrStatsW([8,9]).tconfint_mean()
    ci_8k = sms.DescrStatsW([6,7]).tconfint_mean()
    y = [np.mean(ci_300),np.mean(ci_500),np.mean(ci_1k),np.mean(ci_2k),np.mean(ci_3k),np.mean(ci_5k),np.mean(ci_7k),np.mean(ci_8k)]
    plt.scatter(x, y, color=color, label=label, marker=marker, alpha=0.3)

    ax.legend(loc='best')
    fig.savefig(out_folder + 'RAM_vs_N.png', dpi=my_dpi)
    plt.close()

    ###################################################################################################################
    # SUMMARY PLOT NMI vs mu  #########################################################################################
    ###################################################################################################################
    out_folder = '../graphs/'
    my_dpi = 300
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 0.65])
    ax.set_ylim([0.85, 1.02])
    title = 'NMI vs mu'
    ax.set_title(title)
    ax.set_xlabel('μ')
    ax.set_ylabel('NMI')
    for method in methods:
        N_condition_5k = (grid.scores['N'] == 5000)
        N_condition_7k = (grid.scores['N'] == 7000)
        N_condition_8k = (grid.scores['N'] == 8000)
        N_condition_10k = (grid.scores['N'] == 10000)
        N_condition_15k = (grid.scores['N'] == 15000)

        method_condition = (grid.scores['METHOD'] == method)
        data = grid.scores[method_condition & (N_condition_5k | N_condition_7k | N_condition_8k | N_condition_10k )]
        if(method == 'K1'): color = 'r'; label = 'K1'; marker = '^'; 
        if(method == 'M1'): color = 'g'; label = 'M1'; marker = '<';
        if(method == 'R1'): color = 'b'; label = 'R1'; marker = '>';
        if(method=='louvain'): color='gray'; label='louvain'; marker='o';
                        
        # average over multiple runs: determine confidence interval
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
        # plot average of confidence interval
        y_avg = [np.mean(ci_01), np.mean(ci_02), np.mean(ci_03), np.mean(ci_04), np.mean(ci_05), np.mean(ci_06)]
        x_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
        plt.scatter(x_avg, y_avg, color=color, label=label, marker=marker, alpha=0.3)
    ax.legend(loc='best')
    fig.savefig(out_folder + 'NMI_vs_mu.png', dpi=my_dpi)
    plt.close()


    ###################################################################################################################
    # SUMMARY PLOT NMI vs N  ###########################################################################################
    ###################################################################################################################
    out_folder = '../graphs/'
    my_dpi = 300
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)
    #ax.set_xlim([0, 0.65])
    ax.set_ylim([0.65, 1.02])
    title = 'NMI vs N'
    ax.set_title(title)
    ax.set_xlabel('N')
    ax.set_ylabel('NMI')
    for method in methods:
        method_condition = (grid.scores['METHOD'] == method)
        data = grid.scores[method_condition]
        if(method == 'K1'): color = 'r'; label = 'K1'; marker = '^'; 
        if(method == 'M1'): color = 'g'; label = 'M1'; marker = '<';
        if(method == 'R1'): color = 'b'; label = 'R1'; marker = '>';
        if(method=='louvain'): color='gray'; label='louvain'; marker='o';
                        
        # average over multiple runs: determine confidence interval
        x = data['N']
        y = data['SCORE']
        N_01_condition = (x == 300); y_01 = y[N_01_condition]
        N_02_condition = (x == 500); y_02 = y[N_02_condition]
        N_03_condition = (x == 1000); y_03 = y[N_03_condition]
        N_04_condition = (x == 2000); y_04 = y[N_04_condition]
        N_05_condition = (x == 3000); y_05 = y[N_05_condition]
        N_06_condition = (x == 5000); y_06 = y[N_06_condition]
        N_07_condition = (x == 7000); y_07 = y[N_07_condition]
        N_08_condition = (x == 8000); y_08 = y[N_08_condition]
        N_09_condition = (x == 10000); y_09 = y[N_09_condition]
        N_10_condition = (x == 15000); y_10 = y[N_10_condition]

        ci_01 = sms.DescrStatsW(y_01).tconfint_mean()
        ci_02 = sms.DescrStatsW(y_02).tconfint_mean()
        ci_03 = sms.DescrStatsW(y_03).tconfint_mean()
        ci_04 = sms.DescrStatsW(y_04).tconfint_mean()
        ci_05 = sms.DescrStatsW(y_05).tconfint_mean()
        ci_06 = sms.DescrStatsW(y_06).tconfint_mean()
        ci_07 = sms.DescrStatsW(y_07).tconfint_mean()
        ci_08 = sms.DescrStatsW(y_08).tconfint_mean()
        ci_09 = sms.DescrStatsW(y_09).tconfint_mean()
        ci_10 = sms.DescrStatsW(y_10).tconfint_mean()

        # plot average of confidence interval
        y_avg = [np.mean(ci_01), np.mean(ci_02), np.mean(ci_03), np.mean(ci_04), np.mean(ci_05), np.mean(ci_06), np.mean(ci_07), np.mean(ci_08), np.mean(ci_09), np.mean(ci_10)]
        x_avg = [300, 500, 1000, 2000, 3000, 5000, 7000, 8000, 10000, 15000]
        plt.scatter(x_avg, y_avg, color=color, label=label, marker=marker, alpha=0.3)
    ax.legend(loc='best')
    fig.savefig(out_folder + 'NMI_vs_N.png', dpi=my_dpi)
    plt.close()


    ###################################################################################################################
    # DETAILED PLOTS (as a function of all parameters)   ##############################################################
    ###################################################################################################################
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
                        if(method=='louvain'): color='gray'; label='louvain'; marker='o';

                        # average over multiple runs: determine confidence interval
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
                        # plot average of confidence interval
                        y_avg = [np.mean(ci_01), np.mean(ci_02), np.mean(ci_03), np.mean(ci_04), np.mean(ci_05), np.mean(ci_06)]
                        x_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
                        plt.scatter(x_avg, y_avg, color=color, label=label, marker=marker, alpha=0.3)
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
                    
                    
    ###################################################################################################################
    # DETAILED PLOTS (one for each N folder)   ########################################################################
    ###################################################################################################################
    for N in grid.N:
        out_folder_N = '../graphs/_N' + str(N) + '/'
        my_dpi = 300
        fig = plt.figure(figsize=(4, 4))
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 0.65])
        ax.set_ylim([-0.05, 1.05])
        '''
        if N==5000:
            ax.set_xlim([0.05,0.65])
            ax.set_ylim([0.95,1.002])
        else:
            ax.set_xlim([0.05,0.65])
            ax.set_ylim([0.75,1.02])
        '''
        title = 'N: ' + str(N)
        ax.set_title(title)
        ax.set_xlabel('μ')
        ax.set_ylabel('NMI')
        for method in methods:
            N_condition = (grid.scores['N'] == N)
            method_condition = (grid.scores['METHOD'] == method)
            data = grid.scores[N_condition & method_condition]
            if(method == 'K1'): color = 'r'; label = 'K1'; marker = '^'; 
            if(method == 'M1'): color = 'g'; label = 'M1'; marker = '<';
            if(method == 'R1'): color = 'b'; label = 'R1'; marker = '>';
            if(method=='louvain'): color='gray'; label='louvain'; marker='o';
                        
            # average over multiple runs: determine confidence interval
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
            # plot average of confidence interval
            y_avg = [np.mean(ci_01), np.mean(ci_02), np.mean(ci_03), np.mean(ci_04), np.mean(ci_05), np.mean(ci_06)]
            x_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
            plt.scatter(x_avg, y_avg, color=color, label=label, marker=marker, alpha=0.3)
        ax.legend(loc='best')
        fig.savefig(out_folder_N + str(N) +'.png', dpi=my_dpi)
        plt.close()




if __name__ == '__main__':
    print("\n---------------------------PLOTTING DreamDMI BENCHMARKS-------------------------\n")
    run()
    print("\n-------------------------DONE PLOTTING DreamDMI BENCHMARKS-----------------------\n")
