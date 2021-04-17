#Longest Common Prefix

#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

#Input: strs = ["flower", "flow", "flight"]
#Output: "fl"

#Input: strs = ["dog", "racecar", "car"]
#Output: ""

def longest_common_prefix(strs):
    if not strs:
        return ""

    strs.sort()

    result = []

    for idx, char in enumerate(strs[0]):

        if char == strs[-1][idx]:
            result.append(char)
        else:
            break

    return "".join(result)


if __name__ == '__main__':
    s = ["flower", "flow", "flight"]
    print("The input is : ",s)
    print("The longest common prefix is:",longest_common_prefix(s))