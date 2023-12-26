import os
import csv
import pickle

id_list = []
name_list = []
sal_list = []
dep_list = []


def imptcsv():
    with open('emps_in.csv', 'r') as file:
        line = file.readline()
        while True:
            line = file.readline()
            if not line:
                break
            splitline = line.split(',')
            name, salary, dep = splitline
            name_list.append(name)
            dep_list.append(dep)
            id_list.append(len(id_list) + 1)
            sal_list.append(float(salary))
            print(f"id is: {len(id_list)}, name is {name}, salary is {float(salary)}, dept is {dep} ")

    input()

def findindx():
    searchedname = input("search by first name ")
    if searchedname == "":
        input()
    else:
        searchedNameLower = searchedname.lower()
        indxlist=[]
        for i, nm in enumerate(name_list):
            if nm.lower().startswith(searchedNameLower):
                indxlist.append(i)
        return indxlist

def srchfunc():
    srchlist= findindx()
    for i in srchlist:
      print(f"id: {id_list[i]} , name: {name_list[i]} , salary: {sal_list[i]} , dept is: {dep_list[i]}")
    input()


def delfunc():
    dellist = findindx()
    indicestoremove = []

    for i in dellist:
        print("deleting: ")
        print(f"id: {id_list[i]} , name: {name_list[i]} , salary: {float(sal_list[i])} , dept is: {dep_list[i]}")
        indicestoremove.append(i)

    for i in reversed(indicestoremove):
        name_list.pop(i)
        sal_list.pop(i)
        dep_list.pop(i)
        id_list.pop(i)
    input()


def exptfile():
    with open('output.txt' , 'w') as op:
        for i in range(len(name_list)):
            op.write(f"id: {id_list[i]} , name: {name_list[i]} , salary: {float(sal_list[i])} , dept is: {dep_list[i]}")
    input()


def addfun():
    x = input("enter name, salary, dept with commas in between ")

    splitip = x.split(',')
    if len(splitip) < 3:
        print("invalid ip")
        input()
    else:
        name, salary, dep = splitip

        stpname = name.strip()
        stpsalary = salary.strip()
        stpdep = dep.strip()

        name_list.append(stpname)
        dep_list.append(stpdep)
        id_list.append(len(id_list) + 1)
        if stpsalary.isnumeric():
            sal_list.append(float(stpsalary))
        else:
            stpsalary = 0
            sal_list.append(float(stpsalary))
        print(f"id is: {len(id_list)}, name is {stpname}, salary is {float(stpsalary)}, dept is {stpdep} ")
        input()

def showall():
    for i in range(len(name_list)):
        print(f"id: {id_list[i]} , name: {name_list[i]} , salary: {float(sal_list[i])} , dept is: {dep_list[i]}")
    input()

def expdeps():
    department_dict = {dep: [
        f"id: {id_list[i]}, name: {name_list[i]}, salary: {float(sal_list[i])}, dept is: {dep_list[i]}"
        for i, current_dep in enumerate(dep_list) if current_dep == dep
    ] for dep in set(dep_list)}

    with open('depT.txt', 'w') as output:
        for dep, employees in department_dict.items():
            output.write(f"Department: {dep}\n")
            [output.write(f"{emp_info}\n") for emp_info in employees]
            output.write('\n')
    input()


def pickleexp():
    data = {'id_list': id_list, 'name_list': name_list, 'sal_list': sal_list, 'dep_list': dep_list}
    with open('dataT.pkl', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
    print("Pickle file exprtd")
    input()

def imptpkl():
    global id_list, name_list, sal_list, dep_list
    try:
        with open('dataT.pkl', 'rb') as pickle_file:
            data = pickle.load(pickle_file)
            print("Loaded data:", data)
            id_list, name_list, sal_list, dep_list = data['id_list'], data['name_list'], data['sal_list'], data['dep_list']
        print("Pickle file imprtd")
    except FileNotFoundError:
        print("Pickle file not found, import it first")

    input()


t= True
while t:
    os.system("cls")
    print("welcome")
    print("1-new")
    print("2-search")
    print("3-delete")
    print("4-show all")
    print("5-end")
    print("6-import csv or pickle")
    print("7-export")
    print("8-export departments")
    print("9-export pickle")

    choice = input("choose process ")
    if choice == "":
        print("choice doesnt exist ")
        input()
    else:
        match choice:
            case '1':
                addfun()


            case '2':
                srchfunc()


            case '3':
                delfunc()
                input()

            case '4':
                showall()


            case '5':
                t = False

            case '6':
                importchoice = input("1-csv. 2-pickle. ")
                match importchoice:
                    case '1':
                        imptcsv()
                    case '2':
                        imptpkl()

            case '7':
                exptfile()

            case '8':
                expdeps()

            case '9':
                pickleexp()

            case _:
                print("option unavailable")
                input()
