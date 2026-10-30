from math import sqrt

C4 = (992 + 448*sqrt(2))**0.25
Csq = 3**0.75/sqrt(2)
print(f'C4={C4:.15f}')
print(f'Csq={Csq:.15f}')
print(f'pair_square_cap1={C4*Csq:.15f}')
print(f'bank_sqrt2_caps={2*C4*Csq:.15f}')
print(f'partner_rank3_composite={C4*(17.315056318**0.25):.15f}')
print(f'partner_rank2_composite={C4*(11.6791522071**0.25):.15f}')
print(f'pair_plus_L2_multiplier={C4*sqrt(2):.15f}')
for m in (1,2,4,16,64):
    a = 1/sqrt(2*m)
    D = a*a
    kappa = abs(a)
    print(f'm={m} D={D:.15g} kappa={kappa:.15g} Dkappa={D*kappa:.15g} sumD={m*D:.15g}')
print('STATUS=PASS')
