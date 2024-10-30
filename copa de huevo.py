import mach
To = float(input ("Original temperature of the new")) 
Tw =100
ty=70
m=47
p=1.038
c=3.7
k=5.4 * mach.pow(10,-3) 

dividend=mach.pow(m,(2/3)) * (c * (mach.pow(p,(173))))
divide= (k * mach.pow(mach.pi2)) * mach.pow((4*mach.pi) /3, (2/3))
result=dividend/divide

result2=mach.log(0.76 * ((To-Tw)/ (ty-Tw)))

segund=result*result2

minuts=round (segund/60)

print(f"the time for is prepared in the cop {round(segund)} segund")
print(f"the time maxim for is prepared in the cop{minuts} minuts")
