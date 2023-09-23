def reverseText(string):
    reverse=[]
    for i in string:
        result=""
        for j in range(len(i)):
            result=result+i[-(j+1)]
        reverse.append(result)
    return reverse
string=["banana", "coconut"]
print(reverseText(string))