# Reactions
R1:
    A > B
    k1*A

R2:
    B + cof > C + byp2
    k2*B

R3:
    B + cof > D + byp2
    k3*B

R4:
    D > E + cof
    k4*D

R5:
    C + cof > D + {2.0} byp
    k5*C

R6:
    C > E + {2.0} byp
    k6*C

R7:
    E > A
    k7*E

#InitPar
k1 = 1.0
k2 = 1.0
k3 = 1.0
k4 = 1.0
k5 = 1.0
k6 = 1.0
k7 = 1.0

#InitVar
A = 1000
B = 1000
C = 1000
D = 1000
E = 1000
cof = 10000
byp = 0
byp2 = 0
