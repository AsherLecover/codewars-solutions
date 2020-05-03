#Complete the solution so that the function will break up camel casing, using a space between words.

#Example
#solution("camelCasing")  ==  "camel Casing"

def solution(s):
    result = ""
    for i in s:
        if i != i.lower():
            result += " " + i
        else:
            result += i
    return result