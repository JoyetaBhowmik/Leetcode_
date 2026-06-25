class Solution(object):
    def twoSum(self, nums, target):
       hashmap={}
       for i,num in enumerate(nums):
          com = target-num 
          if com in hashmap:
            return [hashmap[com],i]
          hashmap[num]=i
        