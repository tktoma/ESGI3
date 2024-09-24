a,upper,lower,dicoupp,dicolow = input(),0,0,{},{}
for caractere in a:
    if caractere.isupper():
        upper += 1
        dicoupp[upper]=caractere
    if caractere.islower():
        lower += 1
        dicolow[lower]=caractere
    if caractere == ('\'') or caractere ==('.'):
        a = a.replace(caractere,'')
print (upper,lower)
print (dicoupp, dicolow)
print (a)