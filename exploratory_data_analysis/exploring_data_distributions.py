"""
    Chapter 1: Exploratory Data Analysis: Exploring Data Distributions - Page 49
    Contains Functions:
        Boxplot
        Histogram
        Density Plot
        Frequency Table
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random

class explore_data:

    def boxplot(self,num_range=10):
        #Will create a boxplot using matplotlib
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]  # create random variable
        df = pd.DataFrame(np.array(rand_int_list),columns=['vals'])
        plt.boxplot(df["vals"])
        plt.show()

    def histogram(self,num_range=10,n_bins=3):
        #Will create a histogram using matplotlib
        rand_int_list = np.array([random.randint(1,num_range) for i in range(num_range)]) #create random variables
        plt.hist(rand_int_list, normed=True, bins=n_bins)
        plt.show()
        
    def density_plot(self,num_range=10):
        #create density plot using seaborn
        rand_int_list = np.array([random.randint(1,num_range) for i in range(num_range)]) #create random variables
        sns.set_style('whitegrid')
        sns.kdeplot(np.array(rand_int_list))
        plt.show()

    def frequency_table(self,num_range=10,n_bins=3):
        # create frequency table 
        rand_int_list = [random.randint(1,num_range) for i in range(num_range)] #create random vals
        rand_int_list = sorted(rand_int_list)
        m_list = []
        bin_c = 0
        n_bin = []
        n_bins = int(num_range/n_bins)
        print(n_bins)
        #assign values to bins
        for v_idx,val in enumerate(rand_int_list):
            if bin_c < n_bins:
                n_bin.append(val)
                bin_c+=1
            else:
                n_bin = []
                n_bin.append(val)
                bin_c = 1
            if len(n_bin) == n_bins:
                m_list.append(n_bin)
            elif v_idx == len(rand_int_list)-1:
                print(n_bin)
                prev_bin = m_list[len(m_list)-1]
                for excess_val in n_bin:
                    prev_bin.append(excess_val)
                m_list[len(m_list)-1] = prev_bin

        #create frequency table
        n_bin_list = []
        for b_idx,bin in enumerate(m_list):
            bin_len = len(bin)
            n_bin_list.append([b_idx,bin_len])      
        frequency_table = pd.DataFrame(n_bin_list,columns = ['Bin Number','Bin Values Count'])
        print('Frequency Table')
        print(frequency_table)
# if __name__ == '__main__':
#     explore_data().frequency_table(num_range=100,n_bins=3)