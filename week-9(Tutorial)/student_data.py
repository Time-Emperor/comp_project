with open('file.txt','r') as file:
    lines=file.readlines()
    dict=[]
    for line in lines:
        data=line.strip().split(",")
        #print(data)
        for i in range(len(data)):
            dict[data[0]]=[data[1],int(data[2])]
        print(dict)

        id=input("Enter id: ")
        if id in dict:
            try:
                marks=int(input("Enter marks: "))
                value=dict[id]