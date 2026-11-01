#!/usr/bin/env python3
"""Exact polynomial checks; rational logarithm certificates; tagged exploration.

No FEI theorem is asserted. Python standard library only.
"""
from fractions import Fraction as F
from math import comb, log2
from functools import lru_cache
import json, hashlib, pathlib

def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
        h*=2
    return a

@lru_cache(None)
def ln_interval(x):
    assert x>0
    if x<1:
        lo,hi=ln_interval(1/x);return -hi,-lo
    power=x.numerator.bit_length()-x.denominator.bit_length()
    scale=F(2)**power
    if x<scale:power-=1;scale/=2
    y=x/scale
    assert 1<=y<2
    z=(y-1)/(y+1);z2=z*z;term=z;total=F(0)
    for j in range(48):
        total+=2*term/F(2*j+1);term*=z2
    err=2*term/(97*(1-z2))
    if power:
        l2,h2=ln_interval(F(2)) if x!=2 else (None,None)
        if x==2:
            # Special base: use the series directly at y=2, z=1/3.
            z=F(1,3);term=z;total=F(0)
            for j in range(48):total+=2*term/F(2*j+1);term/=9
            return total,total+2*term/(97*(1-F(1,9)))
        return total+power*l2,total+err+power*h2
    return total,total+err

def lg_interval(x):
    lo,hi=ln_interval(F(x));l2,h2=ln_interval(F(2))
    if lo>=0:return lo/h2,hi/l2
    return lo/l2,hi/h2

def entropy_interval(entries):
    lo=hi=F(0)
    for weight,count in entries:
        if not weight:continue
        a,b=lg_interval(1/weight);lo+=count*weight*a;hi+=count*weight*b
    return lo,hi

def encl(x):
    """Return endpoints outward as both binary floats and serialized decimal text."""
    from math import nextafter, inf
    lo=float(x[0]);hi=float(x[1])
    while F.from_float(lo)>x[0] or F(str(lo))>x[0]:lo=nextafter(lo,-inf)
    while F.from_float(hi)<x[1] or F(str(hi))<x[1]:hi=nextafter(hi,inf)
    assert F.from_float(lo)<=x[0]<=x[1]<=F.from_float(hi)
    assert F(str(lo))<=x[0]<=x[1]<=F(str(hi))
    return [lo,hi]

def test_enclosures():
    for x in (F(1,10),F(1,3),F(-1,3),F(0),F(1,2),F(7,11),F.from_float(0.1),F.from_float(-0.1)):
        lo,hi=encl((x,x))
        assert F.from_float(lo)<=x<=F.from_float(hi)
        assert F(str(lo))<=x<=F(str(hi))
    # A binary endpoint can be outward while its JSON decimal spelling is not.
    for v in (0.1630852002095617,0.1,-0.3333333333333333):
        x=(F.from_float(v)+F(str(v)))/2
        lo,hi=encl((x,x))
        assert F.from_float(lo)<=x<=F.from_float(hi)
        assert F(str(lo))<=x<=F(str(hi))


def histogram(vals):
    from collections import Counter
    W=fwht(vals);return W,dict(sorted(Counter(W).items()))

def H(vals):
    from collections import Counter
    N=len(vals);return entropy_interval([(F(w2,N*N),c) for w2,c in Counter(w*w for w in fwht(vals)).items()])

def influence_num(vals):
    N=len(vals);n=N.bit_length()-1
    return [sum(vals[x]!=vals[x^(1<<i)] for x in range(N)) for i in range(n)]

def main():
    test_enclosures()
    witness=json.loads(pathlib.Path('witness.json').read_text());n=witness['n'];N=1<<n
    f=[-1 if x in witness['negative_f'] else 1 for x in range(N)];g=[-1]+[1]*(N-1);h=[x*y for x,y in zip(f,g)]
    Wf,hf=histogram(f);Wg,hg=histogram(g);Wh,hh=histogram(h)
    assert hf=={-6:48,-2:60,26:16,30:4}
    assert hg=={-2:127,126:1}
    assert hh=={-8:48,-4:60,24:16,28:4}
    assert all(b==a-2 for a,b in zip(Wf,Wh))
    Hf,Hg,Hh=H(f),H(g),H(h)
    excess=(Hh[0]-Hf[1]-Hg[1],Hh[1]-Hf[0]-Hg[0])
    assert excess[0]>F(1630852002095,10**13)
    out={'status':'PASS','full_FEI':'OPEN','seven_bit':{'signed_histograms':[hf,hg,hh],'entropy_intervals':[encl(v) for v in (Hf,Hg,Hh)],'excess_interval':encl(excess),'rational_lower_bound':'1630852002095/10000000000000'}}
    clause=[]
    for m in range(2,9):
        n=2*m-1;M=1<<n;a_mask=(1<<m)-1;b_mask=1|(((1<<(m-1))-1)<<m)
        ff=[-1 if x&a_mask==0 else 1 for x in range(M)];gg=[-1 if x&b_mask==0 else 1 for x in range(M)];hh=[a*b for a,b in zip(ff,gg)]
        p=F(1,2**(m-1));coeff=[(1-2*p+2*p*p,1),(-2*p*(1-p),1),(-p*(1-2*p),4*(1/p-1)),(2*p*p,2*(1/p-1)**2)]
        predicted=entropy_interval([(x*x,c) for x,c in coeff])
        from collections import Counter
        actual=Counter(F(w,M) for w in fwht(hh));expected=Counter()
        for a,c in coeff:expected[a]+=int(c)
        # Explicit table also counts zero coefficients at the small endpoint.
        expected[0]+=M-sum(expected.values())
        assert actual==+expected
        direct=H(hh);base=H(ff)
        assert max(predicted[0],direct[0])<=min(predicted[1],direct[1])
        delta=(direct[0]-2*base[1],direct[1]-2*base[0])
        if m==6:assert delta[0]>F(239650700679,10**14)
        iff=F(sum(influence_num(ff)),M);igg=F(sum(influence_num(gg)),M);ih=F(sum(influence_num(hh)),M)
        assert iff==igg==m*p and ih==2*m*p-2*p*p
        clause.append({'m':m,'physical_n':n,'inputs_checked':M,'excess_interval':encl(delta),'actual_influence_deficit':str(iff+igg-ih),'excess_over_influence_deficit_interval':encl((delta[0]/(2*p*p),delta[1]/(2*p*p)))})
    out['shared_control_clause_checks']=clause
    # Average spectra and influence identities, with no floating decisions.
    sumW2=[0]*N;sumInf=[0]*7;sumHlo=sumHhi=F(0)
    for z in range(N):
        hz=[f[x]*g[x^z] for x in range(N)];W=fwht(hz)
        sumW2=[u+w*w for u,w in zip(sumW2,W)];infs=influence_num(hz);sumInf=[a+b for a,b in zip(sumInf,infs)]
        lo,hi=H(hz);sumHlo+=lo;sumHhi+=hi
    conv=[sum(Wf[s]**2*Wg[s^u]**2 for s in range(N)) for u in range(N)]
    assert all(sumW2[u]*N==conv[u] for u in range(N))
    If,Ig=influence_num(f),influence_num(g)
    assert all(sumInf[i]==N*(If[i]+Ig[i])-2*If[i]*Ig[i] for i in range(7))
    assert sumHhi/N<Hf[0]+Hg[0]
    out['averaged_ledger']={'translations_checked':N,'squared_spectrum_identities':N,'coordinate_influence_identities':7,'mean_entropy_interval':encl((sumHlo/N,sumHhi/N)),'input_entropy_sum_interval':encl((Hf[0]+Hg[0],Hf[1]+Hg[1]))}
    out['script_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    pathlib.Path('verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
