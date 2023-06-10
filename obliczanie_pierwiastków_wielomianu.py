import re
import numpy as np

test_input = '2*x**3 + 2*x**2 + 1*x + 15'
test_input2 = '-12*x**4 - 72*x**3 + 4*x**2 + 21*x + 15'
test_inpur3 = '1*x**2 + 1*x + 2'
test_input4 = '1*x**2 + 4*x + 4'
test_input5 = '1*x**2 + 4'
# log(x)+x**2-3*x+2-10/x
def return_poly(input):
    potegi_n = re.findall(r"(^[0-9]{1,5}\*x\**[0-9]|^[+-]*[0-9]{1,5}\*x\**[0-9]|[+-]\s[0-9]{1,5}\*x\**[0-9])", input)
    #potegi_n_bez_wsp = re.findall(r"[+-]\sx\*\*[0-9]", input)
    potega1 = re.findall(r"[+-]\s[0-9]{1,5}\*x\s|[+-]\sx\s",input)                                
    liczba = re.findall(r"[+-]\s[0-9]{1,5}$",input) 
    # for i in range(0,len(potegi_n_bez_wsp)):
    #     potegi_n_bez_wsp[i] = ''.join(potegi_n_bez_wsp[i].split())
    for i in range(0,len(potegi_n)):
        potegi_n[i] = ''.join(potegi_n[i].split())
    if liczba:
        liczba[0] = "".join(liczba[0].split())
    if potega1:
        potega1[0] = "".join(potega1[0].split())
   # print(potegi_n)
    #print(potegi_n_bez_wsp)
   # print(potega1)
   # print(liczba)
   
    if potegi_n:
        max_pot = potegi_n[0][-1]
    elif potega1:
        max_pot = 1
    else:
        return "brak miejsca zerowego"
    

    coeff = [0 for _ in range(int(max_pot)+1)]

    if potegi_n:
        for el in potegi_n:
            #print(int(el[-1]))
            coeff[int(el[-1])] = int(el[0:-5])

    if potega1:
            coeff[1] = int(potega1[0][0:-2])
    if liczba:
            coeff[0] = int(liczba[0])

    coeff.reverse()
    #print(coeff)
    root = np.roots(coeff)
    res = ""
    for id, x in enumerate(root):
        res += "x" + str(id+1)+ ": " + str(round(x,2))+ " \n "
         
    return res

#print(return_poly(test_input))

