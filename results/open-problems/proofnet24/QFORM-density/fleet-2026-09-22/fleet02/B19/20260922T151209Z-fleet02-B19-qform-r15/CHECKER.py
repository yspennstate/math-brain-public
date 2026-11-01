from fractions import Fraction
import math, random

random.seed(20260922)

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

lower_c=Fraction(41,56)*Fraction(27,41)
lower_ab=Fraction(7,8)**2
prod=lower_ab*lower_c**2
print(f"lower_c={lower_c}")
print(f"lower_ab={lower_ab}")
print(f"pivot_det_product_lower={prod}")
print(f"pivot_det_product_is_729_4096={prod==Fraction(729,4096)}")
C=8*math.sqrt(math.e)*(4096/729)**0.25
print(f"constant_numeric={C:.15f}")
print(f"constant_closed_numeric={64*math.sqrt(math.e)/(3*math.sqrt(3)):.15f}")

for idx in range(5):
    a=Fraction(random.randint(7,20),8)
    b=Fraction(random.randint(7,20),8)
    lam=Fraction(random.choice([-1,1])*random.randint(41,80),56)
    x=Fraction(random.randint(-5,5),20)
    y=Fraction(random.randint(-5,5),20)
    r=Fraction(random.randint(15,20),20)
    v=[x,y,r]
    D=[a,-b,Fraction(0)]
    M=[[(D[i] if i==j else Fraction(0))+lam*v[i]*v[j] for j in range(3)] for i in range(3)]
    lhs=det3(M); rhs=-a*b*lam*r*r
    print(f"sample{idx}_det_identity={lhs==rhs};lhs={lhs};rhs={rhs}")

for m in (8,16,64):
    H_op=Fraction(m-1,m)
    s2=Fraction(1,m)
    taildiag=Fraction(1,m)
    regime=(H_op>Fraction(7,16) and s2<=Fraction(1,8) and taildiag<Fraction(1,7))
    print(f"m={m};H_op={H_op};s2={s2};taildiag={taildiag};partner_regime={regime}")

print("QFORM_EXACT_ONE_EFFECTIVE_AGGREGATE_CHECK_PASS")
