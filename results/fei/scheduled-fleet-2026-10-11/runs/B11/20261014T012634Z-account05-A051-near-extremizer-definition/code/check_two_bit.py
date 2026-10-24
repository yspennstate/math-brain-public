from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import time,json,hashlib
import exact_tools as d
ROOT=Path(__file__).resolve().parent.parent
count=0
def ck(x):
    global count
    assert x
    count+=1
def logs(x):
    x=F(x);return d.add([(1,d.factor(x.numerator)),(-1,d.factor(x.denominator))])
def H(p):return d.add((-v,logs(v)) for v in p if v)
def nonneg(v):ck(not v or d.interval(v)[0]>=0)
def psi(s):
    s=min(F(1),s)
    return {2:F(2)} if s>=F(3,4) else d.add([(1,H([1-s,s])),(s,{3:F(1)})])
def embed(v,inds):return sum(((v>>j)&1)<<i for j,i in enumerate(inds))
def eval_case(t,mask,retain=False):
    n=(len(t)-1).bit_length();A=[i for i in range(n) if mask>>i&1];C=[i for i in range(n) if not mask>>i&1]
    coeff=[F(v,len(t)) for v in d.fwht([2*z-1 for z in t])]
    rp=[v*v for v in coeff];rootH=H(rp);rootI=sum(s.bit_count()*v for s,v in enumerate(rp))
    IA=sum(sum((s>>i)&1 for i in A)*v for s,v in enumerate(rp))
    wp=[];childH=[];childI=[]
    for a in range(4):
        child=[t[embed(a,A)|embed(c,C)] for c in range(1<<len(C))]
        w=[F(v,len(child)) for v in d.fwht([2*z-1 for z in child])];wp.append(w)
        p=[z*z for z in w];ck(sum(p)==1);childH.append(H(p));childI.append(sum(s.bit_count()*z for s,z in enumerate(p)))
    ck(rootI==IA+sum(childI)/4)
    q=[sum(w[s]**2 for w in wp)/4 for s in range(len(wp[0]))]
    B={};Gamma={};Ctotal=F(0);W0=Wg=Wb=F(0);rows=[]
    for s,qs in enumerate(q):
        if not qs:continue
        w=[v[s] for v in wp];c=sum(v**4 for v in w)/4/qs**2-1;ck(0<=c<=3)
        h=[1 if v>=0 else -1 for v in w];wh=d.fwht(h);rho=[F(v*v,16) for v in wh]
        wu=d.fwht(w);nu=[v*v/(16*qs) for v in wu];ck(sum(nu)==1)
        hv=H(nu);iv=sum(u.bit_count()*p for u,p in enumerate(nu));iph=sum(u.bit_count()*p for u,p in enumerate(rho))
        tv=sum(abs(a-b) for a,b in zip(nu,rho))/2;ck(tv**2<=c);ck(abs(iph-iv)<=2*tv)
        constant=len(set(h))==1
        if constant:
            W0+=qs;cat='constant';e=1-nu[0];ck(e<=c);ck(iv>=e)
            nonneg(d.add([(1,psi(e)),(-1,hv)]))
        elif c<=F(1,16):
            Wg+=qs;cat='good_nonconstant';ck(iph>=1);ck(iv>=F(1,2))
        else:Wb+=qs;cat='bad_nonconstant';ck(iph>=1)
        for K in (4,8,16):
            defect=d.add([(1,hv),(-K*iv,{2:F(1)})])
            cap=logs(1+F(3,1<<K)) if constant else {2:F(2)-F(K,2)} if cat=='good_nonconstant' else {2:F(2)}
            nonneg(d.add([(1,cap),(-1,defect)]))
        B=d.add([(1,B),(qs,hv)]);Gamma=d.add([(1,Gamma),(qs,logs(1+c))]);Ctotal+=qs*c
        if retain:rows.append({'retained_mask':s,'q':str(qs),'c':str(c),'category':cat,'row_I':str(iv),'phase_I':str(iph),'TV':str(tv)})
    ck(W0+Wg+Wb==1);ck(Wb<=16*Ctotal)
    ck(B==d.add([(1,rootH),(-1,H(q))]))
    J=d.add([(1,H(q)),(-F(1,4),d.add((1,h) for h in childH))])
    nonneg(d.add([(1,Gamma),(-1,J)]))
    checks=[]
    for K in (4,8,16):
        D=d.add([(1,rootH),(-K*rootI,{2:F(1)})])
        S=d.add([(F(-1,4),h) for h in childH]+[(K*sum(childI)/4,{2:F(1)})])
        lhs=d.add([(1,D),(1,S),((F(K,2)-2)*Wg,{2:F(1)})])
        ck(d.add([(1,D),(1,S)])==d.add([(1,B),(1,J),(-K*IA,{2:F(1)})]))
        rhs=d.add([(1,Gamma),(W0,logs(1+F(3,1<<K))),(2*Wb,{2:F(1)})])
        gap=d.add([(1,rhs),(-1,lhs)]);nonneg(gap)
        pure=d.add([(1,Gamma),(1,psi(Ctotal)),(2*Wb,{2:F(1)})]);nonneg(d.add([(1,pure),(-1,lhs)]))
        relaxed=d.add([(1,logs(1+Ctotal)),(1,psi(Ctotal)),(32*Ctotal,{2:F(1)})]);nonneg(d.add([(1,relaxed),(-1,lhs)]))
        if retain:checks.append({'K':K,'D':d.enc(D),'S':d.enc(S),'lhs':d.enc(lhs),'rhs':d.enc(rhs),'bank_gap_interval':d.ei(d.interval(gap))})
    return {'mask':mask,'C_A':str(Ctotal),'W0':str(W0),'Wg':str(Wg),'Wb':str(Wb),'Gamma':d.enc(Gamma),'rows':rows,'checks':checks}
def main():
    start=time.perf_counter();tables=cuts=0
    for n in (1,2,3):
        for truth in range(1<<(1<<n)):
            t=tuple((truth>>x)&1 for x in range(1<<n));tables+=1
            for A in combinations(range(n),2):eval_case(t,sum(1<<i for i in A));cuts+=1
            if time.perf_counter()-start>55:raise TimeoutError('Frozen pilot cap')
    controls=[('NAND6',d.tables((((((),()),(),()),()),())))]
    for r in range(1,5):
        t=tuple(1 if (z>>2)==0 else 1-((z&1)*((z>>1)&1)) for z in range(1<<(r+2)))
        controls.append(('rare_bent_'+str(r),t))
    for name,t in controls:
        tables+=1;n=(len(t)-1).bit_length();output=[]
        for A in combinations(range(n),2):
            output.append(eval_case(t,sum(1<<i for i in A),True));cuts+=1
        (ROOT/'out'/('CONTROL_'+name+'.json')).write_text(json.dumps({'name':name,'truth_sha256':hashlib.sha256(bytes(t)).hexdigest(),'cuts':output},indent=2)+'\n',encoding='utf-8')
        if time.perf_counter()-start>55:raise TimeoutError('Frozen pilot cap')
    out={'tables':tables,'two_bit_cuts':cuts,'assertions':count,'elapsed_seconds':time.perf_counter()-start}
    (ROOT/'out/SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
