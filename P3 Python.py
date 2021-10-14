a = int(input ("premier coté" ))
b = int(input ("second coté "))
c = int(input ("troisième coté "))
if a==b and a==c and b==c:
    print("c'est un triangle équilatéral")
elif a==b or a==c or b==c:
    print("c'est un triangle issocèle")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("c'est un triangle rectangle")

