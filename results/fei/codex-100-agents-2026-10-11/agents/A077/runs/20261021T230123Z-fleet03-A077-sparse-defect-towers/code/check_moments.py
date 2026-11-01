"""Independent direct-character/dyadic lane; frozen two-pair domain."""
from fractions import Fraction as Q
from pathlib import Path
import json,time
start=time.monotonic()
def spectrum(f):
    return [Q(sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(8)),8) for s in range(8)]
def g(a):
    a=abs(a)
    if not a: return Q(0)
    n,d=a.numerator,a.denominator
    assert n&(n-1)==0 and d&(d-1)==0
    return 2*a*a*(d.bit_length()-n.bit_length())
def collision(a,b): return sum(((g(x+y)+g(x-y))/2-g(x)-g(y) for x,y in zip(a[1:],b[1:])),Q(0))
signs=[(1-2*(x&1),1-2*((x>>1)&1),1-2*((x>>2)&1)) for x in range(8)]
def maj(x,y,z): return 1 if x+y+z>0 else -1
pairs=[([x for x,y,z in signs],[y for x,y,z in signs]),([maj(x,y,z) for x,y,z in signs],[maj(x,-y,-z) for x,y,z in signs])]
out=[]
for j,(v,w) in enumerate(pairs):
    a,b=spectrum(v),spectrum(w)
    moments=[Q(sum(v),8),Q(sum(w),8),Q(sum(x*y for x,y in zip(v,w)),8)]
    assert moments==[0,0,0]
    c=collision(a,b)
    assert c==(0 if j==0 else -4)
    out.append({'pair':j,'moments':[str(z) for z in moments],'Xi_over_e':str(c),'Vhat':[str(z) for z in a],'What':[str(z) for z in b]})
assert time.monotonic()-start<55
r={'status':'PASS','pairs':out,'exact_assertions':5,'elapsed_seconds':time.monotonic()-start,'method':'direct character sums; dyadic integer logarithms; independent of check_profiles.py'}
(Path(__file__).resolve().parents[1]/'out/moments.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r))
