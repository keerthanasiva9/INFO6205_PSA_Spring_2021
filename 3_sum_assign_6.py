#Given an array nums of n integers, are there elements a, b, c in nums
# such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#The solution set must not contain duplicate triplets.

#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

def threesum(arr):
    print("The input array is",arr)
    res = []

    #Sorting the input array
    arr.sort()

    #creating a set because we dont want duplicate triplets
    non_dup_set = set()

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                first,second,third = arr[i],arr[j],arr[k]
                if first + second + third == 0 and (first,second,third) not in non_dup_set:
                    res.append([first,second,third])
                    non_dup_set.add((first,second,third))
    print("The output array is:",res)



if __name__ == "__main__":
    arr = [-1,0,1,2,-1,-4]
    threesum(arr)