print "Hello Word"

name = raw_input("Enter Name:")
print "Hola", name

hrs = raw_input("Enter Hours:")
hors=float(hrs)
rate = raw_input("Enter Rate:")
rate1=float(rate)
total=hors*rate1
print type(hors),  type(rate1), type (total)
print  total


Cs=raw_input("score: ")
Cs=float(Cs)
if Cs> 1.0: 
    print "Bad Input, try again"
elif Cs < 0:
    print "Bad Input, try again"
elif Cs < 0.6:
    print "F"
elif Cs >= 0.6 and Cs < 0.7:
    print "E"
elif Cs >= 0.7 and Cs < 0.8:
    print "D"
elif Cs >= 0.8 and Cs < 0.9:
    print "B"
elif Cs >= 0.9 and Cs <1:
    print "A"


def computepay(h, r) :
    if h > 40:
        ex=h-40
        total=40.0*r+ex*1.5*r
	return total
    else :
        total=h*r
        return total
#  Fin de la función ahora viene el código que normalmente se ejecuta
inp = raw_input("Enter Hours:")
ho=float(inp)
inp = raw_input("Enter Rate:")
ra=float(inp)
pago = computepay(ho,ra)  # Llamado a la función
print "Pay:",pago
