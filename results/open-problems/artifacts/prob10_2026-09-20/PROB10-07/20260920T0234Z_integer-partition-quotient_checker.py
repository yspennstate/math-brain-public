#!/usr/bin/env python3
# PROB10-07 production exact checker: integer-partition quotient for K_{m,n}, m=10..30.
# Standard library only. All theorem-sign tests use exact integer/Fraction arithmetic.

from collections import Counter, defaultdict
from fractions import Fraction
from math import comb, factorial
import hashlib, json

EXPECTED = {
6: {'a':[1,57,1340,14850,77760,155520],'b':[32,667,7270,42930,129600,155520],'c':[16,239,1822,6912,10368,0],'l':[243,2907,20520,83970,181440,155520],'d':[351,3751,23832,89154,181440,155520]},
7: {'a':[1,120,5306,109200,1143240,5927040,12101040],'b':[64,2404,46016,491280,2960160,9384480,12101040],'c':[32,878,12320,93360,364560,576240,0],'l':[729,14648,175226,1276560,5517960,12841920,12101040],'d':[1134,20368,219286,1452960,5806080,12841920,12101040]},
8: {'a':[1,247,19530,689892,12636120,125314560,639959040,1321205760],'b':[128,8325,263718,4666452,48588120,295626240,970260480,1321205760],'c':[64,3069,73206,967890,7240320,28753920,47185920,0],'l':[2187,70429,1339506,15839712,117441240,527869440,1300561920,1321205760],'d':[3645,104923,1796766,19300032,131449560,551462400,1300561920,1321205760]},
9: {'a':[1,502,68592,3951024,117285840,1953110880,18473676480,92853371520,192849310080],'b':[256,28058,1412088,39138960,648426240,6592350240,40298186880,135708773760,192849310080],'c':[128,10384,400064,8542380,107301600,791169120,3174474240,5356925280,0],'l':[6561,327606,9479280,171397296,1997407440,14964536160,69265264320,178564176000,192849310080],'d':[11664,520288,13559090,222693156,2378907720,16518705840,71943726960,178564176000,192849310080]},
}

def iparts(n,maxpart=None):
    if n==0:
        yield (); return
    if maxpart is None or maxpart>n: maxpart=n
    for first in range(maxpart,0,-1):
        for rest in iparts(n-first,first): yield (first,)+rest

def merge_state(lam,chosen_counts):
    rem=list(lam); total=0
    for s,r in chosen_counts.items():
        total += s*r
        for _ in range(r): rem.remove(s)
    rem.append(total); rem.sort(reverse=True); return tuple(rem)

def build_quotient(m):
    P=list(iparts(m)); idx={p:i for i,p in enumerate(P)}
    rows=[defaultdict(int) for _ in P]; q=m+1
    for i,lam in enumerate(P):
        rows[i][i]=q
        cnt=Counter(lam); sizes=sorted(cnt); choice={}
        def rec(pos,hits,mult):
            if pos==len(sizes):
                if hits>=2: rows[i][idx[merge_state(lam,choice)]] += mult
                return
            s=sizes[pos]; c=cnt[s]
            for r in range(c+1):
                if r: choice[s]=r
                elif s in choice: del choice[s]
                rec(pos+1,hits+r,mult*comb(c,r)*(s**r))
            if s in choice: del choice[s]
        rec(0,0,1)
        assert sum(rows[i].values()) == __import__('math').prod(1+s for s in lam)
        for j,w in rows[i].items():
            if j!=i: assert len(P[j])<len(lam) and w>0
    N=[]
    for i,row in enumerate(rows):
        nr=defaultdict(int,row); nr[i]-=q
        if nr[i]==0: del nr[i]
        N.append(dict(nr))
    return P,idx,N

def state_oneblock(m,k):
    return tuple(sorted(([k] if k>=2 else [])+[1]*(m-k if k>=2 else m),reverse=True))

def initial_vectors(m,idx):
    z=defaultdict(int); e=defaultdict(int); r=defaultdict(int); l=defaultdict(int); d=defaultdict(int)
    z[idx[(1,)*m]]=1
    for k in range(1,m+1): e[idx[state_oneblock(m,k)]] += comb(m-1,k-1)
    for k in range(2,m+1): r[idx[state_oneblock(m,k)]] += comb(m-2,k-2)
    for k in range(1,m+1): l[idx[state_oneblock(m,k)]] += comb(m-1,k-1)*(2**(k-1))
    for k in range(2,m+1): d[idx[state_oneblock(m,k)]] += comb(m-2,k-2)*(2**(k-2))
    for s in range(1,m):
        countS=comb(m-2,s-1); outside=m-s-1
        for u in range(1,outside+2):
            choose_out=comb(outside,u-1)
            parts=[s,u]+[1]*(m-s-u); parts.sort(reverse=True)
            d[idx[tuple(parts)]] += countS*choose_out
            d[idx[state_oneblock(m,s+u)]] += countS*s*choose_out
    assert sum(e.values())==2**(m-1)
    assert sum(r.values())==2**(m-2)
    assert sum(l.values())==3**(m-1)
    return [dict(x) for x in (z,e,r,l,d)]

def row_apply(v,A):
    out=defaultdict(int)
    for i,vi in v.items():
        for j,a in A[i].items(): out[j]+=vi*a
    return {j:x for j,x in out.items() if x}

def coeffs(v,N,m):
    ans=[]; cur=v
    for _ in range(m):
        ans.append(sum(cur.values())); cur=row_apply(cur,N)
    assert not cur; return ans

def padd(a,b):
    c=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pscale(a,s): return [x*s for x in a]
def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def psub(a,b): return padd(a,pscale(b,Fraction(-1)))
def binom_poly(shift,j):
    p=[Fraction(1)]
    for k in range(j): p=pmul(p,[Fraction(shift-k),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))
def normalized_count(vec,q,shift,prefix):
    p=[Fraction(0)]
    for j,a in enumerate(vec): p=padd(p,pscale(binom_poly(shift,j),Fraction(a,q**(prefix+j))))
    return p

def pshift(p,c):
    out=[Fraction(0)]
    for i,a in enumerate(p):
        term=[Fraction(0)]*(i+1)
        for j in range(i+1): term[j]=a*comb(i,j)*(Fraction(c)**(i-j))
        out=padd(out,term)
    return out

def pdiv_linear_nminus1(p):
    high=list(reversed(p)); qh=[high[0]]
    for a in high[1:-1]: qh.append(a+qh[-1])
    assert high[-1]+qh[-1]==0
    return list(reversed(qh))
def rayleigh(vecs,m):
    a,b,c,l,d=vecs; q=m+1
    z=normalized_count(a,q,0,0); e=normalized_count(b,q,-1,1); rr=normalized_count(c,q,-1,1)
    ll=normalized_count(l,q,-2,2); dd=normalized_count(d,q,-2,2)
    return {'R':psub(pmul(e,e),pmul(z,rr)),'L':psub(pmul(e,e),pmul(z,ll)),'D':psub(pmul(e,e),pmul(z,dd))}
def canon_frac_list(p): return [[x.numerator,x.denominator] for x in p]

print('PROB10-07 integer-partition quotient exact checker')
print('theorem_range m=10..30, n>=1; n=1 tree equality, n>=2 strict')
for m in range(6,10):
    P,idx,N=build_quotient(m); vecs=[coeffs(v,N,m) for v in initial_vectors(m,idx)]
    assert dict(zip(('a','b','c','l','d'),vecs))==EXPECTED[m]
    print('regression_m',m,'p(m)=',len(P),'MATCH_ARCHIVED_BELL_VECTORS')
all_digest=[]; raw_failure=None
for m in range(10,31):
    P,idx,N=build_quotient(m); vecs=[coeffs(v,N,m) for v in initial_vectors(m,idx)]; rays=rayleigh(vecs,m)
    assert sum(rays['R'])==0
    shifted={'R':pshift(pdiv_linear_nminus1(rays['R']),2),'L':pshift(rays['L'],2),'D':pshift(rays['D'],2)}
    for key,p in shifted.items(): assert all(x>0 for x in p),(m,key,p)
    if raw_failure is None and any(x<=0 for x in rays['D']): raw_failure=(m,[(i,x) for i,x in enumerate(rays['D']) if x<=0])
    payload={'m':m,'states':len(P),'R':canon_frac_list(shifted['R']),'L':canon_frac_list(shifted['L']),'D':canon_frac_list(shifted['D'])}
    digest=hashlib.sha256(json.dumps(payload,separators=(',',':'),sort_keys=True).encode()).hexdigest(); all_digest.append(digest)
    print('m',m,'states',len(P),'degrees_shifted',{k:len(v)-1 for k,v in shifted.items()},'min_coefficients',{k:str(min(v)) for k,v in shifted.items()},'sha256',digest)
mfail,bad=raw_failure
print('first_unshifted_D_nonpositive_width',mfail)
print('unshifted_D_nonpositive_terms',[(i,str(x)) for i,x in bad])
assert mfail==15
assert bad[0][0]==0
assert bad[0][1]==Fraction(-126638194577404627495822599,316912650057057350374175801344)
print('coefficient_digest_master',hashlib.sha256(('\n'.join(all_digest)).encode()).hexdigest())
print('PROB10_07_INTEGER_PARTITION_QUOTIENT_10_30_EXACT_PASS')
