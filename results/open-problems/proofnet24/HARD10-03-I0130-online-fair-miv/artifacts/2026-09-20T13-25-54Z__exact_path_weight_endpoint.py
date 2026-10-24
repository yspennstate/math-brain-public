from fractions import Fraction as F
S=F(202391574968484000000000)
Q=F(4870886400)
P1=F(21454951)
G=F(2320006002124622963165232172483642250245228391,105941779200)
b0=F(462779651166897045103043986972930783,463474350810274668871680000000000000)
b1=F(57956185151311377325530313,58148415346982400000000000)
Mcont=F(799781,960)
M=Mcont+b0+b1
C=F(230400)+F(76800)*M
eta=G/(S*C)
U=F(9,10)-(P1+eta)/Q
W=U-F(19,30)
Uold=F(4716592387968856810867208985600000000000,5266434552595050168709499855395532216213)
assert U<Uold
assert M < F(1028)+b0+b1
print('I0130_EXACT_PATH_WEIGHT_ENDPOINT_PASS')
for k,v in [('Mcont',Mcont),('Mstar',M),('Cexact',C),('eta',eta),('U_MIV',U),('W_MIV',W),('improvement',Uold-U)]:
 print(f'{k}={v.numerator}/{v.denominator}')
print('Mstar_decimal=%.18f'%float(M))
print('eta_decimal=%.18f'%float(eta))
print('U_decimal=%.18f'%float(U))
print('improvement_decimal=%.18e'%float(Uold-U))
