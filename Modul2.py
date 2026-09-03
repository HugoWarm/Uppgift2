#+, -, *, /, **, //
print(1+1)
print(3-1)
print(2*1)
print(2/1)
print(2**1)
print(4.5//2)
print(5%2)
#** är att höja upp talet
#// är heltasdivition
#% är modulo
förnamn= input("Vad är ditt förnamn?")
efternamn= input("Vad är ditt efternamn?")
age= input("Hur gammal är du?")

print("Du heter "+ förnamn +" "+ efternamn + " och du är "+ age + " år gammal")
print("Skriv 2 nummer du vill multipliceras?")
num1= int(input("Första nummret"))
num2= int(input("Andra nummret"))
print(num1*num2)
print("Skriv in din vikt i kg och längd i meter så kan vi räkna ut ditt bmi.")
längd= float(input("Din längd i meter"))
vikt= int(input("Din vikt i kg"))
answer= vikt/längd**2
print(f"{answer:.2f}")
age2=int(input("Hur gammal är du?"))
print("Du har levt i",age2*52,"veckor")
weight=int(input("hur mycket väger du?"))
print("Det är",weight*2.20462,"lbs")