# listOflist=[
# {'name': "Jackma", 'status': True}, 
# {'name': "Kolap baelen", 'status': False}, 
# {'name': "Tom Teav", 'status': True}, 
# {'name': "Elon mask", 'status': False}, 
# {'name' :"Leadership", 'status' : True} ]
# count=0
# for i in listOflist:
#     if i ['status'] ==True:
#         count +=1
# print(count)


def countStatus(status):
    count=0
    for i in status:
        if i ['status'] ==True:
            count +=1
    return count
status=[
{'name': "Jackma", 'status': True}, 
{'name': "Kolap baelen", 'status': False}, 
{'name': "Tom Teav", 'status': True}, 
{'name': "Elon mask", 'status': False}, 
{'name' :"Leadership", 'status' : True} ]
print(countStatus(status))