import math

K0=(15/4)*6**(2/5)
F0=12*2**(-1/3)
print(f"PARTNER_CONSTANT={K0:.15f}")
print(f"THEOREM_F_CONSTANT={F0:.15f}")
for m in [3,4,8,16,64,256,1024]:
    eig=(1+1/m,-2+1/m,1+1/m)
    maxdiag=2/m
    maxpair=4/m**2
    delta2=8*(m-2)*(m-1)/m**4
    d=1/m
    currency=delta2*d
    pbound=K0*currency**(-1/5)
    global_currency_upper=252/m**3
    assert abs(eig[0])>=1 and abs(eig[1])>=1 and abs(eig[2])>=1
    assert currency <= global_currency_upper+1e-15
    print(f"m={m:4d} eig={eig[0]:.9f},{eig[1]:.9f},{eig[2]:.9f} "
          f"maxdiag={maxdiag:.9g} maxpair={maxpair:.9g} "
          f"packet_Delta2={delta2:.12g} d={d:.12g} currency={currency:.12g} "
          f"partner_bound={pbound:.9f}")
print("STATUS=PASS")
