#!/usr/bin/env python3
import itertools, math


def phi(x):
    return 0.0 if x <= 0.0 else x * math.log2(1.0/x)


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)


def eq_formula(ps):
    d=len(ps); qs=[1-p for p in ps]
    P=math.prod(ps); Q=math.prod(qs); r=P+Q
    masses=[]
    for mask in range(1<<d):
        if mask==0:
            a=1-2*r
        else:
            t1=P; t0=Q; s=0
            for i in range(d):
                if (mask>>i)&1:
                    s+=1
                    t1*=math.sqrt(qs[i]/ps[i])
                    t0*=math.sqrt(ps[i]/qs[i])
            a=-2*(t1+((-1)**s)*t0)
        masses.append(a*a)
    H=sum(phi(w) for w in masses)
    coeff=[]; It=[]
    for i in range(d):
        Pm=math.prod(ps[j] for j in range(d) if j!=i)
        Qm=math.prod(qs[j] for j in range(d) if j!=i)
        s=Pm+Qm
        coeff.append(s)
        It.append(4*ps[i]*qs[i]*s)
    I=sum(It)
    W=I/4-r*(1-r)
    Wclosed=P*sum(qs)+Q*sum(ps)-r*(1-r)
    return r,masses,H,I,W,Wclosed,coeff


def eq_direct(ps):
    d=len(ps); qs=[1-p for p in ps]
    xs=list(itertools.product((0,1),repeat=d))
    probs=[]; vals=[]; basis=[]
    for x in xs:
        probs.append(math.prod(ps[i] if x[i] else qs[i] for i in range(d)))
        vals.append(-1 if all(z==0 for z in x) or all(z==1 for z in x) else 1)
        basis.append([(x[i]-ps[i])/math.sqrt(ps[i]*qs[i]) for i in range(d)])
    coeff=[]
    for mask in range(1<<d):
        c=0.0
        for k in range(len(xs)):
            b=1.0
            for i in range(d):
                if (mask>>i)&1:
                    b*=basis[k][i]
            c+=probs[k]*vals[k]*b
        coeff.append(c)
    masses=[c*c for c in coeff]
    H=sum(phi(w) for w in masses)
    I=sum(mask.bit_count()*masses[mask] for mask in range(1<<d))
    r=math.prod(ps)+math.prod(qs)
    W=I/4-r*(1-r)
    return r,masses,H,I,W


def gamma_tail(x,A=4.9096,B=2.2292198):
    s=min(x,1-x)
    return A*s*math.log2(1/s)+B*s


def gate_D(ps,A=4.9096,B=2.2292198):
    r,m,H,I,W,W2,coef=eq_formula(ps)
    D=sum(coef[i]*(gamma_tail(ps[i],A,B)+h2(4*ps[i]*(1-ps[i]))) for i in range(len(ps))) - H - gamma_tail(r,A,B)
    return D,W


def main():
    tests=[
        [0.13,0.27,0.41],
        [0.07,0.19,0.31,0.43],
        [0.11,0.17,0.23,0.29,0.37],
        [0.03,0.09,0.21,0.33,0.39,0.47],
    ]
    em=eH=eI=eW=eWc=0.0
    for ps in tests:
        a=eq_formula(ps); b=eq_direct(ps)
        em=max(em,max(abs(x-y) for x,y in zip(sorted(a[1]),sorted(b[1]))))
        eH=max(eH,abs(a[2]-b[2])); eI=max(eI,abs(a[3]-b[3])); eW=max(eW,abs(a[4]-b[4])); eWc=max(eWc,abs(a[4]-a[5]))
    assert max(em,eH,eI,eW,eWc)<2e-12

    A=4.9096
    rays=[
      [1/3,1/3,1/3],
      [0.7,0.2,0.1],
      [0.49,0.49,0.01,0.01],
      [0.9,0.05,0.03,0.02],
      [0.55,0.25,0.10,0.06,0.04],
    ]
    tail=[]
    for w in rays:
        z=sum(w); w=[x/z for x in w]
        H=-sum(x*math.log2(x) for x in w)
        gini=1-sum(x*x for x in w)
        target_D=A*H
        target_tc=-2*A*H/gini
        t=1e-5
        D,W=gate_D([t*x for x in w],A)
        obs_D=D/t
        obs_tc=t*(-D/W)
        assert abs(obs_D-target_D)<4e-4
        assert abs(obs_tc-target_tc)<2e-3
        assert 2*H/gini >= 2/math.log(2)-1e-12
        tail.append((len(w),target_D,obs_D,target_tc,obs_tc,2*H/gini))

    print('PASS')
    print('direct_cases=',len(tests))
    print('max_mass_error=%.3e'%em)
    print('max_entropy_error=%.3e'%eH)
    print('max_influence_error=%.3e'%eI)
    print('max_currency_error=%.3e'%eW)
    print('max_currency_closed_form_error=%.3e'%eWc)
    for d,td,od,tc,oc,ratio in tail:
        print('ray d=%d target_D_over_t=%.12f observed=%.12f target_t_c=%.12f observed=%.12f shannon_gini_ratio=%.12f'%(d,td,od,tc,oc,ratio))

if __name__=='__main__':
    main()
