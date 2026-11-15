"""Independent finite audit; standard library only; no submitted code imports."""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt, log, pi, exp
from collections import Counter
import json
from pathlib import Path

OUT = Path('referee_results')
OUT.mkdir(exist_ok=True)
def paths(n):
    for w in product((-1, 1), repeat=n):
        h = [0]
        for v in w: h.append(h[-1] + v)
        yield w, h
def good(h, start, n, a):
    return h[start+n]-h[start] == -a and min(h[start:start+n]) > h[start+n]
def p(s,b):
    return F(comb(s,(s+b)//2), 2**s) if abs(b)<=s and (s+b)%2==0 else F(0)
def f(s,b):
    return F(b,s)*p(s,b) if b>0 else F(0)
def g(s): return F(comb(s-1,(s-1)//2)**2,4**s)
def G(L): return 1+sum((g(s) for s in range(1,L+1)), F(0))
def EV(L): return 1+sum((sum((f(s,b) for b in range(1,s+1)),F(0)) for s in range(1,L+1)),F(0))
def exact_solve(A,b):
    A=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
    n=len(b)
    for j in range(n):
        k=next(k for k in range(j,n) if A[k][j])
        A[j],A[k]=A[k],A[j]
        d=A[j][j]
        A[j][j:]=[v/d for v in A[j][j:]]
        for k in range(j+1,n):
            d=A[k][j]
            if d: A[k][j:]=[x-d*y for x,y in zip(A[k][j:],A[j][j:])]
    x=[F(0)]*n
    for j in range(n-1,-1,-1): x[j]=A[j][-1]-sum(A[j][k]*x[k] for k in range(j+1,n))
    return x

result={}
# Absorbing barrier DP, independent of ballot/reflection formulas.
checks=0
for b in range(1,41):
    alive={0:1}
    for s in range(1,81):
        nxt=Counter(); hits=0
        for h,c in alive.items():
            for u in (-1,1):
                if h+u == -b: hits+=c
                else: nxt[h+u]+=c
        assert F(hits,2**s)==f(s,b)
        assert f(s,b)==(p(s-1,b-1)-p(s-1,b+1))/2
        alive=nxt; checks+=1
result['lemma2_barrier_dp_checks']=checks
mx=F(0)
for s in range(1,501):
    for b in range(1,s+1): mx=max(mx,b*p(s,b))
    assert sum((f(s,b)*p(s,b) for b in range(1,s+1)),F(0))==g(s)
result['max_s_times_f_through_500']=str(mx)
result['lemma3_identity11_times']=500
result['potential']=[dict(L=L,G=float(G(L)),G_over_log=float(G(L))/log(L),last_s_g=float(L*g(L)),target=1/(2*pi)) for L in (10,100,1000,10000)]
# Correct source rounding: floor(lambda sqrt(n)), then add one on wrong parity.
result['local_limit']=[]
for n in (100,1000,10000):
    endpoint=int((-sqrt(n))//1)
    endpoint += (endpoint-n)%2
    a=-endpoint
    result['local_limit'].append(dict(n=n,a=a,nf=float(n*f(n,a)),limit=sqrt(2/pi)*exp(-.5)))

range_rows=[]
for L in range(1,9):
    total=0
    for _,y in paths(L):
        mn=0; rec=[0]
        for t in range(1,L+1):
            if y[t]<mn: rec.append(t); mn=y[t]
        for _,x in paths(L): total+=len({x[t]-y[t] for t in rec})
    er=F(total,4**L)
    assert G(L)*er<=EV(2*L)
    assert float(EV(L))<=1+sqrt(L)
    range_rows.append(dict(L=L,ER=str(er),EV2=str(EV(2*L)),G=str(G(L)),ratio=float(G(L)*er/EV(2*L))))
result['range_exact']=range_rows
# Test restart equivalence and actual no-double-counting pathwise sum.
pairchecks=0
for L in range(1,5):
    for _,y in paths(2*L):
        rec=[True]+[y[t]<min(y[:t]) for t in range(1,2*L+1)]
        for _,x in paths(2*L):
            first={}
            for t in range(L+1):
                if rec[t]: first.setdefault(x[t]-y[t],t)
            visits=[]
            for z,t in first.items():
                for u in range(L+1):
                    shifted=(u==0 or y[t+u]<min(y[t:t+u]))
                    assert rec[t+u]==shifted
                    if rec[t+u] and x[t+u]-y[t+u]==z: visits.append(t+u)
            assert len(visits)==len(set(visits)) and len(visits)<=sum(rec)
            pairchecks+=1
result['record_restart_and_count_path_pairs']=pairchecks

overlaps=0; extensions=0; matrix_checks=0
waiting=[]
for n in range(2,11):
    words={a:[] for a in range(1,n+1)}
    for w,h in paths(n):
        a=-h[-1]
        if a>0 and good(h,0,n,a): words[a].append((w,h))
    for a,wh in words.items():
        if not wh: continue
        for w,h in wh:
            for s in range(1,n):
                hits=0
                for v,z in paths(s):
                    full=h+[h[-1]+k for k in z[1:]]
                    hits+=good(full,s,n,a); extensions+=1
                assert F(hits,2**s)==(f(s,-h[s]) if h[s]<0 else 0)
                overlaps+=1
        # Matching column sums directly from word overlaps.
        for w,h in wh:
            direct=sum((F(1,2**s) for v,_ in wh for s in range(n) if v[:n-s]==w[s:]),F(0))
            formula=1+sum((f(s,-h[s]) for s in range(1,n) if h[s]<0),F(0))
            assert direct==formula; matrix_checks+=1
        if (n,a) not in ((2,2),(3,1),(4,2),(5,1),(6,2),(7,1),(8,2),(9,3),(10,2)): continue
        targets={w for w,_ in wh}
        prefixes=sorted({w[:j] for w in targets for j in range(n)},key=lambda w:(len(w),w))
        index={w:j for j,w in enumerate(prefixes)}
        k=len(prefixes); A=[[F(i==j) for j in range(k)] for i in range(k)]
        for i,w in enumerate(prefixes):
            for bit in (-1,1):
                v=w+(bit,)
                if v in targets: continue
                suffix=max((q for q in prefixes if len(q)<=len(v) and (not q or v[-len(q):]==q)),key=len)
                A[i][index[suffix]]-=F(1,2)
        expectation=exact_solve(A,[1]*k)[0]
        M=[[sum((F(1,2**s) for s in range(n) if v[:n-s]==w[s:]),F(0)) for w,_ in wh] for v,_ in wh]
        matrix_mean=F(2**n,1)/sum(exact_solve(M,[1]*len(wh)))
        assert matrix_mean==expectation
        waiting.append(dict(n=n,a=a,words=len(wh),states=k,ET=str(expectation),decimal=float(expectation),start=float(expectation-n)))
result['overlap_word_shift_cases']=overlaps
result['overlap_extension_paths']=extensions
result['matching_column_checks']=matrix_checks
result['exact_waiting']=waiting

blocks=[]; inclusion_cases=0
for n in range(2,11):
    m=n//2; counts=Counter(); successes=Counter(); nsq=Counter(); right=Counter()
    for w,h in paths(n+m):
        x=h[:m+1]; y=[h[n+s]-h[n] for s in range(m+1)]
        rec=[s for s in range(m+1) if s==0 or y[s]<min(y[:s])]
        r={x[s]-y[s] for s in rec}; B=h[n]-h[m]
        for a in range(1,n+2):
            N=sum(good(h,s,n,a) for s in range(m+1))
            rhs=B in {z-x[-1]-a for z in r}
            assert not N or rhs
            counts[a]+=N; successes[a]+=bool(N); nsq[a]+=N*N; right[a]+=rhs
            inclusion_cases+=1
    D=1+sum((max(f(s,b) for b in range(1,s+1)) for s in range(1,m+1)),F(0))
    er=F(range_rows[m-1]['ER'])
    U=max(p(n-m,b) for b in range(n-m+1))*er
    for a in range(1,n+2):
        en=F(counts[a],2**(n+m)); q=F(successes[a],2**(n+m)); rr=F(right[a],2**(n+m))
        assert en==(m+1)*f(n,a)
        assert en<=D*q and q<=rr<=U
        assert F(nsq[a],2**(n+m))<=(2*D-1)*en
        if f(n,a): blocks.append(dict(n=n,a=a,q=str(q),EN=str(en),lower=str(en/D),inclusion_probability=str(rr),range_upper=str(U)))
result['inclusion_path_endpoint_cases']=inclusion_cases
result['block_checks']=blocks
# Finite analogues of tail bounds: exact unions and independent disjoint blocks.
tails=[]
for n,a,horizon in ((3,1,18),(4,2,18),(5,1,18),(6,2,18)):
    m=n//2; ell=n+m
    q=next(F(b['q']) for b in blocks if b['n']==n and b['a']==a)
    hist=Counter()
    for _,h in paths(horizon):
        t=next((t for t in range(n,horizon+1) if good(h,t-n,n,a)),horizon+1)
        hist[t]+=1
    for t in range(n,horizon+1):
        hit=F(sum(c for u,c in hist.items() if u<=t),2**horizon)
        union=((t-n)//(m+1)+1)*q
        assert hit<=union
        if t%ell==0: assert 1-hit<=(1-q)**(t//ell)
    et=next(F(w['ET']) for w in waiting if w['n']==n and w['a']==a)
    lower=max(F(t)*(1-min(F(1),((t-n)//(m+1)+1)*q)) for t in range(n,100))
    assert lower<=et<=F(ell)/q
    tails.append(dict(n=n,a=a,horizon=horizon,ET=str(et),finite_lower=str(lower),geometric_upper=str(F(ell)/q)))
result['tail_and_expectation_checks']=tails
# Submitted binomial-ratio inequalities, including support endpoints.
ratios=0
for k in range(1,151):
    for j in range(k+1):
        even=float(p(2*k,2*j)/p(2*k,0))
        assert even<=exp(-j*j/(k+j))*(1+1e-14)
        assert exp(-j*j/(k+j))<=exp(-j*j/(2*k))*(1+1e-14)
        odd=float(p(2*k+1,2*j+1)/p(2*k+1,1))
        assert odd<=exp(-j*(j+1)/(k+j+1))*(1+1e-14)
        ratios+=1
result['binomial_ratio_checks']=ratios
source_table={100:179.805,200:358.249,500:893.041,1000:1800.002,2000:3682.022,5000:8549.390,10000:12231.412}
diagnostic=[]
last=None
for n,mean in source_table.items():
    endpoint=int((-sqrt(n))//1);endpoint+=(endpoint-n)%2;a=-endpoint
    row=dict(n=n,a=a,source_mean=mean,exact_reciprocal_probability=float(1/f(n,a)))
    if last: row['recomputed_source_exponent']=log(mean/last[1])/log(n/last[0])
    diagnostic.append(row);last=(n,mean)
result['source_table_diagnostic']=diagnostic
OUT.joinpath('exact.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if not isinstance(v,list)},indent=2),flush=True)
print('All exact assertions passed.',flush=True)
