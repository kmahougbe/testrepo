


Fin="Fin"
while True:
 f=1
 x = input("Number  ")
 if (x == Fin):
  print("Jespere que cela a ete utile")
  break
 try:
  num=int(x)
  if num == 0:
   f= 1
  if num != 0:
   for i in range (1,num+1) :
    f=f*i
  print("le factoriel est", f)
  continue
 except:
  print("Entrez un nombre entier")
  continue











#{x=1541 y=1222 print(x*y) x=1+33**96/8+55 print(x) x=9/2 x=float(x) print(x) print('Good morning we are gonna work with') number=input('Give a number and i divide it in three     ') x=number/3 print(x)
