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


def hadamard(L):return [[1 if (i&j).bit_count()%2==0 else -1 for j in range(L)] for i in range(L)]

def mul(H,v):return [sum(a*b for a,b in zip(row,v)) for row in H]

def bits_signs(mask,n):return [-1 if mask>>i&1 else 1 for i in range(n)]

def calc(L,k,r):
    H=hadamard(L);n_control=r*L;n_data=k*L;n=n_control+n_data;N=1<<n
    norm2=L**(k+1);raw=[];rounded=[];onehot=0;layer_counts=[]
    for rest in range(1<<((k-1)*L)):
        w=[1]*L
        for layer in reversed(range(1,k)):
            x=bits_signs(rest>>((layer-1)*L),L);w=mul(H,[a*b for a,b in zip(x,w)])
        assert sum(a*a for a in w)==L**k
        flat=all(a*a==L**(k-1) for a in w);count=0
        for x0 in range(1<<L):
            x=bits_signs(x0,L);v=mul(H,[a*b for a,b in zip(x,w)])
            assert sum(a*a for a in v)==norm2
            if sum(a!=0 for a in v)==1:count+=1
        assert count==(2*L if flat else 0)
        onehot+=count;layer_counts.append(count)
    for data in range(1<<n_data):
        v=[1]*L
        for layer in reversed(range(k)):
            x=bits_signs(data>>(layer*L),L);v=mul(H,[a*b for a,b in zip(x,v)])
        assert sum(a*a for a in v)==norm2
        for controls in range(1<<n_control):
            ys=[-1 if ((controls>>(j*r))&((1<<r)-1)).bit_count()%2 else 1 for j in range(L)]
            z=sum(a*b for a,b in zip(v,ys));raw.append(z);rounded.append(1 if z>=0 else -1)
    assert len(raw)==N
    W=fwht(raw);support=[s for s,w in enumerate(W) if w]
    assert len(support)==L**(k+1)
    assert all(abs(W[s])==N and s.bit_count()==r+k for s in support)
    assert sum(z*z for z in raw)==N*norm2
    assert sum(z**4 for z in raw)<=3*N*norm2**2
    assert 3*max(z*z for z in raw)>=L*norm2
    infs=[F(sum(rounded[x]!=rounded[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    Ic=sum(infs[:n_control]);Id=sum(infs[n_control:]);lo,hi=ln_interval(F(4*L))
    assert 24*Ic*Ic*lo>=r*r*L
    from collections import Counter
    hist=Counter(w*w for w in fwht(rounded));ent=entropy_interval([(F(w2,N*N),c) for w2,c in hist.items()])
    return {'L':L,'k':k,'r':r,'physical_variables':n,'truth_table_inputs':N,'all_data_assignments':1<<n_data,'outer_conditional_contexts':len(layer_counts),'onehot_data_assignments':onehot,'unrounded_support':len(support),'unrounded_homogeneous_degree':r+k,'control_influence':str(Ic),'data_influence':str(Id),'rounded_entropy_interval':encl(ent),'analytic_control_lower_bound_squared_interval':encl((F(r*r*L,24)/hi,F(r*r*L,24)/lo))}

def main():
    test_enclosures()
    out={'status':'PASS','full_classical_FEI':'OPEN','scope':'Exact finite self-checks of the abstract last-layer theorem and multilayer application; not independent audit or formalization.'}
    configs=[(2,1,1),(2,2,1),(2,3,1),(2,4,1),(2,2,2),(4,1,1),(4,2,1),(4,3,1),(4,1,2),(8,1,1)]
    out['checks']=[calc(*args) for args in configs]
    out['script_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest();pathlib.Path('verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
