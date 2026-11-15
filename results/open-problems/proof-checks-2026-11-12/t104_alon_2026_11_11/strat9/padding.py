"""PROVED: lower-bound coefficients for extending moment cells to N>=6."""
from fractions import Fraction as F
from cells import base_value,lower_value,controls,minimum,vector_from_record,check

def base_coefficients(p,a,r):
    A,B,C=p;s=a*(1+r);lam=(2+s)/4;fm=A+r*B+(1+r)*C
    K=a*a*(A+r*r*B+2*r*C-(1+r*r)/5)
    Fm=a*fm;hd=F(4,5)-2*s/5+Fm
    T5=(14+2*s)*(Fm-s/5)/9+F(4,3)*a*a*(1+r*r)-F(14,3)*a*a*(A+r*r*B)-4*a*a*(1+r*r+r/3)*C
    X35=(1-lam)*(10*Fm-2*s)/9
    core=T5-X35-F(4,3)*K
    return (16*base_value(p,a,r),8*core+4*K+(1-lam)*(14*lam-4+2*hd),core+(1-lam)*2*lam)

def lower_coefficients(p,a,r,vector):
    extra=lower_value(p,a,r,vector)-base_value(p,a,r)
    return tuple(b+c*extra for b,c in zip(base_coefficients(p,a,r),(16,8,1)))

def check_allN(rec,verts):
    check(rec,verts)
    vec=vector_from_record(rec)
    lo,hi,alo,ahi=map(F,(rec['rlo'],rec['rhi'],rec['alo'],rec['ahi']))
    margins=[]
    for k in range(3):
        m=min(minimum(lambda rr:controls(lambda aa:lower_coefficients(p,aa,rr,vec)[k],alo,ahi)[j],lo,hi)for p in verts for j in range(3))
        assert m>=0
        margins.append(m)
    return margins
