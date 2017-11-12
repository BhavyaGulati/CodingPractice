'''Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.'''

import math
class Solution(object):
    def firstMissingPositive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(arr)
        j=0
        for i in range(size):
            if arr[i]<=0:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                j+=1
        print arr
        narr=arr[j:]
        print narr
        size=len(narr)
        print size
        for i in range(size):
            if(abs(narr[i]) - 1 < size):
                if(narr[abs(narr[i]) - 1] > 0):
                    narr[abs(narr[i]) - 1] = -narr[abs(narr[i]) - 1]
                    
        for i in range(size):
            if (narr[i] > 0):
                return i+1;  #// 1 is added becuase indexes 
                       #// start from 0
      
        return size+1;
            
        