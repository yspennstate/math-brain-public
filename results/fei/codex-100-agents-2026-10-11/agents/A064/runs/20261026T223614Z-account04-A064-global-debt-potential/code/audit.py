"""Independent direct-character Fourier check and complete-cut enumeration."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, time
import check as c

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
checks=0
def ok(b):
    global checks
    checks+=1
    assert b,checks
def direct(t):
    N=len(t)
    return [F(sum(t[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N))**2,N*N) for s in range(N)]
cores=0
for n in range(4):
    for m in range(2**(2**n)):
        t=[-1 if m>>x&1 else 1 for x in range(2**n)]
        p=direct(t); ok(p==c.spectral(t)); cores+=1
        # Omit disjointness: reusing the exact same factor squares to constant.
        pp=direct([x*x for x in t]); ok(pp==[F(1)]+[F(0)]*(len(t)-1))

# Independent cut representation: nodes are (offset,width) intervals of leaves.
def cuts(offset,width):
    r=[[(offset,width)]]
    if width>1:
        half=width//2
        r.extend(a+b for a in cuts(offset,half) for b in cuts(offset+half,half))
    return r
allcuts=cuts(0,8); ok(len(allcuts)==26)
vectors=0
# A smaller independent corpus; the full 65536-vector census is in check.py.
for leaves in product([0,1,3],repeat=8):
    before=sum(max(2,x) for x in leaves)
    after=max(16,sum(leaves))
    bv=[]
    for cut in allcuts:
        total=0
        for a,w in cut:
            total += (sum(max(2,x) for x in leaves[a:a+w]) if w==1 else 2*w)
        bv.append(total)
    ok(max(bv)==before)
    # After pivot every proper early lottery stop has current cost zero.
    av=[sum(leaves[a] for a,w in cut if w==1) for cut in allcuts]
    ok(max([16]+av)==after)
    ok(before>=after); vectors+=1

# Explicit genuinely Boolean tensor: 64 disjoint point_3 factors, k=3.
t=[-1]+[1]*7
p=direct(t); H=c.entropy(p)
T=c.sub(c.mul(c.entropy([F(1,4),F(3,4)]),3),H)
ok(T==(F(2),F(-9,8),F(0),F(0)))
L=c.mul(T,64); lam=c.mul(L,F(1,8))
before=c.mul(c.sub(L,c.const(2)),F(1,8))
ok(c.ge(L,c.const(13))); ok(c.ge(c.const(14),L))
ok(c.ge(c.const(2),lam))
ok(c.positive(c.sub(lam,c.const(2)))==c.Z)
ok(c.ge(before,c.const(F(11,8))))
ok(c.ge(c.const(F(3,2)),before))
ok(c.ge(c.const(4*49),c.add(c.mul(H,64),c.const(2))))

# A087's sharper all-dimensional terminal lower bound, independent small points.
point_rows=[]
for m in range(2,9):
    N=2**m; p=direct([-1]+[1]*(N-1)); d=F(2,N)
    ok(p[0]==(1-d)**2); ok(all(x==d*d for x in p[1:]))
    # Exact algebra of retaining just -d log2 d in h2(d).
    # -x log2 x>=0 on 0<x<=1; no extra numerical logarithm is needed.
    ok(0<1-d<1)
    point_rows.append({'m':m,'I_F':m+1,'lower_ratio':str(F(m*(m-1),m+1))})
out={'status':'PASS','checks':checks,'cores_direct_character':cores,
     'cuts_per_vector':26,'independent_vectors':vectors,
     'fixture':{'core':'64 disjoint point_3 factors','physical_dimension_with_mask':194,
                'L':'128-72 log2(3)','E_L':'16-9 log2(3)',
                'before_extra':'63/4-9 log2(3)','after_extra':'0',
                'L_bounds':[13,14],'before_extra_bounds':['11/8','3/2']},
     'A087_full_terminal_rows':point_rows,'seconds':round(time.perf_counter()-start,6)}
(root/'out'/'AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['fixture','A087_full_terminal_rows']}))
