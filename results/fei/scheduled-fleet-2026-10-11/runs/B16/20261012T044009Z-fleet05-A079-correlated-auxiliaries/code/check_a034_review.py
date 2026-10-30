import json,time
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
helper=(ROOT/'code'/'check_transport.py').read_text().split('for k,m in [(1,1),(2,1)]:')[0]
scope={'__file__':str(ROOT/'code'/'check_transport.py')}
exec(compile(helper,str(ROOT/'code'/'check_transport.py'),'exec'),scope)
walsh,sign,H,plus,law=map(scope.get,['walsh','sign','H','plus','law'])
START=time.perf_counter();ASSERTIONS=0;CASES=0

def check(ok):
    global ASSERTIONS
    ASSERTIONS+=1;assert ok,ASSERTIONS
    if time.perf_counter()-START>60:raise RuntimeError('Frozen runtime cap')

def rank(rows):
    piv={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;break
    return len(piv)

def phase(y,mask):
    v=mask&1
    for i in range(3):v^=((mask>>(1+i))&1)*((y>>i)&1)
    for z,(i,j) in enumerate([(0,1),(0,2),(1,2)]):v^=((mask>>(4+z))&1)*((y>>i)&1)*((y>>j)&1)
    return v

def rowcheck(A,mask):
    base=A[0];V=[y^base for y in A]
    basis=[]
    for v in V:
        if rank(basis+[v])>len(basis):basis.append(v)
    def polar(v,w):return phase(base,mask)^phase(base^v,mask)^phase(base^w,mask)^phase(base^v^w,mask)
    mat=[sum(polar(v,w)<<j for j,w in enumerate(basis)) for v in basis]
    r=rank(mat);codim=3-len(basis);expected=codim+r
    u=[(-1)**phase(y,mask) if y in A else 0 for y in range(8)]
    w=walsh(u);alpha=Q(len(A),8)
    raw=[Q(z*z,64) for z in w];p=[z/alpha for z in raw]
    support=[i for i,z in enumerate(p) if z]
    check(sum(raw)==alpha)
    check(len(support)==1<<expected)
    check(all(p[i]==Q(1,1<<expected) for i in support))
    check(H(p)==({2:Q(expected)} if expected else {}))
    varies=sum(len({s>>i&1 for s in support})==2 for i in range(3))
    ones=sum(all(s>>i&1 for s in support) for i in range(3))
    energy=sum((p[s]*s.bit_count() for s in range(8)),Q(0))
    check(energy==Q(varies,2)+ones)
    check(expected<=2*energy)
    return expected,energy

for mask in range(128):
    for normal in range(1,8):
        for coset in [0,1]:
            cells=[[y for y in range(8) if (normal&y).bit_count()%2==b^coset] for b in [0,1]]
            expr=[rowcheck(A,mask) for A in cells]
            f=[(-1)**phase(y,mask)*sign(x*((normal&y).bit_count()%2^coset)) for y in range(8) for x in range(2)]
            p=law(f);px=[sum((p[v+2*t] for t in range(8)),Q(0)) for v in range(2)]
            cond=sum(Q(e,2) for e,_ in expr)
            iy=sum((p[s]*(s>>1).bit_count() for s in range(16)),Q(0))
            check(H(px)=={2:Q(1)})
            check(H(p)=={2:1+cond})
            check(plus((1,H(p)),(-1,H(px)))==({2:cond} if cond else {}))
            check(iy==sum(en/2 for _,en in expr))
            check(cond<=2*iy and 1+cond<=4*iy)
            CASES+=1
    rowcheck(list(range(8)),mask);CASES+=1
out={'status':'PASS','cases':CASES,'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'GF(2) polar rank; integer Walsh/Fraction; exact entropy','review_target':'A034-QUADRATIC-AFFINE-ROW-CONDITIONAL v1','scope':'independent finite sanity check; all-dimensional acceptance rests on reconstruction in REVIEW_A034.md'}
(ROOT/'out'/'a034_review_validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
