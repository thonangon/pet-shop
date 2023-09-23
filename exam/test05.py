scoreStudent=[ {'name': 'Nit', 'subject': 'Algorithm', 'score': 10}, 
{'name': 'Visal', 'subject': 'PL', 'score': 80}, 
{'name': 'Dyna', 'subject': 'Algorithm', 'score': 49}, 
{'name': 'Virak','subject': 'English', 'score': 50}, 
 ]
count=0
result=""
for key in scoreStudent:
    if key["subject"]=="Algorithm" and key["score"]<50:
        result= result+" " + key['name']+" "
        count+=1
print(str(count)+" students failed algorithm: " + result)