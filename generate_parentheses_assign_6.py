#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

#Input: n = 1
#Output: ["()"]

def generate_parentheses(num):
    print("The input number is",num)
    ans =[]

    def gen(o,c,s):
        if o>c:
            return
        if o==0 and c==0:
            ans.append(s)
            return
        if o==0:
            gen(o,c-1,s+')')
        else:
            gen(o-1,c,s+'(')
            gen(o,c-1,s+')')
    gen(num,num,'')
    print("The output array is :",ans)

if __name__ == "__main__":
    num = 3
    generate_parentheses(num)