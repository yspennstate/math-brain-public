from itertools import product
from fractions import Fraction
from collections import Counter

# Eisenstein integers u+v*w with w^2+w+1=0.
PHI = ((1,0),(0,1),(-1,-1))

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def scale(c,a): return (c*a[0], c*a[1])
def norm2(a):
    u,v=a
    return u*u-u*v+v*v

def amp(signs):
    z=(0,0)
    for e,p in zip(signs,PHI): z=add(z,scale(e,p))
    return z

def sorted_sv2(a2,b2):
    # Here a2,b2 are 0 or 4, hence |a|,|b| are 0 or 2.
    aa = 0 if a2==0 else 2
    bb = 0 if b2==0 else 2
    s1=(aa+bb)**2
    s2=(abs(aa-bb))**2
    return tuple(sorted((s1,s2), reverse=True))

cnt=Counter()
full_even=full_odd=0
sum_T=sum_T2=sum_S2=0
N=0
for signs in product((-1,1), repeat=6):
    ae=amp(signs[:3]); ao=amp(signs[3:])
    ae2=norm2(ae); ao2=norm2(ao)
    assert ae2 in (0,4) and ao2 in (0,4)
    cnt[sorted_sv2(ae2,ao2)] += 1

    # Complement indicator n_g=(1-e_g)/2 gives amplitude exactly -a/2.
    ce=amp(tuple((1-e)//2 for e in signs[:3]))
    co=amp(tuple((1-e)//2 for e in signs[3:]))
    assert scale(2,ce)==scale(-1,ae)
    assert scale(2,co)==scale(-1,ao)

    even_full = all(e==-1 for e in signs[:3])
    odd_full = all(e==-1 for e in signs[3:])
    full_even += even_full
    full_odd += odd_full

    # Equality rule at mu=6: total scalar mass 24 on each available full triangle.
    rp=24 if even_full else 0
    rm=24 if odd_full else 0
    T=rp+rm; S=rp-rm
    sum_T += T; sum_T2 += T*T; sum_S2 += S*S
    N += 1

assert N==64
assert cnt == Counter({(0,0):4,(4,4):24,(16,0):36})
assert full_even==8 and full_odd==8
ET=Fraction(sum_T,N); ET2=Fraction(sum_T2,N); ES2=Fraction(sum_S2,N)
assert ET==6 and ET2==162 and ET2-ET*ET==126 and ES2==126
assert ET2+ES2==288

# Exact weighted-triangle minima: ||sum w_i rho(g_i)||_F^2 = 3 sum w_i^2 - m^2.
# Equal weights on k available positions minimize sum w_i^2 at fixed mass m.
coeff={k: Fraction(3,k)-1 for k in (1,2,3)}
assert coeff=={1:Fraction(2),2:Fraction(1,2),3:Fraction(0)}

print('P26-P04-CLAIM44-EISENSTEIN-EXACT-AUDIT: PASS')
print('SIGNED_SV2_COUNTS', sorted(cnt.items()))
print('SUPPORT_PARETO_COEFFS', [(k,str(coeff[k])) for k in (1,2,3)])
print('FULL_EVEN_MASKS', full_even)
print('FULL_ODD_MASKS', full_odd)
print('UNIFORM_RULE_E_T', ET)
print('UNIFORM_RULE_E_T2', ET2)
print('UNIFORM_RULE_VAR_T', ET2-ET*ET)
print('UNIFORM_RULE_E_S2', ES2)
print('UNIFORM_RULE_ENERGY', ET2+ES2)
print('P26-P04-CLAIM44-EISENSTEIN-EXACT-AUDIT: PASS_END')
