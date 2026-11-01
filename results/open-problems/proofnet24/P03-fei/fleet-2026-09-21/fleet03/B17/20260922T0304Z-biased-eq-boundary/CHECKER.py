#!/usr/bin/env python3
import itertools, math


def phi(x):
    return 0.0 if x <= 0.0 else x * math.log2(1.0/x)


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)


def eq_formula(d,p):
    q=1-p
    r=p**d+q**d
    masses=[(1-2*r)**2]
    for s in range(1,d+1):
        a=p**(d-s/2)*q**(s/2)+((-1)**s)*q**(d-s/2)*p**(s/2)
        masses += [4*a*a]*math.comb(d,s)
    H=sum(phi(w) for w in masses)
    I=d*4*p*q*(p**(d-1)+q**(d-1))
    W=I/4-r*(1-r)
    return r,masses,H,I,W


def eq_direct(d,p):
    q=1-p
    xs=list(itertools.product((0,1),repeat=d))
    probs=[]; vals=[]; basis=[]
    for x in xs:
        probs.append(math.prod(p if z else q for z in x))
        vals.append(-1 if (all(z==0 for z in x) or all(z==1 for z in x)) else 1)
        basis.append([(z-p)/math.sqrt(p*q) for z in x])
    coeff=[]
    for mask in range(1<<d):
        c=0.0
        for j,x in enumerate(xs):
            b=1.0
            for i in range(d):
                if (mask>>i)&1:
                    b*=basis[j][i]
            c+=probs[j]*vals[j]*b
        coeff.append(c)
    masses=[c*c for c in coeff]
    H=sum(phi(w) for w in masses)
    I=sum(mask.bit_count()*masses[mask] for mask in range(1<<d))
    r=p**d+q**d
    W=I/4-r*(1-r)
    return r,masses,H,I,W


def gamma_synthetic(p,A=2.3,B=0.7):
    s=min(p,1-p)
    return 0.0 if s==0.0 else A*s*math.log2(1/s)+B*s


def eq_D(d,p,gamma=gamma_synthetic):
    q=1-p
    r,m,H,I,W=eq_formula(d,p)
    D=d*(p**(d-1)+q**(d-1))*(gamma(p)+h2(4*p*q))-H-gamma(r)
    return D,W


def main():
    max_mass=max_H=max_I=max_W=0.0
    cases=0
    for d in range(3,8):
        for p in (1e-4,0.01,0.13,0.33,0.5):
            a=eq_formula(d,p); b=eq_direct(d,p)
            ma=sorted(a[1]); mb=sorted(b[1])
            max_mass=max(max_mass,max(abs(x-y) for x,y in zip(ma,mb)))
            max_H=max(max_H,abs(a[2]-b[2]))
            max_I=max(max_I,abs(a[3]-b[3]))
            max_W=max(max_W,abs(a[4]-b[4]))
            cases+=1
    assert max_mass < 1e-12 and max_H < 1e-12 and max_I < 1e-12 and max_W < 1e-12

    d3_err=0.0
    for p in (1e-6,1e-4,0.01,0.17,0.33,0.5):
        d3_err=max(d3_err,abs(eq_formula(3,p)[4]-3*(p*(1-p))**2))
    assert d3_err < 1e-12

    A=2.3
    tail=[]
    for d in (3,4,5,8):
        target=-2*A*math.log2(d)/(d-1)
        p=1e-5
        D,W=eq_D(d,p)
        observed=p*(-D/W)
        tail.append((d,target,observed,abs(target-observed)))
        assert abs(target-observed) < 5e-4

    print('PASS')
    print('direct_cases=',cases)
    print('max_spectral_mass_error=%.3e'%max_mass)
    print('max_entropy_error=%.3e'%max_H)
    print('max_influence_error=%.3e'%max_I)
    print('max_currency_error=%.3e'%max_W)
    print('max_EQ3_W_identity_error=%.3e'%d3_err)
    for d,target,observed,err in tail:
        print('tail d=%d target_p_c=%.12f observed_p_c=%.12f error=%.3e'%(d,target,observed,err))

if __name__=='__main__':
    main()
