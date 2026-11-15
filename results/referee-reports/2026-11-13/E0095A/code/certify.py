"""Exact rational certificates: integer Bareiss inertia and residual enclosures.
No floating-point assertion is accepted as a proof. --verify replays saved certs.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
from fractions import Fraction as F
from pathlib import Path
import json, argparse, time
import numpy as np
import networkx as nx
from search import matchings
ROOT=Path(__file__).resolve().parents[1]

def inertia(M):
    """Number of negative eigenvalues, provided all leading principal minors nonzero.
    Fraction-free symmetric elimination; pivot signs give Sylvester inertia.
    """
    a=[list(map(int,row)) for row in M];n=len(a);previous=1;neg=0
    for k in range(n):
        pivot=a[k][k]
        if not pivot:raise ArithmeticError('zero leading minor; choose another rational threshold')
        neg+=int(pivot*previous<0)
        for i in range(k+1,n):
            for j in range(i,n):
                val=pivot*a[i][j]-a[i][k]*a[k][j]
                assert val%previous==0
                a[i][j]=a[j][i]=val//previous
        previous=pivot
    return neg

def lap(adj,extra=()):
    a=[[int(x) for x in row] for row in adj];n=len(a)
    for u,v in extra:a[u][v]+=1;a[v][u]+=1
    d=[sum(row) for row in a]
    l=[[(d[i] if i==j else 0)-a[i][j] for j in range(n)] for i in range(n)]
    return l,d

def below(l,d,t):
    t=F(t);p,q=t.numerator,t.denominator
    return inertia([[q*l[i][j]-(p*d[i] if i==j else 0) for j in range(len(l))] for i in range(len(l))])

def ff(x):return str(x)
def sqint(a,b):
    assert a<=b
    return (F(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))

def base_certificate(a):
    l,d=lap(a);n=len(a);w,v=np.linalg.eigh(np.array(l,dtype=float));scale=10**12
    lo=F(int(np.floor(w[1]*scale))-2,scale);hi=F(int(np.ceil(w[1]*scale))+2,scale)
    assert below(l,[1]*n,lo)==1 and below(l,[1]*n,hi)==2
    thirdlo=F(int(np.floor(w[2]*scale))-2,scale);assert below(l,[1]*n,thirdlo)==2
    c=(lo+hi)/2;eta=min(c,thirdlo-c);assert eta>0
    denom=2**45;qnum=[int(round(x*denom)) for x in v[:,1]];q=[F(x,denom) for x in qnum]
    norm2=sum(x*x for x in q);assert F(1,2)<norm2<4
    residual=[sum(l[i][j]*q[j] for j in range(n))-c*q[i] for i in range(n)]
    residual2=sum(x*x for x in residual)
    delta=F(1,10**11)
    while delta*delta*eta*eta<residual2:delta*=10
    assert delta*delta<norm2
    return {'lambda2_lo':ff(lo),'lambda2_hi':ff(hi),'lambda3_lo':ff(thirdlo),'q_den':denom,'q_num':qnum,'delta':ff(delta)}

def verify_base(a,b):
    l,d=lap(a);n=len(a);lo=F(b['lambda2_lo']);hi=F(b['lambda2_hi']);thirdlo=F(b['lambda3_lo'])
    assert 0<lo<hi<thirdlo
    assert below(l,[1]*n,lo)==1 and below(l,[1]*n,hi)==2 and below(l,[1]*n,thirdlo)==2
    q=[F(x,b['q_den']) for x in b['q_num']];c=(lo+hi)/2;eta=min(c,thirdlo-c);delta=F(b['delta'])
    r2=sum((sum(l[i][j]*q[j] for j in range(n))-c*q[i])**2 for i in range(n))
    assert r2<=delta**2*eta**2 and delta**2<sum(x*x for x in q)<4
    return q,delta,lo/d[0],hi/d[0]

def edge_candidates(a,b,kind):
    q,de,mlo,mhi=verify_base(a,b);bounds=[]
    for u in range(len(a)):
      for v in range(u+1,len(a)):
        if a[u][v]:continue
        sl,sh=sqint(q[u]-q[v]-2*de,q[u]-q[v]+2*de)
        if kind=='corrected':
            ul,uh=sqint(q[u]-de,q[u]+de);vl,vh=sqint(q[v]-de,q[v]+de)
            sl-=mhi*(uh+vh);sh-=mlo*(ul+vl)
        bounds.append(((u,v),sl,sh))
    top=max(z[1] for z in bounds)
    return [e for e,sl,sh in bounds if sh>=top]

def matching_candidates(a,b):
    # For all matchings at once, norm(L_M)=2 gives |s(q)-s(f)| <= 8 delta+2 delta^2.
    delta=F(b['delta']);err=8*delta+2*delta*delta;qn=b['q_num'];den=b['q_den']
    scored=[];best=-1
    for m in matchings(np.array(a)):
        s=sum((qn[u]-qn[v])**2 for u,v in m);best=max(best,s);scored.append((m,s))
    return [m for m,s in scored if F(best-s,den*den)<=2*err]

def compare(a,winner,losers,threshold):
    for extra in [winner]+list(losers):
        assert len(extra)==len(winner)
        seen=set()
        for u,v in extra:
            assert 0<=u<len(a) and 0<=v<len(a) and u!=v and not a[u][v]
            if len(extra)>1:assert u not in seen and v not in seen
            seen.update((u,v))
        assert len(extra)==1 or (len(extra)*2==len(a) and len(seen)==len(a))
    t=F(threshold);l,d=lap(a,winner);win=below(l,d,t);assert win==1
    for extra in losers:
        l,d=lap(a,extra);assert below(l,d,t)>=2
    return True

def generate():
    start=time.monotonic();counts={'certified':0,'unresolved':0,'edge':0,'matching':0};out=ROOT/'data/failure_certificates.jsonl'
    unresolved=[]
    with out.open('w') as dest:
      for path in sorted((ROOT/'data').glob('search_d*.jsonl')):
        for line in path.open():
          r=json.loads(line)
          if not r['simple']:continue
          kinds=[k for k in ('naive','corrected') if r.get(k,{}).get('strong_failure')]
          if r.get('matching',{}).get('strong_failure'):kinds.append('matching')
          if not kinds:continue
          a=nx.to_numpy_array(nx.from_graph6_bytes(r['g6'].encode()),dtype=int).tolist();base=base_certificate(a)
          for kind in kinds:
            if kind=='matching':
                hs=matching_candidates(a,base);winner=r['matching']['best'][0]
                hg=max(g for m,g in r['matching']['heuristic']);best=r['matching']['gap_best']
                losers=hs
            else:
                hs=edge_candidates(a,base,kind);winner=[r['best_edges'][0]]
                lookup={tuple(e):g for e,g in zip(r['edges'],r['edge_gaps'])};hg=max(lookup[e] for e in hs);best=r['best_edge_gap'];losers=[[e] for e in hs]
            if best-hg<1e-8:
                unresolved.append([path.name,r['id'],kind,'candidate enclosure touches optimizer']);counts['unresolved']+=1;continue
            threshold=F(round((best+hg)/2*10**10),10**10)
            try:compare(a,winner,losers,threshold)
            except ArithmeticError:
                threshold+=F(1,10**11);compare(a,winner,losers,threshold)
            cert={'source':path.name,'id':r['id'],'g6':r['g6'],'kind':kind,'base':base,'winner':winner,'heuristic_superset':losers,'threshold':ff(threshold)}
            dest.write(json.dumps(cert,separators=(',',':'))+'\n');dest.flush();counts['certified']+=1;counts['matching' if kind=='matching' else 'edge']+=1
        print(path.name,counts,'elapsed',round(time.monotonic()-start,1),flush=True)
    (ROOT/'data/certification_summary.json').write_text(json.dumps({**counts,'elapsed_seconds':time.monotonic()-start,'unresolved_cases':unresolved},indent=2)+'\n')

def verify():
    count=0;start=time.monotonic()
    for line in (ROOT/'data/failure_certificates.jsonl').open():
        c=json.loads(line);a=nx.to_numpy_array(nx.from_graph6_bytes(c['g6'].encode()),dtype=int).tolist();verify_base(a,c['base'])
        hs=matching_candidates(a,c['base']) if c['kind']=='matching' else [[e] for e in edge_candidates(a,c['base'],c['kind'])]
        assert json.loads(json.dumps(hs))==c['heuristic_superset']
        compare(a,c['winner'],c['heuristic_superset'],c['threshold']);count+=1
    print(json.dumps({'verified':count,'elapsed_seconds':time.monotonic()-start}));(ROOT/'data/replay_summary.json').write_text(json.dumps({'verified':count,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args();verify() if args.verify else generate()
