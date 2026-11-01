#!/usr/bin/env python3
# PROB10-07 exact checker: uniform-all-forests Rayleigh for K_{m,n}, m=6,7,8,9.
# Standard library only. All theorem comparisons use exact integer/Fraction arithmetic.

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

EXPECTED = {
6: {
 'states':203, 'nnz':1756,
 'a':[1,57,1340,14850,77760,155520],
 'b':[32,667,7270,42930,129600,155520],
 'c':[16,239,1822,6912,10368,0],
 'l':[243,2907,20520,83970,181440,155520],
 'd':[351,3751,23832,89154,181440,155520],
 'R':(1,13841287201,True,[1679616,21835008,129913632,468992592,1144906353,1978618590,2429369378,2034079416,1042490541,246086714]),
 'L':(20,13841287201,False,[3032640,36325584,194183460,605408481,1204568240,1566902294,1302024828,632416601,137632592]),
 'D':(4,13841287201,False,[1446336,18168624,100118700,314752167,613963411,755493426,567551238,234872887,40034619]),
},
7: {
 'states':877, 'nnz':10951,
 'a':[1,120,5306,109200,1143240,5927040,12101040],
 'b':[64,2404,46016,491280,2960160,9384480,12101040],
 'c':[32,878,12320,93360,364560,576240,0],
 'l':[729,14648,175226,1276560,5517960,12841920,12101040],
 'd':[1134,20368,219286,1452960,5806080,12841920,12101040],
 'R':(1,4398046511104,True,[282475249,4283247143,30206380750,131615737050,396563703249,873648357015,1443108801184,1789481315000,1627415091856,1027152457328,401814004096,73283733248]),
 'L':(3,2199023255552,False,[2311685201,32711716205,211647333660,825104648130,2147801056701,3903147258213,5018049281150,4509655115180,2713232922264,987715201024,165380565376]),
 'D':(1,2199023255552,False,[478478483,7084234535,47428441620,188701096710,492769643223,879407921679,1081217795450,898754582660,479081965512,145714204672,18662128768]),
},
8: {
 'states':4140, 'nnz':72911,
 'a':[1,247,19530,689892,12636120,125314560,639959040,1321205760],
 'b':[128,8325,263718,4666452,48588120,295626240,970260480,1321205760],
 'c':[64,3069,73206,967890,7240320,28753920,47185920,0],
 'l':[2187,70429,1339506,15839712,117441240,527869440,1300561920,1321205760],
 'd':[3645,104923,1796766,19300032,131449560,551462400,1300561920,1321205760],
 'R':(1,1853020188851841,True,[68719476736,1187558457344,9647754838016,49001616375808,174472740777984,462236138596992,941602987975793,1497341979911038,1859356247827177,1776792045505778,1264746910035771,631820836777410,197559574075755,29080347734862]),
 'L':(14,1853020188851841,False,[314606354432,5119684902912,38683227455488,179566394941440,570716118643008,1309242248425845,2224280006477269,2821525521192753,2654034679914833,1806616089745407,845378078465439,244360468014939,33026941317627]),
 'D':(2,1853020188851841,False,[114890375168,1950905008128,15264153862144,72691739320320,234344184906432,537781081341195,898594800223864,1097989949633559,969407162287952,599276834446833,243775279071864,57569408844525,5757517345536]),
},
9: {
 'states':21147, 'nnz':515354,
 'a':[1,502,68592,3951024,117285840,1953110880,18473676480,92853371520,192849310080],
 'b':[256,28058,1412088,39138960,648426240,6592350240,40298186880,135708773760,192849310080],
 'c':[128,10384,400064,8542380,107301600,791169120,3174474240,5356925280,0],
 'l':[6561,327606,9479280,171397296,1997407440,14964536160,69265264320,178564176000,192849310080],
 'd':[11664,520288,13559090,222693156,2378907720,16518705840,71943726960,178564176000,192849310080],
 'R':(1,1000000000000000000,True,[22876792454961,443131942738689,4066556450845077,23526970688552373,96314138089029819,296656917253071291,712767298680990711,1364203637931899799,2100356031462548184,2601199753751557896,2565981996649099952,1974338041776594928,1142954943407150336,468300883004973824,121047962761922560,14842987356569600]),
 'L':(1,125000000000000000,False,[231874649450901,4258399328588097,36699675397467453,196836455916904797,734429588825842875,2017769583813792291,4211985522010039839,6790330089810892911,8500758651232594292,8228789623349101632,6066794220617920608,3305596317544392592,1259177855370517632,300380168352065280,33883842580428800]),
 'D':(1,250000000000000000,False,[18922778944227,361645791287319,3225577371485931,17786135621987019,67686101996730525,187860400387287957,391609795225341753,621729004137641097,753591412454561884,691668268385981264,470966780396175616,229053057568759984,74333985864107264,14097644458850560,1123485160857600]),
},
}

def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b:b[0]))

def partitions(seq):
    if not seq:
        yield ()
        return
    x=seq[0]
    for p in partitions(seq[1:]):
        yield canon(((x,),)+p)
        for i in range(len(p)):
            q=[tuple(b) for b in p]
            q[i]=tuple(sorted(q[i]+(x,)))
            yield canon(tuple(q))

def build(m):
    P=sorted(set(partitions(tuple(range(m)))), key=lambda p:(-len(p),p))
    idx={p:i for i,p in enumerate(P)}
    M=[defaultdict(int) for _ in P]
    E0=[defaultdict(int) for _ in P]
    E1=[defaultdict(int) for _ in P]
    E01=[defaultdict(int) for _ in P]
    def legal(p,S):
        ss=set(S)
        return all(sum(x in ss for x in b)<=1 for b in p)
    def nxt(p,S):
        ss=set(S)
        if len(ss)<=1:
            return p
        hit=[i for i,b in enumerate(p) if any(x in ss for x in b)]
        merged=tuple(sorted(x for i in hit for x in p[i]))
        return canon([p[i] for i in range(len(p)) if i not in hit]+[merged])
    for i,p in enumerate(P):
        for r in range(m+1):
            for S in combinations(range(m),r):
                if not legal(p,S):
                    continue
                j=idx[nxt(p,S)]
                M[i][j]+=1
                if 0 in S: E0[i][j]+=1
                if 1 in S: E1[i][j]+=1
                if 0 in S and 1 in S: E01[i][j]+=1
    q=m+1
    N=[defaultdict(int) for _ in P]
    for i,row in enumerate(M):
        assert row.get(i,0)==q
        for j,val in row.items():
            w=val-(q if i==j else 0)
            if w:
                assert len(P[j]) < len(P[i])
                N[i][j]=w
    return P,M,N,E0,E1,E01

def row_apply(v,A):
    out=defaultdict(int)
    for i,vi in v.items():
        for j,a in A[i].items():
            out[j]+=vi*a
    return {j:x for j,x in out.items() if x}

def coeffs(v,N,m):
    ans=[]
    cur=v
    for _ in range(m):
        ans.append(sum(cur.values()))
        cur=row_apply(cur,N)
    assert not cur
    return ans

# polynomials are low-to-high Fraction coefficients in n
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
def peval(a,x):
    s=Fraction(0)
    for c in reversed(a): s=s*x+c
    return s

def binom_poly(shift,j):
    p=[Fraction(1)]
    for k in range(j):
        p=pmul(p,[Fraction(shift-k),Fraction(1)])
    return pscale(p,Fraction(1,factorial(j)))
def normalized_count(vec,q,shift,prefix):
    p=[Fraction(0)]
    for j,a in enumerate(vec):
        term=pscale(binom_poly(shift,j),Fraction(a,q**(prefix+j)))
        p=padd(p,term)
    return p

def expected_ray(spec):
    scalar,den,has_nm1,high=spec
    p=[Fraction(x*scalar,den) for x in reversed(high)]
    if has_nm1: p=pmul(p,[Fraction(-1),Fraction(1)])
    return p

def counts_at(vecs,m,n):
    q=m+1
    a,b,c,l,d=vecs
    Z=sum(a[j]*comb(n,j)*q**(n-j) for j in range(m) if j<=n)
    E=sum(b[j]*comb(n-1,j)*q**(n-1-j) for j in range(m) if j<=n-1)
    R=sum(c[j]*comb(n-1,j)*q**(n-1-j) for j in range(m) if j<=n-1)
    if n>=2:
        L=sum(l[j]*comb(n-2,j)*q**(n-2-j) for j in range(m) if j<=n-2)
        D=sum(d[j]*comb(n-2,j)*q**(n-2-j) for j in range(m) if j<=n-2)
    else: L=D=None
    return Z,E,R,L,D

def is_forest(vcount,edges,mask):
    parent=list(range(vcount)); rank=[0]*vcount
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1 and not union(u,v): return False
    return True

def brute(m,n):
    edges=[(i,m+j) for j in range(n) for i in range(m)]
    e=0; fr=1; fl=m; fd=m+1
    Z=E=R=L=D=0
    for mask in range(1<<len(edges)):
        if not is_forest(m+n,edges,mask): continue
        Z+=1
        if mask&1: E+=1
        if (mask&1) and ((mask>>fr)&1): R+=1
        if (mask&1) and ((mask>>fl)&1): L+=1
        if (mask&1) and ((mask>>fd)&1): D+=1
    return Z,E,R,L,D

for m in (6,7,8,9):
    P,M,N,E0,E1,E01=build(m)
    exp=EXPECTED[m]
    assert len(P)==exp['states']
    assert sum(len(row) for row in M)==exp['nnz']
    v={0:1}
    a=coeffs(v,N,m)
    b=coeffs(row_apply(v,E0),N,m)
    c=coeffs(row_apply(v,E01),N,m)
    l=coeffs(row_apply(row_apply(v,E0),E0),N,m)
    d=coeffs(row_apply(row_apply(v,E0),E1),N,m)
    vecs=(a,b,c,l,d)
    assert a==exp['a'] and b==exp['b'] and c==exp['c'] and l==exp['l'] and d==exp['d']
    q=m+1
    z=normalized_count(a,q,0,0)
    e=normalized_count(b,q,-1,1)
    r=normalized_count(c,q,-1,1)
    ll=normalized_count(l,q,-2,2)
    dd=normalized_count(d,q,-2,2)
    ray={'R':psub(pmul(e,e),pmul(z,r)),
         'L':psub(pmul(e,e),pmul(z,ll)),
         'D':psub(pmul(e,e),pmul(z,dd))}
    for key in ('R','L','D'):
        want=expected_ray(exp[key])
        assert ray[key]==want
        scalar,den,has_nm1,high=exp[key]
        assert scalar>0 and den>0 and all(x>0 for x in high)
        if has_nm1:
            assert peval(ray[key],1)==0
            assert all(peval(ray[key],n)>0 for n in range(2,25))
        else:
            assert all(peval(ray[key],n)>0 for n in range(1,25))
    # Independent direct enumeration of original forest model at n=2.
    direct=brute(m,2)
    transfer=counts_at(vecs,m,2)
    assert direct==transfer
    Z,E,R,L,D=direct
    assert E*E-Z*R>0 and E*E-Z*L>0 and E*E-Z*D>0
    print('m',m,'states',len(P),'transfer_nnz',sum(len(row) for row in M))
    print('coeff_a',a)
    print('coeff_b',b)
    print('coeff_c',c)
    print('coeff_l',l)
    print('coeff_d',d)
    print('brute_n2',direct)
    for key in ('R','L','D'):
        scalar,den,has_nm1,high=exp[key]
        print('rayleigh',key,'scalar',scalar,'den',den,'factor_n_minus_1',has_nm1,'positive_coefficients_high_to_low',high)

print('K6_K7_K8_K9_TRANSFER_EXACT_PASS')
