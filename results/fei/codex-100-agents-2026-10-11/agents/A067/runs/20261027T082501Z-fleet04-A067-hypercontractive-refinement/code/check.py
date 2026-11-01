from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import ast, json, time, sys, hashlib, itertools

R=Path(__file__).resolve().parents[1]; ROOT=R.parents[1]
mode=sys.argv[1]; started=time.monotonic(); checks=0
def ck(test):
    global checks
    checks+=1
    assert test, checks
    assert time.monotonic()-started<58, 'frozen runtime exceeded'

helper=ROOT/'runs/20261023T120754Z-fleet03-A067-hypercontractive-refinement/code/check.py'
names={'wal','sp','rest','marg','inf','TI','ln','lg','pt','add','mul','sub','overlaps','CE','enc'}
tree=ast.parse(helper.read_text(encoding='utf-8'))
body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names]
exec(compile(ast.Module(body=body,type_ignores=[]),str(helper),'exec'))
L2=ln(F(2))
def entropy(p): return CE(p,p)
def weights(v):
    # Independent unnormalised integer Walsh; compare to inherited helper.
    a=list(v); j=1
    while j<len(a):
        for base in range(0,len(a),2*j):
            for t in range(j):
                u,w=a[base+t],a[base+t+j]
                a[base+t],a[base+t+j]=u+w,u-w
        j*=2
    return a
def seed(n,kind,affine):
    edges=[(i,i+1) for i in range(0,n,2)] if kind=='matching' else list(itertools.combinations(range(n),2))
    return tuple((-1)**(sum(((x>>i)&1)*((x>>j)&1) for i,j in edges)+(x&affine).bit_count()) for x in range(1<<n))
def scatter(x,labels): return sum(((x>>j)&1)<<i for j,i in enumerate(labels))
def erase_index(x,j): return (x&((1<<j)-1))|((x>>(j+1))<<j)
def ceil_log(k): return (k-1).bit_length()

cases=[(4,'matching',0,(0,1,2)),(4,'complete',5,(0,3,7,15))] if mode=='pilot' else [
    (4,'matching',0,(0,)),(4,'complete',5,(0,3)),
    (6,'matching',9,(0,1,3,7)),(6,'complete',17,(2,5,8,13,21,34,55)),
    (8,'matching',37,tuple(range(16))),
    (12,'complete',137,tuple((157*j)%4096 for j in range(16)))]
if mode=='boundary':
    cases=[(8,'complete',37,(0,3,7,255)),(12,'complete',137,tuple((157*j)%4096 for j in range(16)))]
rows=[]; states=0; zero_labels=0; occupation_checks=0
for n,kind,affine,marks in cases:
    m=n//2; k=len(marks); d=F(1,1<<n); A=F(1,1<<m); x=k*A
    b0=seed(n,kind,affine); b=b0+b0
    c=tuple(-v if i in marks else v for i,v in enumerate(b))
    qb,qc=sp(b),sp(c)
    ck(all(v==d for v in qb[:1<<n]) and all(v==0 for v in qb[1<<n:]))
    ck(TI(b)==m); ck(inf(c,n)==k*d)
    ck(TI(c)>=m-n*k*d+k*d)
    raw=weights(c); ck(qc==tuple(F(a*a,len(c)**2) for a in raw))
    hroot=mul(add(entropy(qb),entropy(qc)),F(1,2))
    r4=sub(pt(4*(TI(b)+TI(c))/2),entropy(sp(b+c)))
    ck(r4[0]>=2*m-4*m*k*d+2*k*d-2)
    def walk(v,q,lab,live,reach,depth):
        global states,zero_labels,occupation_checks
        states+=1
        p=sp(v); ck(sum(q)==sum(p)==1)
        ck(all(pp==0 or qq>0 for pp,qq in zip(p,q)))
        w_live=n in lab
        if w_live:
            t=n-sum(label<n for label in lab); wi=lab.index(n)
            mass=sum(pp for s,pp in enumerate(p) if (s>>wi)&1)
            ck(mass==len(live)*(1<<t)*d)
            ck(inf(v,wi)==mass)
            # Independently reconstruct every Q1 marginal from signed buckets.
            erased=[j for j in range(n) if j not in lab]
            remaining=[j for j in lab if j<n]
            for r in range(1<<len(remaining)):
                buckets={}
                ss=scatter(r,remaining)
                for e in marks:
                    key=tuple((e>>j)&1 for j in erased)
                    buckets[key]=b0[e]*(-1)**((e&ss).bit_count())+buckets.get(key,0)
                expected=(1<<t)*d*d*sum(a*a for a in buckets.values())
                ii=sum(((r>>j)&1)<<lab.index(label) for j,label in enumerate(remaining))|(1<<wi)
                ck(q[ii]==expected)
                if expected: ck((1<<t)*d*d<=expected<=(1<<t)*k*k*d*d)
                else: zero_labels+=1
        if not live or not lab:
            return {'L':F(0),'rare':F(0),'wmass':F(0),'J':F(0),'H':mul(entropy(p),reach),'C':mul(CE(p,q),reach),'K':mul(sub(CE(p,q),entropy(p)),reach),'depth':reach*depth}
        # Deterministic adaptive order depends on marked input and branch state.
        j=(sum(live)+depth)%len(lab)
        label=lab[j]; qq=marg(q,j)
        for s,qqs in enumerate(q):
            if not qqs: continue
            ratio=qq[erase_index(s,j)]/qqs
            if w_live and label<n and (s>>lab.index(n))&1: ck(ratio<=2*k*k)
            elif label<n and x<=F(1,4): ck(ratio<F(4))
        newlab=lab[:j]+lab[j+1:]
        children=[]
        for bit in (0,1):
            newlive=[e for e in live if (0 if label==n else (e>>label)&1)==bit]
            children.append(walk(rest(v,j,bit),qq,newlab,newlive,reach/2,depth+1))
        z={key:children[0][key]+children[1][key] for key in children[0]}
        z['L']+=reach
        z['J']+=reach*inf(v,j)
        if w_live:
            if label==n:z['wmass']+=reach*mass
            else:z['rare']+=reach*mass
        ck(z['K'][1]<=z['depth'])
        occupation_checks+=1
        return z
    # Restrict expensive n=12 identity checks to a frozen 4-query prefix.
    if n==12 and mode!='boundary':
        v=c; q=qc; labels=list(range(n+1)); live=list(marks)
        for label in (0,3,n,1):
            j=labels.index(label); qm=marg(q,j)
            for s,qs in enumerate(q):
                if not qs:continue
                ratio=qm[erase_index(s,j)]/qs
                if label<n:
                    ck(ratio<=2*k*k if n in labels and (s>>labels.index(n))&1 else ratio<4)
            v=rest(v,j,0);q=qm;labels.remove(label)
            live=[e for e in live if label==n or not((e>>label)&1)]
        ck(k<=1<<(m-2))
        rows.append({'n':n,'k':k,'kind':kind,'scope':'fixed four-query conditional audit, actual original source','r4':enc(r4)})
        continue
    out=walk(c,qc,list(range(n+1)),list(marks),F(1,2),0)
    L=out['L']; ck(L<=F(ceil_log(k)+2,2))
    ck(out['rare']<=n*k*d/2); ck(out['wmass']<=k*d/2)
    # Keep original b sibling and both full CE/KL terminal bills.
    hh=add(mul(entropy(qb),F(1,2)),out['H'])
    cc=add(mul(entropy(qb),F(1,2)),out['C'])
    eh=sub(sub(hroot,hh),pt(4*out['J']))
    eq=sub(sub(hroot,cc),pt(4*out['J']))
    ck(overlaps(eh,add(eq,out['K'])))
    if x<=F(1,4):
        bound=add(pt(3*L+F(1,12)+(n-2)*k*d/2),mul(lg(F(2*k*k)),n*k*d/2))
        ck(eh[1]<bound[0])
    rows.append({'n':n,'k':k,'kind':kind,'L':str(L),'rare':str(out['rare']),'actual_debit':enc(eh),'full_KL':enc(out['K']),'r4':enc(r4)})

# Exact endpoint and discrete monotonicity, no floating inference.
ck(F(6,2)-F(25,12)-F(2*6*6+2*6-1,4*2**6)==F(455,768))
for m in range(6,257):
    aa=2*m*m+2*m-1; bb=2*(m+1)**2+2*(m+1)-1
    ck(2*aa-bb==2*m*m-2*m-5>0)
    ck(F(m,2)-F(25,12)-F(aa,4*2**m)>=F(455,768))
result={'status':'PASS','mode':mode,'checks':checks,'states':states,'zero_labels_retained':zero_labels,'occupation_checks':occupation_checks,'cases':rows,'runtime_seconds':time.monotonic()-started,'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest()}
(R/'out').mkdir(exist_ok=True)
(R/'out'/('PILOT.json' if mode=='pilot' else 'BOUNDARY.json' if mode=='boundary' else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
