#!/usr/bin/env python3
"""Exact fixed-point interval certificate. No floating arithmetic in the verifier."""
from __future__ import annotations
import argparse, json, time, hashlib
from functools import lru_cache
from pathlib import Path
from fractions import Fraction

BITS=72
Q=1<<BITS
LOG_TERMS=16
OUT=Path(__file__).resolve().parent

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None): self.lo=lo; self.hi=lo if hi is None else hi
    @staticmethod
    def rat(a,b=1): return I(a*Q//b,ceildiv(a*Q,b))
    @staticmethod
    def coerce(x): return x if isinstance(x,I) else I.rat(x)
    def __add__(self,b):
        b=I.coerce(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,b): return self+-I.coerce(b)
    def __rsub__(self,b): return I.coerce(b)+-self
    def __mul__(self,b):
        b=I.coerce(b); v=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return I(min(v)//Q,ceildiv(max(v),Q))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.coerce(b)
        if b.lo<=0: raise ArithmeticError('nonpositive divisor')
        vals=(self.lo*Q//b.lo,self.lo*Q//b.hi,self.hi*Q//b.lo,self.hi*Q//b.hi)
        ups=(ceildiv(self.lo*Q,b.lo),ceildiv(self.lo*Q,b.hi),ceildiv(self.hi*Q,b.lo),ceildiv(self.hi*Q,b.hi))
        return I(min(vals),max(ups))
    def sq(self):
        ma=max(self.lo*self.lo,self.hi*self.hi)
        mi=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return I(mi//Q,ceildiv(ma,Q))
    def log(self):
        assert self.lo>0
        a=logpoint(self.lo);b=logpoint(self.hi)
        return I(a[0],b[1])
    def json(self): return [str(self.lo),str(self.hi)]

@lru_cache(maxsize=200000)
def logpoint(a):
    """Enclose log(a/Q) by the positive atanh series and its exact tail."""
    assert a>0
    neg=a<Q
    y=I.rat(abs(a-Q),a+Q)
    assert 0<=y.lo<=y.hi<Q
    y2=y.sq(); power=y; total=I.rat(0)
    for k in range(LOG_TERMS):
        total=total+power/(2*k+1)
        power=power*y2
    tail=2*power/((2*LOG_TERMS+1)*(1-y2))
    value=I(2*total.lo,2*total.hi+tail.hi)
    if neg:value=-value
    return value.lo,value.hi

def multiply(xs):
    ans=I.rat(1)
    for x in xs:ans=ans*x
    return ans

def envelope(box,tlo,thi):
    """Return rational upper interval on U, an upper bound on scalar T."""
    r=box[:3]; z=box[3]; a=[x.sq() for x in r]; u=[1-x for x in a]
    rr=multiply(r); determinant=1-sum(a)+2*rr*z
    if determinant.lo<=0:return None
    c=[-x.log() for x in u]; tau=(multiply(u)/determinant).log()
    conditional=[]
    for i in range(3):
        j,k=[h for h in range(3) if h!=i]
        residual=(r[i]-r[j]*r[k]).sq()+2*rr*(1-z)
        ci=(1+residual/determinant).log()
        conditional.append(I(max(0,ci.lo),ci.hi))
        alt=conditional[-1]-c[i]
        tau=I(max(tau.lo,alt.lo),min(tau.hi,alt.hi))
        assert tau.lo<=tau.hi
    def kval(i,t):
        j,k=[h for h in range(3) if h!=i]
        N=t[i]*(1+t[j]*u[k]+t[k]*u[j]+t[j]*t[k]*determinant)
        B=1+t[j]+t[k]+t[j]*t[k]*u[i]
        odds=N/B
        lower=(I(odds.lo)/(1+I(odds.lo))).lo
        upper=(I(odds.hi)/(1+I(odds.hi))).hi
        # Schur complementation: the effective inclusion odds do not exceed t_i.
        upper=min(upper,(t[i]/(1+t[i])).hi)
        return I(lower,upper)
    d=[]
    for i in range(3):
        low=kval(i,[tlo if h==i else thi for h in range(3)])
        high=kval(i,[thi if h==i else tlo for h in range(3)])
        # External-field marginal monotonicity supplies this interval for every field.
        k=I(max(0,low.lo),min(Q,high.hi))
        di=c[i]+tau*k
        p=(1-I(k.lo))*c[i]+I(k.lo)*conditional[i]
        q=(1-I(k.hi))*c[i]+I(k.hi)*conditional[i]
        # M_ii=(1-K_ii)c_i+K_ii(c_i+tau), a convex interpolation.
        di=I(max(di.lo,min(p.lo,q.lo)),min(di.hi,max(p.hi,q.hi)))
        assert di.lo<=di.hi
        d.append(di)
    if any(x.lo<=0 for x in d):return None
    U=sum(d[(i+1)%3]*d[(i+2)%3]/(4*d[i]) for i in range(3))
    s=I((tlo/(1+tlo)).lo,(thi/(1+thi)).hi)
    for i in range(3):
        j,k=[h for h in range(3) if h!=i]
        rho=(a[i]-2*s*rr*z+s.sq()*a[j]*a[k])/((1-s*a[j])*(1-s*a[k]))
        # If this enclosure is poor, |K_jk|^2<=1/4 always remains valid.
        if rho.hi>=Q:
            W=I.rat(1,4)
        else:
            b=I(max(0,rho.hi))
            W=b/(4*(2-b).sq())
        U=U+2*tau.sq()*W/(d[j]*d[k])
    return U

def contract(box):
    """Retain all points with r0<=r1<=r2; other orders use site permutations."""
    b=[I(x.lo,x.hi) for x in box]
    for j in (1,2):b[j].lo=max(b[j].lo,b[j-1].lo)
    for j in (1,0):b[j].hi=min(b[j].hi,b[j+1].hi)
    return None if any(x.lo>x.hi for x in b) else b

def split_dim(box):
    # Heuristic controls runtime only. Every chosen split is checked exactly.
    scores=[Fraction(x.hi-x.lo,x.lo+Q//20) for x in box[:3]]
    scores.append(Fraction(2*(box[3].hi-box[3].lo),5*Q))
    return max(range(4),key=lambda j:scores[j])

def split(box,j):
    m=(box[j].lo+box[j].hi)//2
    assert box[j].lo<m<box[j].hi
    b=[I(x.lo,x.hi) for x in box]; c=[I(x.lo,x.hi) for x in box]
    b[j].hi=m;c[j].lo=m
    return b,c

def make_root(lo,hi):
    il=I.rat(*lo);ih=I.rat(*hi)
    return [I(il.lo,ih.hi) for _ in range(3)]+[I(-Q,Q)]

def validate_parameters(lo,hi,tlow,thigh,threshold):
    assert 0<Fraction(*lo)<=Fraction(*hi)<Fraction(1,2)
    assert 0<Fraction(*tlow)<=Fraction(*thigh)
    assert 0<Fraction(*threshold)<Fraction(3,2)

def generate(lo,hi,tlow,thigh,max_nodes,threshold):
    validate_parameters(lo,hi,tlow,thigh,threshold)
    root=make_root(lo,hi);tl=I.rat(*tlow);th=I.rat(*thigh);target=I.rat(*threshold).lo
    stack=[(root,0)];tree=[]; stats={'nodes':0,'certified':0,'outside':0,'max_depth':0,'max_U_numerator':0,'unresolved':0}
    start=time.monotonic()
    while stack:
        box,depth=stack.pop();stats['nodes']+=1
        b=contract(box)
        if b is None:tree.append('X');stats['outside']+=1;continue
        ans=envelope(b,tl,th)
        if ans is not None and ans.hi<=target:
            tree.append('C');stats['certified']+=1
            stats['max_U_numerator']=max(stats['max_U_numerator'],ans.hi)
            stats['max_depth']=max(stats['max_depth'],depth)
        elif stats['nodes']>=max_nodes:
            tree.append('U');stats['unresolved']+=1
        else:
            j=split_dim(b);left,right=split(b,j);tree.append(str(j))
            stack.append((right,depth+1));stack.append((left,depth+1))
        if stats['nodes']%2048==0:
            print(json.dumps({**stats,'stack':len(stack),'elapsed_seconds':round(time.monotonic()-start,2)}),flush=True)
    certificate={'format':'C082-exact-fixed-point-interval-tree-v1','bits':BITS,'log_terms':LOG_TERMS,'radius_lower':lo,'radius_upper':hi,'field_lower':tlow,'field_upper':thigh,'threshold':threshold,'tree':''.join(tree),'stats':stats}
    certificate['tree_sha256']=hashlib.sha256(certificate['tree'].encode()).hexdigest()
    certificate['wall_seconds']=round(time.monotonic()-start,3)
    name='certificate.json' if stats['unresolved']==0 else 'partial-certificate.json'
    (OUT/name).write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({k:v for k,v in certificate.items() if k!='tree'},indent=2),flush=True)
    return certificate

def verify(path):
    data=json.loads(Path(path).read_text());assert data['bits']==BITS and data['log_terms']==LOG_TERMS
    validate_parameters(data['radius_lower'],data['radius_upper'],data['field_lower'],data['field_upper'],data['threshold'])
    assert hashlib.sha256(data['tree'].encode()).hexdigest()==data['tree_sha256']
    root=make_root(data['radius_lower'],data['radius_upper']);tl=I.rat(*data['field_lower']);th=I.rat(*data['field_upper']);target=I.rat(*data['threshold']).lo
    stack=[root];certified=outside=unresolved=0; maxupper=0
    for a in data['tree']:
        assert stack, 'trailing tree data'
        box=contract(stack.pop())
        if a=='X':assert box is None;outside+=1;continue
        assert box is not None
        if a=='C':
            result=envelope(box,tl,th);assert result is not None and result.hi<=target
            maxupper=max(maxupper,result.hi);certified+=1
        elif a=='U':unresolved+=1
        else:
            assert a in '0123';left,right=split(box,int(a));stack.extend([right,left])
    assert not stack,'incomplete partition tree'
    assert certified==data['stats']['certified'] and outside==data['stats']['outside'] and unresolved==data['stats']['unresolved']
    assert maxupper==data['stats']['max_U_numerator']
    print(json.dumps({'verification':'PASS','certified_leaves':certified,'outside_leaves':outside,'unresolved_leaves':unresolved,'upper_numerator':str(maxupper),'denominator':str(Q),'strict_target':data['threshold']}),flush=True)
    return not unresolved

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--verify');p.add_argument('--max-nodes',type=int,default=1000000);p.add_argument('--lo',default='1/10');p.add_argument('--hi',default='2/5');p.add_argument('--tlo',default='1/2');p.add_argument('--thi',default='2');p.add_argument('--threshold',default='7/5');a=p.parse_args()
    if a.verify: raise SystemExit(0 if verify(a.verify) else 2)
    else:
        f=lambda s: [Fraction(s).numerator,Fraction(s).denominator]
        generate(f(a.lo),f(a.hi),f(a.tlo),f(a.thi),a.max_nodes,f(a.threshold))
