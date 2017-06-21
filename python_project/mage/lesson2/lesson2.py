#encoding: utf-8

users = []

while True:
    input_text = input("please enter the command ( find,list,add,delete,update,exit ) : ")

    if input_text == "list" :
        if len(users) == 0:
            print("no any user")
        else:
            print("the count of users is ",len(users))
            for v in users :
                print("name:{}  age:{}  tel:{}".format(v[0],v[1],v[2]))
    elif input_text == "find" :
        input_name = input("please enter the name to find : ")
        for v in users:
            if v[0] == input_name :
               print("name:{}  age:{}  tel:{}".format(v[0],v[1],v[2]))
               break
        else:
            print("can not find user")
    elif input_text == "add" :
        input_name = input("please enter the name to add : ")
        input_age = input("please enter the age to add : ")
        input_tel = input("please enter the telephone number to add : ")
        for v in users:
            if v[0] == input_name :
               print("the name have already added")
               break
        else:
            users.append([input_name,input_age,input_tel])
            print("the new user add successfully")
    elif input_text == "update" :
        input_name = input("please enter the name to update : ")
        input_age = input("please enter the age to add : ")
        input_tel = input("please enter the telephone number to add : ")
        for v in users:
            if v[0] == input_name :
               v[1] = input_age
               v[2] = input_tel
               print("the {} information is updated".format(input_name))
               break
        else:
            print("can not find user")
    elif input_text == "delete" :
        input_name = input("please enter the name to delete : ")
        for v in users:
            if v[0] == input_name :
               users.remove(v)
               print("the {} information is deleted".format(input_name))
               break
        else:
            print("can not find user")
    elif input_text == "exit" :
        print("the management over")
        break