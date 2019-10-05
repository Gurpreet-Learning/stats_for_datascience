"""
    Chapter 1: Exploratory Data Analysis: Correlations - Page 72
    Contains Functions:
        Correlation Coefficient
        Correlation Matrix
        Scatterplot
"""
import math
import random
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class collerations:

    def corelation_coefficent(self,num_range=10,x_vals = None,y_vals = None):
        '''
            Gets pearsons r correlation coefficient
        '''
        if x_vals is None and y_vals is None:
            #create random vals of x and y if values is none
            x_vals = [random.randint(1,num_range) for i in range(num_range)]
            y_vals = [random.randint(1,num_range) for i in range(num_range)]

        x_mean = statistics.mean(x_vals)
        y_mean = statistics.mean(y_vals)

        ssm = 0 #summation for val where pval is (xi-xmean)*(yi-ymean)
        ssx_squared = 0 #summation of squared x pval
        ssy_squared = 0 #summation of squared y pval
        for i in range(num_range):
            pval = (x_vals[i]-x_mean)*(y_vals[i]-y_mean)
            ssm+= pval
            ssx_squared += (x_vals[i]-x_mean)**2
            ssy_squared += (y_vals[i]-y_mean)**2
        
        r = ssm/math.sqrt(ssx_squared*ssy_squared)  #correlation coefficient
        return r

    def correlation_matrix(self,num_range=10):
        labels = ['A','B','C','D']
        data_vals = []

        #create data
        for i in range(num_range):
            data_vals.append([random.randint(1,num_range) for i in range(len(labels))])   #create random val for each rows
        df = pd.DataFrame(data_vals,columns=labels) #create dataframe
        print('>>Data Generated<<')
        print(df)

        #create matrix plotting points
        m_matrix_plot = []
        for label_y in labels:
            sub_row = []
            for label_x in labels:
                plot = label_y+'-'+label_x
                sub_row.append(plot)
            m_matrix_plot.append(sub_row)
        m_matrix_r = []

        #create correlation matrix
        for row in m_matrix_plot:
            r_row=[]
            for plot in row:
                plot = plot.split('-')
                x_col = plot[0]
                y_col = plot[1]
                x_vals = list(df[x_col])
                y_vals = list(df[y_col])
                r = self.corelation_coefficent(x_vals=x_vals,y_vals=y_vals)
                r_row.append(r)
            m_matrix_r.append(r_row)
        correlation_matrix = pd.DataFrame(m_matrix_r,columns=labels,index=labels)
        print("\n>>Correlation Matrix<<")
        print(correlation_matrix)
        pass

    def scatterplot(self,num_range=10):
        #create scatterplot using matplotlib
        x_vals = np.array([random.randint(1,num_range) for i in range(num_range)])
        y_vals = np.array([random.randint(1,num_range) for i in range(num_range)])
        colors = np.random.rand(num_range)
        plt.scatter(x_vals, y_vals,c=colors)
        plt.show()
        

if __name__ == '__main__':
    collerations().scatterplot(100)