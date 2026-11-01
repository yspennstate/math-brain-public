from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

class Q2:
    """Exact a+b*sqrt(2), with rational a,b."""
    __slots__ = ("a","b")
    def __init__(self,a=0,b=0):
        self.a = a if isinstance(a,F) else F(a)
        self.b = b if isinstance(b,F) else F(b)
    @staticmethod
    def coerce(x):
        return x if isinstance(x,Q2) else Q2(x,0)
    def __add__(self,o):
        o=Q2.coerce(o); return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o): return self + (-Q2.coerce(o))
    def __rsub__(self,o): return Q2.coerce(o)-self
    def __mul__(self,o):
        o=Q2.coerce(o)
        return Q2(self.a*o.a+2*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        den=self.a*self.a-2*self.b*self.b
        if den==0: raise ZeroDivisionError
        return Q2(self.a/den,-self.b/den)
    def __truediv__(self,o): return self*Q2.coerce(o).inv()
    def __rtruediv__(self,o): return Q2.coerce(o)/self
    def sign(self):
        a,b=self.a,self.b
        if a==0 and b==0:return 0
        if b==0:return 1 if a>0 else -1
        if a==0:return 1 if b>0 else -1
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        aa=a*a; bb=2*b*b
        if a>0 and b<0:
            return 1 if aa>bb else (-1 if aa<bb else 0)
        return 1 if bb>aa else (-1 if bb<aa else 0)
    def __eq__(self,o):
        o=Q2.coerce(o); return self.a==o.a and self.b==o.b
    def __lt__(self,o): return (self-Q2.coerce(o)).sign()<0
    def __le__(self,o): return (self-Q2.coerce(o)).sign()<=0
    def __gt__(self,o): return (self-Q2.coerce(o)).sign()>0
    def __ge__(self,o): return (self-Q2.coerce(o)).sign()>=0
    def __abs__(self): return self if self.sign()>=0 else -self
    def __repr__(self): return f"Q2({self.a},{self.b})"
    def pretty(self):
        if self.b==0:return str(self.a)
        return f"({self.a})+({self.b})*sqrt2"
    def approx(self): return float(self.a)+float(self.b)*(2.0**0.5)

ZERO=Q2(0); ONE=Q2(1); SQ2=Q2(0,1)
T0=Q2(F(9,4),1)
K0=Q2(F(1,2),1)
assert K0*K0 == T0

SIGNS=[(1,)+x for x in product((-1,1), repeat=3)]

x=Q2(F(3,7),F(-1,7))
y=Q2(F(-2,7),F(3,7))
WEIGHTS=[]
NAMES=[]
for pos in range(4):
    w=[x,x,x,x]; w[pos]=y
    WEIGHTS.append(tuple(w)); NAMES.append(f"surd_large_{pos}")
for pos in range(4):
    w=[Q2(F(3,11)) for _ in range(4)]; w[pos]=Q2(F(2,11))
    WEIGHTS.append(tuple(w)); NAMES.append(f"rational_small_{pos}_2_3_3_3")
RWS=[
    (13,1,1,1),(3,4,4,5),(5,4,5,2),(4,5,4,3),(4,3,3,6),
    (1,5,5,5),(4,1,5,6),(4,5,1,6),(4,3,5,4),(4,5,6,1),
    (4,3,4,5),(6,1,1,8),(4,1,9,2),(4,9,1,2),
]
for aa in RWS:
    WEIGHTS.append(tuple(Q2(F(z,16)) for z in aa)); NAMES.append("rational_"+"_".join(map(str,aa)))
for w in WEIGHTS:
    assert sum(w,ZERO)==ONE and all(z>ZERO for z in w)

def set_partitions(n):
    out=[]; blocks=[]
    def rec(i):
        if i==n:
            out.append(tuple(tuple(b) for b in blocks)); return
        for b in blocks:
            b.append(i); rec(i+1); b.pop()
        blocks.append([i]); rec(i+1); blocks.pop()
    rec(0); return out
PARTITIONS=set_partitions(8)
assert len(PARTITIONS)==4140

def orientation_options(block):
    k=len(block)
    for tail in product((-1,1), repeat=k-1):
        sig=(1,)+tail
        yield tuple(sig[j]*(block[j]+1) for j in range(k))

def oriented_vectors(key):
    out=[]
    for z in key:
        sg=1 if z>0 else -1
        s=SIGNS[abs(z)-1]
        out.append(tuple(sg*t for t in s))
    return out

@lru_cache(None)
def block_lb(key, wi):
    lam=WEIGHTS[wi]
    vecs=oriented_vectors(key); k=len(vecs)
    best=ZERO
    for mask in range(1,1<<k):
        q=mask.bit_count(); v=[0,0,0,0]
        for i,t in enumerate(vecs):
            if (mask>>i)&1:
                for j in range(4): v[j]+=t[j]
        if v==[0,0,0,0]:
            return None
        den=ZERO
        for j in range(4):
            den += Q2(v[j]*v[j])/lam[j]
        val=Q2(q*q)/den
        if val>best: best=val
    return best

C=(2,1,1,1)
count=0; equality_count=0; equality_examples=[]; usage=[0]*len(WEIGHTS)
for part in PARTITIONS:
    opts=[tuple(orientation_options(b)) for b in part]
    for keys in product(*opts):
        count+=1; ok=False
        for wi,w in enumerate(WEIGHTS):
            total=ZERO; infeasible=False
            for key in keys:
                z=block_lb(key,wi)
                if z is None:
                    infeasible=True; break
                total += z
            if infeasible:
                ok=True; usage[wi]+=1; break
            target=sum((w[j]*C[j] for j in range(4)),ZERO)/T0
            if total>=target:
                ok=True; usage[wi]+=1
                if total==target:
                    equality_count+=1
                    if len(equality_examples)<12:
                        equality_examples.append((part,keys,NAMES[wi]))
                break
        if not ok:
            raise AssertionError(("UNCERTIFIED",count,part,keys))
assert count==75905

h=SQ2/Q2(2)
U=[
    (h,h,h,h),
    (Q2(F(-1,2)),Q2(F(-1,2)),Q2(F(1,2)),Q2(F(1,2))),
    (-h,h,ZERO,ZERO),
    (ZERO,ZERO,-h,h),
]
col_norm2=[]
for u in U:
    col_norm2.append(sum((z*z for z in u),ZERO))
assert col_norm2 == [Q2(2),Q2(1),Q2(1),Q2(1)]
for s in SIGNS:
    rows=[]
    for i in range(4):
        rows.append(sum((Q2(s[j])*U[j][i] for j in range(4)),ZERO))
    mx=max((abs(z) for z in rows))
    assert mx==K0

assert T0 < Q2(F(15,4))

strict=[]; retained=[]
for n in range(5,76):
    q=(n+4)//5
    new=T0*q
    old=Q2(F(3*n,4))
    if new<old: strict.append(n)
    else: retained.append(n)
expected=[5,10,15,20,25,30,35,40,44,45,49,50,54,55,59,60,64,65,69,70,74,75]
assert strict==expected
assert T0*16 > Q2(57)
assert F(18*22,7) < 57

print("R13 exact weighted-4 / n=5 checker")
print("oriented_configurations=",count)
print("certificate_weights=",len(WEIGHTS))
print("equality_certificates_selected=",equality_count)
print("equality_examples=",equality_examples)
print("weighted4_sharp_column_norm2=",[z.pretty() for z in col_norm2])
print("weighted4_exact_constant= sqrt(2)+1/2")
print("B5_squared_before=15/4")
print("B5_squared_after=9/4+sqrt(2)")
print("B5_after=sqrt(2)+1/2")
print("propagated_strict_improvements=",len(strict),strict)
print("retained_old_finite_entries=",len(retained),retained)
print("weight_usage_nonzero=",[(NAMES[i],c) for i,c in enumerate(usage) if c])
print("ALL_EXACT_CHECKS_PASS")
