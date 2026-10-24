"""Complete chronological star coefficients and joint-edge rational certificates."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product,permutations
from math import factorial,comb
from time import perf_counter
import json,sys
BASE=Path(__file__).resolve().parents[1]; checks=0
def ck(ok):
    global checks
    checks+=1
    if not ok: raise AssertionError(checks)
def mul(it):
    z=Q(1)
    for x in it:z*=x
    return z
def save(name,obj): (BASE/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fwht(a):
    a=list(a); step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for k in range(i,i+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    return a
def maximal(A,E):
    J=[i for i,e in enumerate(E) if set(e)<=set(A)]
    for mask in range(1<<len(J)):
        M=tuple(J[k] for k in range(len(J)) if mask>>k&1); endpoints=[v for i in M for v in E[i]]
        if len(set(endpoints))!=len(endpoints):continue
        if any(u not in endpoints and v not in endpoints for u,v in (E[i] for i in J)):continue
        yield M
def traces(A,E):
    ids={frozenset(e):i for i,e in enumerate(E)}; coeff={}; seenkeys=set()
    for M in maximal(A,E):
        matching={v:i for i in M for v in E[i]}; U=tuple(v for v in A if v not in matching)
        choices=[tuple(v if u==a else a for a,v in E if u in (a,v)) for u in U]
        for nu in product(*choices):
            own={i:tuple(E[i]) for i in M}; roots=set(M); groups={}
            for u,v in zip(U,nu):
                i=ids[frozenset((u,v))];ck(i not in own);own[i]=(u,)
                if v in matching:groups.setdefault((matching[v],v),[]).append(i)
                else:roots.add(i)
            slots=[(i,v) for i in sorted(own) for v in sorted(own[i])]
            for order in product(*(tuple(permutations(groups.get(k,[]))) for k in slots)):
                draw=dict(zip(slots,order)); todo=list(sorted(roots)); visits=[]; prob=Q(1,4**len(roots)); used=set()
                while todo:
                    i=todo.pop(0);ck(i not in used);used.add(i);B=own[i];s=len(B)
                    children=tuple((v,j) for v in sorted(B) for j in draw[i,v]);c=len(children)
                    prob*=Q(1,s*(s+1)*comb(2,s)*(c+1)*(c+2)*comb(s+c-1,c))
                    visits.append((i,B,children));todo.extend(j for v,j in children)
                ck(used==set(own))
                key=(tuple(sorted(roots)),tuple(visits));ck(key not in seenkeys);seenkeys.add(key)
                mask=sum(1<<i for i in used);coeff[mask]=coeff.get(mask,Q(0))+prob
    return coeff,len(seenkeys)
def occupation_mass(A,E,w):
    ids={frozenset(e):i for i,e in enumerate(E)}; total=Q(0)
    for M in maximal(A,E):
        V=tuple(sorted(v for i in M for v in E[i])); matched=set(V);pos={v:k for k,v in enumerate(V)}
        U=tuple(v for v in A if v not in matched);poly={(0,)*len(V):Q(1)}
        for u in U:
            terms={}
            for a,b in E:
                if u not in (a,b):continue
                v=b if u==a else a;i=ids[frozenset((u,v))];key=[0]*len(V)
                if v in matched:key[pos[v]]=1; val=w[i]/8
                else:val=w[i]/32
                terms[tuple(key)]=terms.get(tuple(key),Q(0))+val
            nxt={}
            for h,p in poly.items():
                for k,q in terms.items():
                    key=tuple(a+b for a,b in zip(h,k));nxt[key]=nxt.get(key,Q(0))+p*q
            poly=nxt
        J=Q(0)
        for h,p in poly.items():
            for i in M:
                a,b=(h[pos[v]] for v in E[i]);c=a+b;p*=Q(factorial(a)*factorial(b),(c+1)**2*(c+2))
            J+=p
        total+=mul(w[i]/24 for i in M)*J
    return total
def evaluate(coeff,w):return sum((k*mul(w[i] for i in range(len(w)) if mask>>i&1) for mask,k in coeff.items()),Q(0))
def scalar_review():
    count=0
    for a in range(33):
        for b in range(33):
            c=a+b; exact=Q(factorial(a)*factorial(b),(c+1)**2*(c+2))
            bound=Q(2**max(c-1,0),2*6**c);ck(exact>=bound)
            # Shared endpoint moments, not independent endpoint TB draws.
            moment=Q(1,c+1)*Q(2,(c+1)*(c+2))*factorial(a)*factorial(b)/2
            ck(moment==exact);count+=1
    save('A008_REVIEW_CHECK.json',{'status':'PASS','integer_pairs':count,'claim':'A008-MATCHING-OCCUPATION-MASS-COLLISION-CREDIT@1',
        'method':'independent chronological coefficient pushforward versus occupation convolution; rational shared-endpoint moments and collision credit'})
def slice_certificate(P,coeff,w,e,E):
    n=len(E);d=mul(1+w[i]/4 for i in range(n) if i!=e)-1
    L=Q(min(1-sum(w[i] for i in range(n) if i!=e and u in E[i]) for u in E[e]));ck(L>0)
    if n==1:
        for A,C in coeff.items():ck(evaluate(C,w)/(w[e]/4)==evaluate(C,[L])/(L/4))
        return {'edge':e,'kind':'ONE_GATE_CONSTANT','beta':'any positive <= '+str(L),'gap_bits':'0'}
    j=(1+d)/4;R=j*L/(d+j*L);rows=[]
    for A,p in P.items():
        C=coeff[A];a=Q(0);b=Q(0)
        for mask,k in C.items():
            value=k*mul(w[i] for i in range(n) if i!=e and mask>>i&1)
            if mask>>e&1:b+=value
            else:a+=value
        q0=a/d;q1=b/j;z=q1-q0;rows.append((p,q0,z))
        for frac in [Q(1,3),Q(2,3),Q(1)]:
            beta=L*frac;r=j*beta/(d+j*beta);ww=list(w);ww[e]=beta
            ck(evaluate(C,ww)/(d+j*beta)==q0+z*r)
    grouped={}
    for p,q0,z in rows:grouped[q0,z]=grouped.get((q0,z),Q(0))+p
    grouped_rows=[(p,q0,z) for (q0,z),p in grouped.items()]
    ck(sum(p for p,q0,z in grouped_rows)==sum(P.values()))
    def grad(r):return -sum((p*z/(q0+z*r) for p,q0,z in grouped_rows),Q(0))
    mu=sum((p*z*z/max(q0,q0+z*R)**2 for p,q0,z in rows),Q(0))
    if not mu:return {'edge':e,'kind':'CONSTANT','beta':str(w[e]),'gap_bits':'0'}
    I=sum(p*A.bit_count() for A,p in P.items());eps=I/Q(10**9)
    gR=grad(R)
    finite0=all(q0>0 for p,q0,z in rows)
    if gR<=0:
        ck(gR<=0);return {'edge':e,'kind':'UPPER_BOUNDARY','beta':str(L),'r':str(R),'gradient':str(gR),'gap_bits':'0'}
    lower=finite0 and grad(Q(0))>=0
    lo=Q(0);hi=R;iterations=0
    while True:
        t=(lo+hi)/2;g=grad(t)
        gap=min(g*g/mu,2*max(g*t,-g*(R-t),Q(0)))
        ck(gap>=0)
        if gap<=eps:break
        if lower:hi=t
        elif g<0:lo=t
        else:hi=t
        iterations+=1
        if iterations>80:raise RuntimeError('frozen 80 rational bisections')
    beta=d*t/(j*(1-t));ck(0<beta<=L);ck(gap<=I/Q(10**9))
    # Original reference incidence is still feasible after the proposed global coordinate update.
    ww=list(w);ww[e]=beta;ck(all(sum(x for x,edge in zip(ww,E) if u in edge)<=1 for u in set(v for edge in E for v in edge)))
    if not lower:
        ck((not finite0 or grad(lo)<=0) and grad(hi)>=0)
    return {'edge':e,'kind':'ZERO_BOUNDARY_INFIMUM' if lower else 'UNIQUE_INTERIOR',
        'beta':str(beta),'r_bracket':[str(lo),str(hi)],'r_test':str(t),'mu':str(mu),'gradient':str(g),
        'gap_bits':str(gap),'I':str(I),'bisections':iterations}
def main():
    start=perf_counter();n=3 if '--pilot' in sys.argv else 4; allE=list(combinations(range(n),2));tables=[];traces_count=0;slices=0;kinds={}
    for mask in range(1,1<<len(allE)):
        E=tuple(e for i,e in enumerate(allE) if mask>>i&1);deg=[sum(v in e for e in E) for v in range(n)];Delta=max(deg)
        w=tuple(Q(1,2*Delta) for e in E);covered={v for v in range(n) if deg[v]}
        values=[1 if any(all(x>>v&1 for v in e) for e in E) else -1 for x in range(1<<n)];W=fwht(values)
        ck(sum(a*a for a in W)==1<<(2*n))
        edges_count=sum(values[x]!=values[x^(1<<v)] for v in range(n) for x in range(1<<n) if not x>>v&1)
        ck(sum(A.bit_count()*W[A]**2 for A in range(1<<n))==edges_count*(1<<(n+1)))
        coeff={};P={};D=mul(1+x/4 for x in w)-1;totalmass=Q(0)
        for A in range(1,1<<n):
            Cset=tuple(v for v in range(n) if A>>v&1)
            if not set(Cset)<=covered:ck(W[A]==0);continue
            C,count=traces(Cset,E);traces_count+=count;coeff[A]=C
            numeric=evaluate(C,w);ck(numeric==occupation_mass(Cset,E,w));ck(numeric>0);totalmass+=numeric/D
            if W[A]:P[A]=Q(W[A]**2,1<<(2*n))
        ck(totalmass<=1)
        v=sum(P.values());root_law={T:mul(w[i]/4 for i in range(len(E)) if T>>i&1)/D for T in range(1,1<<len(E))}
        ck(sum(root_law.values())==1)
        Qbase={A:evaluate(coeff[A],w)/D for A in P}
        h={T:sum((p*coeff[A].get(T,Q(0))*4**T.bit_count()/Qbase[A] for A,p in P.items()),Q(0)) for T in root_law}
        ck(sum(root_law[T]*h[T] for T in root_law)==v)
        Gamma=max(h.values())-v;ck(Gamma>=0)
        for A,p in P.items():ck(sum(root_law[T]*coeff[A].get(T,Q(0))*4**T.bit_count() for T in root_law)==Qbase[A])
        I=sum(p*A.bit_count() for A,p in P.items())
        jointgap={'Gamma_natural':str(Gamma),'global_joint_bit_gap_bound':str(2*Gamma),'global_joint_bit_gap_over_I':str(2*Gamma/I),
            'root_law':{str(T):str(root_law[T]) for T in root_law},'h':{str(T):str(h[T]) for T in h},
            'scope':'same complete maximal-matching star family, all feasible global weights and changing actual posterior; relaxation can be loose'}
        results=[]
        for e in range(len(E)):
            r=slice_certificate(P,coeff,w,e,E);slices+=1;kinds[r['kind']]=kinds.get(r['kind'],0)+1;results.append(r)
        row={'edges':E,'weights':list(map(str,w)),'positive_spectral_sets':len(P),'global_joint_gap':jointgap,'slices':results};tables.append(row)
        save('PARTIAL_'+str(n)+'.json',{'tables_done':len(tables),'slices':slices,'last_table':row})
        if perf_counter()-start>(55 if n==3 else 295):raise RuntimeError('frozen runtime guard')
    scalar_review();elapsed=perf_counter()-start;ck(elapsed<(60 if n==3 else 300))
    summary={'status':'PASS','helper_version':'A006-joint-edge-root-marginal-v1.2','n':n,'tables':len(tables),'actual_traces':traces_count,
        'joint_slices':slices,'slice_kinds':kinds,'assertions':checks,'seconds':elapsed,'bit_gap_bound':'I/10^9 for each positive rational approximate slice optimum'}
    save('CHECK_'+str(n)+'.json',{'summary':summary,'tables':tables});save('PILOT_SUMMARY.json' if n==3 else 'CHECK_SUMMARY.json',summary)
    print(json.dumps(summary))
if __name__=='__main__':main()
