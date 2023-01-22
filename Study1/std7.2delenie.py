a=int(input('summa: '))
b=1
c=5
d=10
e=20
f=100
af=a//f #100
fe=(a-f*af)//e #20
fd=((a-f*af)-e*fe)//d #10
dc=((a-f*af)-e*fe-d*fd)//c #5
cb=(a-f*af-e*fe-d*fd-c*dc)//b #1
print('Всего банкнот: ',af+fe+fd+dc+cb)
print('Соток: ',af)
print('Двадцаток: ',fe)
print('Десяток: ',fd)
print('Пятерок: ',dc,)
print('По одному: ',cb)