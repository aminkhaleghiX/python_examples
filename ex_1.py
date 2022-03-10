

n = int(input("Please Enter number of users: "))

users = []
for i in range(n):
    user = {
        "name": input("Name: "),
        "age" : int(input("Age: "))
    }
    users.append(user)

search_name = input("please Enter a name for search in users: ")
for user in users:
    if user["name"].lower() == search_name.lower():
        search_name = ""
        print(user["age"])
        break
    

if search_name != "":
    print("User Not Found")