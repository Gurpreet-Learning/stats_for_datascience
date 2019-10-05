"""
    Chapter 1: Exploratory Data Analysis: Estimates of Location - Page 28
    Contains Functions:
        Mean
        Mediam
        Weighted Mean
        Weighted Median
        Trimmed Mean
        #TODO: Weighted Median
"""

import random
class EOL:

    def mean(self,num_range=10):
        '''
            Formula: mean = sum(X)/len(X)
            where X is a collection of values
        '''
        rand_int_list =[random.randint(0,num_range) for i in range(num_range)]
        print(rand_int_list)
        sum = 0
        for rand_int in rand_int_list:
            sum+=rand_int
        mean = sum/num_range
        return mean

    def trimmed_mean(self,num_range=10):
        '''
            Formula: trimmed mean = sum(X[min+1:len(max-1)])/len(X)-2
        '''
        rand_int_list = sorted([random.randint(0,num_range) for i in range(num_range)])
        print(rand_int_list)
        sum = 0
        for i in range(1,num_range-1):
            sum+=rand_int_list[i]
        trimmed_mean = sum/num_range-2
        return trimmed_mean

    def weighted_mean(self,num_range)=10:
        '''
            Formula: weighted mean = sum(X*W)/sum(W)
            where X is a collection of values
        '''
        rand_int_list =[random.randint(0,num_range) for i in range(num_range)]
        weights = [random.randint(0,num_range) for i in range(num_range)]
        print(rand_int_list)
        print(weights)
        sum = 0
        for i,rand_int in enumerate(rand_int_list):
            sum+=rand_int*weights[i]
        w_sum = 0
        for weight in weights:
            w_sum += weight
        w_mean = sum/w_sum
        return w_mean

    def median(self,num_range=10):
        rand_int_list =sorted([random.randint(0,num_range) for i in range(num_range)])
        print(rand_int_list)
        if (num_range % 2) == 0:
            mid = int(num_range/2)
            mid_1 = mid - 1
            mid_2 = mid
            median = (rand_int_list[mid_1]+rand_int_list[mid_2])/2
        else:
            mid = int(num_range/2)
            median = rand_int_list[mid]
        return median

# if __name__ == '__main__':
#     mean = EOL().mean(10)
#     print(f'Mean: {mean}')
#     trimmed_mean = EOL().trimmed_mean(10)
#     print(f'Trimmed Mean: {trimmed_mean}')
#     weigted_mean = EOL().weighted_mean(10)
#     print(f'Weighted Mean: {trimmed_mean}')
#     median = EOL().median(10)
#     print(f'Median: {median}')