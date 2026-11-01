#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache

TERMS = 26
C0 = F(16137, 2500)              # 6.4548
ASTAR = F(2682048, 10_000_000)   # 0.2682048

def fwht_int(a):
    a = list(map(int, a))
    h = 1
    n = len(a)
    while h < n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h *= 2
    return a

def bent_value(x,m):
    q=0
    for j in range(0,m,2):
        q ^= ((x>>j)&1) & ((x>>(j+1))&1)
    return 1 if q==0 else -1

def log_unit_interval(x):
    assert F(1) <= x <= F(2)
    if x == 1:
        return F(0),F(0)
    z=(x-1)/(x+1)
    z2=z*z
    power=z
    s=F(0)
    for k in range(TERMS):
        s += power/(2*k+1)
        power *= z2
    lo=2*s
    rem=2*power/((2*TERMS+1)*(1-z2))
    return lo, lo+rem

@lru_cache(maxsize=None)
def log2_interval(x):
    x=F(x)
    if x < 1:
        lo,hi=log2_interval(1/x)
        return -hi,-lo
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x < F(2)**e:
        e -= 1
    m=x/F(2)**e
    a,b=log_unit_interval(m)
    c,d=log_unit_interval(F(2))
    return F(e)+a/d, F(e)+b/c

def phi_interval(x):
    x=F(x)
    if x == 0:
        return F(0),F(0)
    lo,hi=log2_interval(1/x)
    return x*lo,x*hi

def h2_interval(x):
    x=F(x)
    a,b=phi_interval(x)
    c,d=phi_interval(1-x)
    return a+c,b+d

def dec(x,digits=18):
    return f"{float(x):.{digits}f}"

def closed_interval(m):
    assert m%2==0 and m>=4
    N=1<<m
    sq=1<<(m//2)
    rho=F(4,sq)
    delta=F(2,N)
    nplus=F(N,4)+F(sq,2)
    nminus=F(N,4)-F(sq,2)

    Tp=(1+(1-rho)**2)/F(2*N)
    Tm=(1+(1+rho)**2)/F(2*N)
    pp=(1-rho)**2/(1+(1-rho)**2)
    pm=(1+rho)**2/(1+(1+rho)**2)
    thp=rho*rho/(2*(1+(1-rho)**2))
    thm=rho*rho/(2*(1+(1+rho)**2))

    hp=h2_interval(pp); hm=h2_interval(pm)
    hb_lo=F(1,2)+nplus*Tp*hp[0]+nminus*Tm*hm[0]
    hb_hi=F(1,2)+nplus*Tp*hp[1]+nminus*Tm*hm[1]
    js_lo,js_hi=1-hb_hi,1-hb_lo

    htp=h2_interval(thp); htm=h2_interval(thm)
    hj_lo=nplus*Tp*htp[0]+nminus*Tm*htm[0]
    hj_hi=nplus*Tp*htp[1]+nminus*Tm*htm[1]

    W=delta/4
    c_lo=4*(js_lo+hj_lo)/delta-4*C0
    c_hi=4*(js_hi+hj_hi)/delta-4*C0
    defect_lo=delta*C0-js_hi-hj_hi+ASTAR*W
    defect_hi=delta*C0-js_lo-hj_lo+ASTAR*W
    return (delta,js_lo,js_hi,hj_lo,hj_hi,W,c_lo,c_hi,defect_lo,defect_hi)

def brute_m6():
    m=6; N=1<<m
    f0=[bent_value(x,m) for x in range(N)]
    u=0; v=3
    assert f0[u]==1 and f0[v]==-1
    f1=f0[:]
    f1[u]*=-1
    f1[v]*=-1
    assert sum(f0)==sum(f1)==8
    assert sum(a!=b for a,b in zip(f0,f1))==2

    A=fwht_int(f0)
    B=fwht_int(f1)
    assert set(A)=={-8,8}
    cats={}
    for s,(a,b) in enumerate(zip(A,B)):
        parity=((s&3).bit_count()&1)
        cats[(parity,a,b)]=cats.get((parity,a,b),0)+1
    expected={
        (0,8,8):16,
        (0,-8,-8):16,
        (1,8,4):20,
        (1,-8,-12):12,
    }
    assert cats==expected, (cats,expected)
    return cats

def main():
    cats=brute_m6()
    delta,jsl,jsh,hjl,hjh,W,cl,ch,dl,dh=closed_interval(6)
    assert cl > ASTAR
    assert dh < 0
    assert cl > F(6,1)
    print("PASS")
    print("m6_categories =", cats)
    print("delta =", delta, "W =", W)
    print("JS_interval =", dec(jsl), dec(jsh))
    print("H_J_given_S_interval =", dec(hjl), dec(hjh))
    print("c_loc_interval =", dec(cl,15), dec(ch,15))
    print("lifted_local_defect_interval =", dec(dl,15), dec(dh,15))
    print("a_star =", float(ASTAR))
    print("gap_c_lower_minus_astar =", dec(cl-ASTAR,15))
    for m in range(4,22,2):
        z=closed_interval(m)
        print("m",m,"delta",float(z[0]),"c_loc",dec(z[6],12),dec(z[7],12))
    print("full_FEI_status = OPEN")

if __name__=="__main__":
    main()
