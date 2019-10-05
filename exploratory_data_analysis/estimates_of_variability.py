"""
    Chapter 1: Exploratory Data Analysis: Estimates of Variability - Page 40
    Contains Functions:
        Variance
        Standard Deviation
        Mean Absolute Deviation (MAD)
        MAD from the median
        Range
        Percentile
        Interquantile Range
"""

import math
import random

class EOV:

    def variance(self,num_range=10):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        #compute mean
        sum = 0
        for rand_int in rand_int_list:
            sum+=rand_int
        mean = sum/num_range

        #compute variance
        sum = 0
        for rand_int in rand_int_list:
            sum+=(rand_int - mean)**2
        variance = sum/num_range-1

        return variance

    def mean_absolute_deviation(self,num_range=10):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        #compute mean
        sum = 0
        for rand_int in rand_int_list:
            sum+=rand_int
        mean = sum/num_range

        #compute mean absolute deviation
        sum = 0
        for rand_int in rand_int_list:
            sum+=(rand_int - mean)
        mad = sum/num_range-1

        return mad

    def standard_deviation(self,num_range=10):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        #compute mean
        sum = 0
        for rand_int in rand_int_list:
            sum+=rand_int
        mean = sum/num_range

        #compute variance
        sum = 0
        for rand_int in rand_int_list:
            sum+=(rand_int - mean)**2   #square every value
        variance = sum/num_range-1

        standard_deviation = math.sqrt(variance)    #standard deviation is just the square root of variance

        return standard_deviation

    def median_absolute_deviation(self,num_range):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        #compute median
        median = self.__get_median(rand_int_list)
        n_list = []
        for rand_int in rand_int_list:
            n_list.append(rand_int - median)

        median_abs_deviation = self.__get_median(n_list)
        
        return median_abs_deviation

    def interquantile_range(self,num_range):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        rand_int_list = sorted(rand_int_list)   #sort data 
        mid_point = int(len(rand_int_list)/2)
        if (len(rand_int_list)%2) != 0:
            q1 = rand_int_list[0:mid_point]
            q2 = rand_int_list[mid_point+1:len(rand_int_list)]
        else:
            q1 = rand_int_list[0:mid_point]
            q2 = rand_int_list[mid_point:len(rand_int_list)]

        median_q1 = self.__get_median(q1)
        median_q2 = self.__get_median(q2)

        iqr = median_q2 - median_q1

        return iqr

    def percentile(self,num_range,P):
        rand_int_list =[random.randint(1,num_range) for i in range(num_range)]
        print(rand_int_list)

        rand_int_list = sorted(rand_int_list)   #sort data

        ord_rank = (P/100)/len(rand_int_list)

        return ord_rank

    def __get_median(self,num_list):
        num_range = len(num_list)
        if (num_range % 2) == 0:
            mid = int(num_range/2)
            mid_1 = mid - 1
            mid_2 = mid
            median = (num_list[mid_1]+num_list[mid_2])/2
        else:
            mid = int(num_range/2)
            median = num_list[mid]
            
        return median


# if __name__ == '__main__':
#     IQR = EOV().interquantile_range(10)
#     print(IQR)
