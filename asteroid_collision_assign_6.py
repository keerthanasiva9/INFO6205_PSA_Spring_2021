#We are given an array asteroids of integers representing asteroids in a row.
#For each asteroid, the absolute value represents its size, and the sign represents
# its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet

#Input: asteroids = [10,2,-5]
#Output: [10]
#Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

#Input: asteroids = [-2,-1,1,2]
#Output: [-2,-1,1,2]
#Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet each other.


class Solution:
    def asteroid_collision(self,arr):

        print("The input array is:", arr)
        res = []

        for i in arr:
            while res and res[-1] > 0 and i < 0:
                if res[-1] + i < 0:
                    res.pop()

                elif res[-1] + i > 0:
                    break

                else:
                    res.pop();
                    break
            else:
                res.append(i)
        return res

l1 = Solution()

arr = [-2,-1,1,2]
print("The output after collision is:",l1.asteroid_collision(arr))





