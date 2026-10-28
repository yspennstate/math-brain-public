import hashlib,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache

R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py'
source=OLD.read_text(encoding='utf-8')
defs=source[source.index('def ck(x):'):source.index("transport={'positive'")]
ns={'Q':Q,'lru_cache':lru_cache,'checks':0}
exec(defs,ns)
ck=ns['ck']; sp=ns['spectrum']; fw=ns['fw']; ce=ns['ce']; add=ns['add']; gate=ns['gate']; psi=ns['psi']; nn=ns['nonnegative']; iv=ns['interval']; lf=ns['logform']
pilot='--pilot' in sys.argv
start=time.monotonic()
def enc(f): return {str(p):str(v) for p,v in f.items()}
def kl(p,q): return add((1,ce(p,q)),(-1,ce(p,p)))
def contam(p): return tuple((x+int(i==0))/2 for i,x in enumerate(p))
def parent_and_lift(a,b,qa,qb):
    h=tuple(x for pair in zip(a,b) for x in pair); p=sp(h); q=[]
    for i in range(len(a)):
        row=p[2*i]+p[2*i+1]; qr=(qa[i]+qb[i])/2
        q.extend((qr*p[2*i]/row,qr*p[2*i+1]/row) if row else (qr,Q(0)))
    ck(sum(q)==1)
    return h,p,tuple(q)
rows=[]
for k in ([2] if pilot else range(2,9)):
    eps=Q(1,1<<k)
    a=tuple(1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
    b=tuple(-1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
    p=sp(a); ck(p==sp(b)); q=contam(p)
    ck(Q(sum(a),len(a))==eps);ck(Q(sum(b),len(b))==-eps)
    ck(all(abs(sum(z))<len(z) for z in (a,b)))
    for j,v in enumerate(p): ck(v==((1-eps)**2 if j==1 else eps**2))
    h,ph,qh=parent_and_lift(a,b,q,q)
    ck(Q(sum(x!=y for x,y in zip(a,b)),len(a))==eps)
    ck(ph[0]==0); ck(ph[1]==eps**2);ck(qh[0]==0);ck(qh[1]==q[0])
    ck(kl(ph,qh)==kl(p,q)); ck(ce(ph,ph)==ce(p,p))
    influence=sum(v*i.bit_count() for i,v in enumerate(p))
    ck(influence==1+(k-1)*eps)
    ck(sum(v*i.bit_count() for i,v in enumerate(ph))==influence+eps)
    rt=gate(h,qh,1); ch=[gate(z,q,1) for z in (a,b)]
    ck(not rt[1]);ck(ch[0][1]==ch[1][1])
    lam=ch[0][1]
    m=eps**2; aa=(1+m)/2
    formula=add((m/8,lf(m/aa)),((1+m/4)/2,lf((1+aa/4)/(1+m/4))))
    ck(lam==formula)
    curvature=add((1,psi(Q(0))),(-1,psi(eps/2)))
    ck(add((1,rt[0]),(-Q(1,2),ch[0][0]),(-Q(1,2),ch[1][0]))==add((1,curvature),(1,lam)))
    ck(nn(add((1,lam),(-Q(1,32),{2:Q(1)}))));ck(nn(add((Q(1,8),{2:Q(1)}),(-1,lam))))
    bank=add((4*influence,{2:Q(1)}),(-1,ce(p,q)))
    ck(nn(add((1,bank),(-1,{2:Q(1)}))))
    # Half of the original core bank, including a prior 1/8 booking, stays positive.
    remaining=add((Q(1,2),bank),(-Q(1,8),{2:Q(1)}),(-1,lam))
    ck(nn(add((1,remaining),(-Q(1,4),{2:Q(1)}))))
    rows.append({'k':k,'d':str(eps),'Lambda':enc(lam),'core_bank':enc(bank),'remaining_after_old_1_over_8':enc(remaining)})
    (R/'out/PARTIAL.json').write_text(json.dumps({'completed_k':k,'checks':ns['checks']},indent=2),encoding='utf-8')
    assert time.monotonic()-start<60

# Boundary excluded from the >1 core-bank proof: k=1, checked rather than silently cancelled.
boundary={'k':1,'reason':'epsilon<=1/4 used only for k>=2; outside theorem scope'}
supp=0
if not pilot:
    fs=[tuple(1-2*((mask>>v)&1) for v in range(4)) for mask in range(16)]
    for a in fs:
        for b in fs:
            pa,pb=sp(a),sp(b);qa,qb=contam(pa),contam(pb)
            h,ph,qh=parent_and_lift(a,b,qa,qb)
            rt=gate(h,qh,1);ca,cb=gate(a,qa,1),gate(b,qb,1)
            dc=add((Q(1,2),kl(pa,qa)),(Q(1,2),kl(pb,qb)),(-1,kl(ph,qh)))
            ck(nn(dc))
            lam=add((Q(1,2),ca[1]),(Q(1,2),cb[1]),(-1,rt[1]),(-Q(1,2),dc))
            bound=add((Q(1,2),lf(1+(qa[0]+qb[0])/8)))
            ck(nn(add((1,bound),(-1,lam))))
            supp+=1
            assert time.monotonic()-start<60
    ck(145**4<2*128**4)
    ck(72**65>2**7*65**65)
out={'status':'PASS','helper_version':'A019-biased-empty-row-v1','source_helper_sha256':hashlib.sha256(source.encode()).hexdigest(),'structured_cases':len(rows),'all_two_bit_ordered_child_pairs':supp,'checks':ns['checks'],'seconds':time.monotonic()-start,'boundary':boundary,'rows':rows,'full_fei':'OPEN','proof_rung':'exact finite checks plus analytic all-k proof; independent review pending'}
(R/'out'/('PILOT.json' if pilot else 'CERTIFICATE.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
