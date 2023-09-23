filterTheName=["Champa","Kanha","Chompei","Meta","Dara"]
result=[]
for i in filterTheName:
    count=0
    for j in range(len(i)):
        if i[j]=="a":
            count+=1
    if count>=2:
        result.append(i)
print(result)