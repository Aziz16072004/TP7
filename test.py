#declaration
from pickle import *
e = dict(NP = str , CIN = str , NT = str)
def remplirf():
    global f
    f= open('client.dat','ab')
    e['NP'] = str(input("nom et prenom ="))
    while not (verif(e['NP'])):
        e['NP'] = str(input("nom et prenom ="))
    
    e['CIN'] = str(input("CIN ="))
    while not (e['CIN'].isdecimal() and len(e['CIN']) == 8):
        e['CIN'] = str(input("CIN ="))
        
    e['NT'] = str(input("numero telephone ="))
    while not (e['NT'].isdecimal or e['NT'][0]=="2" or e['NT'][0]=="4" or e['NT'][0]=="6" or e['NT'][0]=="8"):
        e['NT'] = str(input("numero telephone  ="))
    dump(e,f)
    f.close()
def verif(ch):
    i = 0
    res = True
    while res and i<len(ch):
        res = "A"<=ch[i].upper()<="Z" or ch[i]==" "
        i +=1
    return res

def chance(ch):
    nc = 0
    #calcule nombre de chance
    for i in range (len(ch)):
        nc = nc + (int(ch[i])*i)
        
    #verifier si nc premier ou non  
    res = premier(nc)
    return res
def premier(x):
    i = 2
    res = True
    while res and i<=x//2:
        res = x%i != 0
        i+=1
    return res
def afficher(f):
    f= open('client.dat','rb')
    finfichier = False
    while not finfichier :
        try :
            e = load(f)
            if chance(e["NT"]):
                print(e['CIN'],':"Felicitation , vous avez gagne"')
            else:
                print(e['CIN'],':"desole , vous navez pas gagne"')
        except :
            finfichier = True
    f.close()
#pp
remplirf()
afficher(f)