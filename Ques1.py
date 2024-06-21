#input= Aeroplane
# outputs = eAeroplan
#           neAeropla

str = input("enter string")

for i in range(len(str)):
    str2 = str[-i:]+str[:-i]
    str3 = str2.replace(" ","")

    
    print(str3)
    
   
