def f(s):
    return g(s,0)
def g(s,num = 0):
    if not s[0:3].isdigit() :
        return g(s[1:])
    if len(s) < 3:
        return 0
    if (s[0] < s[1] and s[1] > s[2]) or (s[0] > s[1] and s[1] < s[2]):
        return 1 + g(s[1:])
    return g(s[1:])
    
string = input("Enter your string : \n")
print(f(string))