from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time,sys
from arithmetic import fwht,log2,scale,plus,Q,phi_ratio
ROOT=Path(__file__).resolve().parents[1]
H=[-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64)]
CO=fwht(H);checks=0
def ck(b):
    global checks
    assert b;checks+=1
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for k,v in enumerate(a):c[k]+=v
    for k,v in enumerate(b):c[k]+=v
    while len(c)>1 and not c[-1]:c.pop()
    return c
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    return c
def powp(a,k):
    c=[F(1)]
    for _ in range(k):c=mul(c,a)
    return c
def ev(a,p):
    z=F(0)
    for x in reversed(a):z=z*p+x
    return z
def diff(a):return [k*a[k] for k in range(1,len(a))]
def signed(iv,r):
    if r>=0:return scale(iv,r)
    lo,hi=scale(iv,-r);return -hi,-lo
def entropy(masses):
    iv=(0,0)
    for p in masses:
        if p:iv=plus(iv,scale(log2(1/p),p))
    return iv
def spectrum(p):
    m=1-2*p;v=1-m*m;mass=[]
    for T in range(64):
        c=sum(CO[U]*m**((U^T).bit_count()) for U in range(64) if U&T==T)
        mass.append(v**T.bit_count()*c*c)
    return mass
def symbolic():
    counts=[sum(H[x]==-1 for x in range(64) if x.bit_count()==k) for k in range(7)]
    ck(counts==[1,6,3,0,0,0,0])
    alpha=[F(0)]
    for k,c in enumerate(counts):alpha=add(alpha,[c*x for x in mul(powp([0,1],k),powp([1,-1],6-k))])
    tau=add([1],[-x for x in alpha]);ck(tau==list(map(F,[0,0,12,-28,27,-12,2])))
    q=list(map(F,[0,4,-14,18,-10,2]));qp=diff(q)
    ck(diff(tau)==[6*x for x in q])
    ck(qp==[2*x for x in mul(powp([1,-1],2),[2,-10,5])])
    for j in range(6):
        pivotal=[0]*6
        for x in range(64):
            if x>>j&1:continue
            if H[x]!=H[x|1<<j]:pivotal[x.bit_count()]+=1
        pp=[F(0)]
        for k,c in enumerate(pivotal):pp=add(pp,[c*x for x in mul(powp([0,1],k),powp([1,-1],5-k))])
        ck(pp==q)
    delta=F(1,16);cut=F(7,32);rho=F(19,16)
    ck(ev([2,-10,5],cut)==F(53,1024)>0)
    ck(6*ev(q,delta)>rho)
    ck((1-cut)**2*(2-cut)>1)
    ck(12*cut**3*(1-cut*cut)>F(1,9))
    ck(3-5*F(1,2)**2>0)
    ck(162<256)
    ck(ev(tau,cut)<F(3,8))
    b=[0,0,0,0,3,0,-2]
    ck(ev(b,F(1,2))==F(5,32)<cut)
    ck(ev(b,F(3,8))==F(7047,131072)<delta)
    ck(ev(tau,delta)<delta and ev(tau,cut)>cut)
    fixed=[-1,12,-28,27,-12,2]
    for r in [F(1),F(-1),F(1,2),F(-1,2)]:ck(not delta<=r<=cut)
    lo,hi=delta,cut
    for _ in range(32):
        md=(lo+hi)/2
        if ev(fixed,md)<0:lo=md
        else:hi=md
    ck(ev(fixed,lo)<0<ev(fixed,hi))
    # Constant coefficients in the one-use reciprocal-influence potential.
    ck(F(38,3)*(1-1/rho)==2)
    ck(F(19,3)*(1-1/rho)==1)
    ck(F(76,3)+32==F(172,3)<58)
    ck(F(-38,3)-4==F(-50,3))
    return {'counts':counts,'alpha_coeff':[str(x) for x in alpha],'tau_coeff':[str(x) for x in tau],'q_coeff':[str(x) for x in q],'fixed_point_bracket':[str(lo),str(hi)],'minority_expansion_floor':str(rho),'ordinary_positive_potential':'38/3','ordinary_negative_potential':'19/3','moderate_bill_bounds':['-50/3','172/3'],'checks':checks},lo,hi
def pilot():
    start=time.perf_counter();sym,lo,hi=symbolic();rows=[]
    for p in [F(1,16),F(7,32),F(1,2),F(25,32),F(27,32),lo,hi]:
        masses=spectrum(p);v=4*p*(1-p);q=2*p*(1-p)**3*(2-p);QQ=6*q
        ck(sum(masses)==1)
        ck(sum(t.bit_count()*mass for t,mass in enumerate(masses))==v*QQ)
        for j in range(6):ck(sum(mass for t,mass in enumerate(masses) if t>>j&1)==v*q)
        E=entropy(masses);hv=entropy([v,1-v]);C=plus(E,signed(hv,-QQ));Cratio=signed(C,1/QQ)
        ck(Cratio[0]>=-Q)
        if p<=F(7,32):ck(Cratio[1]<=2*Q)
        else:ck(Cratio[1]<=8*Q)
        rows.append({'p':str(p),'Q':str(QQ),'spectrum':[str(x) for x in masses],'entropy_interval':E,'C_interval':C,'C_over_Q_interval':Cratio})
        (ROOT/'out/BIAS_CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n')
    out={'helper_version':'moderate-prefix-payment-v1','symbolic':sym,'assertions_passed':checks,'failed':0,'runtime_seconds':time.perf_counter()-start}
    ck(out['runtime_seconds']<55)
    (ROOT/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='symbolic'}))
def physical():
    start=time.perf_counter();rows=[]
    for mask in range(1,15):
        g=[-1 if mask>>x&1 else 1 for x in range(4)]
        neg=sum(x==-1 for x in g)
        if neg>2:g=[-x for x in g];neg=4-neg
        p=F(neg,4)
        if p>F(7,32):g=[-x for x in g];p=1-p
        core=fwht(g);v=1-core[0]**2
        truth=[]
        for x in range(4096):
            index=sum((g[(x>>(2*j))&3]==-1)<<j for j in range(6))
            truth.append(H[index])
        coeff=fwht(truth);masses=spectrum(p);q=2*p*(1-p)**3*(2-p);QQ=6*q
        for S,c in enumerate(coeff):
            T=0;term=F(1)
            for j in range(6):
                U=(S>>(2*j))&3
                if U:T|=1<<j;term*=core[U]**2/v
            ck(c*c==masses[T]*term)
        ck(sum(c*c for c in coeff)==1)
        di=[F(sum(g[x]!=g[x^(1<<i)] for x in range(4)),4) for i in range(2)]
        parent=[]
        for i in range(12):
            e=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(4096)),4096)
            ck(e==q*di[i%2]);parent.append(e)
        ck(sum(parent)==QQ*sum(di))
        Hg=entropy([c*c for c in core]);HF=entropy([c*c for c in coeff]);Hp=entropy(masses);hv=entropy([v,1-v])
        right=plus(scale(Hg,QQ),plus(Hp,signed(hv,-QQ)))
        ck(HF[0]<=right[1] and right[0]<=HF[1])
        rows.append({'mask':mask,'oriented_bias':str(p),'I_core':str(sum(di)),'I_parent':str(sum(parent)),'entropy_identity_intervals':[HF,right]})
        (ROOT/'out/PHYSICAL_CASES.json').write_text(json.dumps(rows,indent=2)+'\n')
        ck(time.perf_counter()-start<55)
    out={'version':'moderate-prefix-payment-v1','cases':14,'physical_dimension':12,'assertions_passed':checks,'failed':0,'runtime_seconds':time.perf_counter()-start}
    (ROOT/'out/PHYSICAL.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':pilot() if '--pilot' in sys.argv else physical()
