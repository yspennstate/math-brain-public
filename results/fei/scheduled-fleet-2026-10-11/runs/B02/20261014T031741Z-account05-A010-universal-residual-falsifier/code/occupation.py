from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product,permutations
from math import factorial,prod
import json,time,sys
OUT=Path(__file__).resolve().parents[1]/'out'

def matchings(edges,A):
    inside=[e for e in edges if all(A>>v&1 for v in e)]; out=[]
    for mask in range(1<<len(inside)):
        M=[e for j,e in enumerate(inside) if mask>>j&1]; vertices=[v for e in M for v in e]
        if len(set(vertices))!=len(vertices): continue
        if any(all(v not in vertices for v in e) for e in inside): continue
        out.append(M)
    return out

def evaluate(edges,lam,A,M,n):
    owned={v:e for e in M for v in e}; U=[u for u in range(n) if A>>u&1 and u not in owned]; pol={(0,)*n:Q(1)}
    for u in U:
        terms=[]
        for e in edges:
            if u not in e: continue
            v=e[0] if e[1]==u else e[1]
            assert v not in U
            terms.append((v,lam[e]/(8 if v in owned else 32)))
        new={}
        for h,c in pol.items():
            for v,w in terms:
                h2=list(h)
                if v in owned: h2[v]+=1
                h2=tuple(h2); new[h2]=new.get(h2,Q(0))+c*w
        pol=new
    moment=lower=Q(0)
    for h,c in pol.items():
        j=Q(1); k=d=0
        for v,w in M:
            ce=h[v]+h[w]; k+=ce; d+=ce>0
            j*=Q(factorial(h[v])*factorial(h[w]),(ce+1)**2*(ce+2))
            # Distinct beta/exponential/uniform moment expression.
            moment_edge=Q(factorial(h[v])*factorial(h[w]),ce+1)*Q(2,(ce+1)*(ce+2))/2
            assert moment_edge==Q(factorial(h[v])*factorial(h[w]),(ce+1)**2*(ce+2))
        moment+=c*j; lower+=c*Q(2)**(k-d)/Q(6)**k
    polynomial_mass=prod(lam[e]/24 for e in M)*moment
    lower_mass=prod(lam[e]/48 for e in M)*lower
    assert polynomial_mass>=lower_mass
    choices=[]
    for u in U:
        choices.append([(e,e[0] if e[1]==u else e[1]) for e in edges if u in e])
    direct=Q(0); events=0; seen=set()
    for nu in product(*choices):
        child_groups={v:[] for e in M for v in e}; roots=list(M); singleton=[]
        for u,(e,v) in zip(U,nu):
            singleton.append((u,e,v))
            if v in owned: child_groups[v].append(e)
            else: roots.append(e)
        # Actual label sequences at repeated attachment slots, not a factorial shortcut.
        perms=[list(permutations(child_groups[v])) for v in sorted(child_groups)]
        for seqs in product(*perms):
            trace=(tuple(sorted(roots)),tuple((v,s) for v,s in zip(sorted(child_groups),seqs)))
            assert trace not in seen
            seen.add(trace)
            q=Q(1)
            for e in M:
                ce=sum(len(child_groups[v]) for v in e)
                q*=lam[e]*Q(1,4)*Q(1,6)*Q(1,(ce+1)*(ce+2))*Q(1,ce+1)
            for u,e,v in singleton:
                q*=lam[e]*Q(1,4)*Q(1,2)
                if v not in owned: q*=Q(1,4)
            direct+=q; events+=1
    assert direct==polynomial_mass,(edges,A,M,direct,polynomial_mass)
    return direct,events,len(pol)

if __name__=='__main__':
    pilot='pilot' in sys.argv; n=3 if pilot else 4; start=time.monotonic(); all_edges=list(combinations(range(n),2)); rows=[]; cases=events=terms=0
    for G in range(1,1<<len(all_edges)):
        edges=[e for i,e in enumerate(all_edges) if G>>i&1]; degree={v:sum(v in e for e in edges) for v in range(n)}
        for name,lam in [('uniform',{e:Q(1,max(degree.values())) for e in edges}),('local',{e:Q(1,degree[e[0]]+degree[e[1]]) for e in edges})]:
            assert all(sum(lam[e] for e in edges if v in e)<=1 for v in range(n))
            D=prod(1+lam[e]/4 for e in edges)-1; total=Q(0)
            for A in range(1,1<<n):
                if any(not degree[v] for v in range(n) if A>>v&1): continue
                mass=Q(0)
                for M in matchings(edges,A):
                    assert time.monotonic()-start<(60 if pilot else 300)
                    value,count,size=evaluate(edges,lam,A,M,n); mass+=value; events+=count; terms+=size; cases+=1
                assert mass>0; total+=mass/D
            assert total<=1
            rows.append({'graph':G,'vector':name,'total_output_subprobability':str(total)})
        (OUT/'occupation_checkpoint.json').write_text(json.dumps({'graphs':G,'matching_cases':cases,'actual_events':events}))
    for a in range(65):
        for b in range(65-a):
            c=a+b; j=Q(factorial(a)*factorial(b),(c+1)**2*(c+2))
            assert j>=Q(1,2)*Q(1,6)**c*Q(2)**max(c-1,0)
    result={'n':n,'graphs':len(rows)//2,'rational_vectors':len(rows),'matching_cases':cases,'actual_events':events,'occupation_monomials':terms,'rows':rows,'elapsed_seconds':time.monotonic()-start,'verdict':'Exact occupation equality, collision bound, shared endpoint moments, coverage and subprobability PASS'}
    (OUT/('occupation_pilot.json' if pilot else 'occupation.json')).write_text(json.dumps(result,indent=2)); print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
