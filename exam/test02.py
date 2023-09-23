dic1=[
{"ingredient" : "rice","quantity" : 100},
{"ingredient" : "beef", "quantity" : 50}
]
dic2=[
{"ingredient" : "banana", "quantity" : 100},
{"ingredient" : "beef", "quantity" : 200},
{"ingredient" : "rice", "quantity" : 300}
]
# def compareIngrediant(dic1,dic2):
for i in dic1:
    if i["ingredient"]=="rice":
            result1= i["quantity"]
    elif i["ingredient"]=="beef":
            result2=i["quantity"]
for j in dic2:
    if j["ingredient"]=="rice":
        result3= j["quantity"]
    elif j["ingredient"]=="beef":
        result4=j["quantity"]
if result3>=result1 and result4>=result2:
    print(True)
else:
    print(False)
