qtd=(int(input("Enter with the quantity: ")))
if(qtd<1):
    while True:
        print("Error! The quantity needs to be positive")
        qtd=(int(input("Enter with the quantity: ")))
        if not(qtd<1):
            break


number=[]

for i in range(qtd):
    number.append(float(input("Enter with the number: ")))
    if(number[i]<0):
        print("This position in list had the negative number converted to be a positive number")
        print("Pre-converted number: ", number[i])

        number[i]=number[i]*-1
        
        print("Converted number: ", number[i])
    elif(number[i]>0):
        print("This position in list had the positive number converted to be a negative number")
        print("Pre-converted number: ", number[i])

        number[i]=number[i]*-1

        print("Converted number: ", number[i])
    else: 
        print("Zero is a neutral number")
    


