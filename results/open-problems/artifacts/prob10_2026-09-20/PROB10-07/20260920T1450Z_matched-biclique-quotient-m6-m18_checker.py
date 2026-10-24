#!/usr/bin/env python3
from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import product
from math import factorial, gcd, comb
from hashlib import sha256
import sys, time

WIDTHS=[int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else list(range(6,13))

# Each layer is ('S', marks) or ('P', marks). Mark payload for S is terminal label;
# for P it is 'h' or ('u',terminal) or ('v',terminal).
ORBITS=[
("SS_same_layer_diff_terminal",[('S',[('e',0),('f',1)])]),
("SS_diff_layers_same_terminal",[('S',[('e',0)]),('S',[('f',0)])]),
("SS_diff_layers_diff_terminal",[('S',[('e',0)]),('S',[('f',1)])]),
("P_same_h_spoke",[('P',[('e','h'),('f',('u',0))])]),
("P_same_same_endpoint_diff_terminal",[('P',[('e',('u',0)),('f',('u',1))])]),
("P_same_opposite_same_terminal",[('P',[('e',('u',0)),('f',('v',0))])]),
("P_same_opposite_diff_terminal",[('P',[('e',('u',0)),('f',('v',1))])]),
("PP_diff_matching_matching",[('P',[('e','h')]),('P',[('f','h')])]),
("PP_diff_matching_spoke",[('P',[('e','h')]),('P',[('f',('u',0))])]),
("PP_diff_spokes_same_terminal",[('P',[('e',('u',0))]),('P',[('f',('u',0))])]),
("PP_diff_spokes_diff_terminal",[('P',[('e',('u',0))]),('P',[('f',('u',1))])]),
("PS_matching_ordinary",[('P',[('e','h')]),('S',[('f',0)])]),
("PS_spokes_same_terminal",[('P',[('e',('u',0))]),('S',[('f',0)])]),
("PS_spokes_diff_terminal",[('P',[('e',('u',0))]),('S',[('f',1)])]),
]

@lru_cache(None)
def integer_partitions(n,min_part=1):
    if n==0:return ((),)
    out=[]
    for a in range(min_part,n+1):
        for rest in integer_partitions(n-a,a):out.append((a,)+rest)
    return tuple(out)

@lru_cache(None)
def marked_set_partitions(d):
    if d==0:return ((),)
    parts=[((0,),)]
    for x in range(1,d):
        nxt=set()
        for p in parts:
            for j in range(len(p)):
                q=[list(b) for b in p]; q[j].append(x)
                nxt.add(tuple(sorted((tuple(sorted(b)) for b in q),key=lambda b:b[0])))
            nxt.add(tuple(sorted(p+((x,),),key=lambda b:b[0])))
        parts=sorted(nxt)
    return tuple(parts)

def weak_compositions_leq(total,slots):
    if slots==0:return [()]
    out=[]
    def rec(pre,k,rem):
        if k==1:
            for a in range(rem+1):out.append(tuple(pre+[a]))
            return
        for a in range(rem+1):rec(pre+[a],k-1,rem-a)
    rec([],slots,total)
    return out

@lru_cache(None)
def quotient_states(m,d):
    u=m-d; out=[]
    for mp in marked_set_partitions(d):
        g=len(mp)
        if g==0:
            for pure in integer_partitions(u):out.append(((),pure))
        else:
            for av in weak_compositions_leq(u,g):
                rem=u-sum(av)
                for pure in integer_partitions(rem):
                    out.append((tuple((mp[i],av[i]) for i in range(g)),pure))
    return tuple(out)

def canon_state(db,pure):
    db2=tuple(sorted(((tuple(sorted(group)),a) for group,a in db),key=lambda z:min(z[0]))) if db else ()
    return (db2,tuple(sorted(pure)))

def discrete_state(m,d):
    db=tuple(((i,),0) for i in range(d))
    return (db,tuple([1]*(m-d)))

# Generic one-center coarsening transition. Optional selected block weight = z*|B|.
# required_labels is a tuple/list, not a set: duplicates deliberately signal collision.
def transition_merge(state,required_labels,state_index,z=1):
    db,pure=state
    label_to_block={}
    for i,(group,a) in enumerate(db):
        for x in group:label_to_block[x]=i
    req_blocks=[label_to_block[x] for x in required_labels]
    if len(set(req_blocks))!=len(req_blocks):return {}
    req=set(req_blocks)
    optional_db=[i for i in range(len(db)) if i not in req]
    pure_items=sorted(Counter(pure).items())
    out=defaultdict(int)
    for mask in range(1<<len(optional_db)):
        sel_db=set(req); w_db=1
        for j,bi in enumerate(optional_db):
            if (mask>>j)&1:
                sel_db.add(bi)
                group,a=db[bi]
                w_db*=z*(len(group)+a)
        chosen=[0]*len(pure_items)
        def rec(t,w_pure,sel_count,sel_sum):
            if t==len(pure_items):
                total=len(sel_db)+sel_count
                if total<2:
                    target=state
                else:
                    new_db=[b for i,b in enumerate(db) if i not in sel_db]
                    new_pure=[]
                    for (s,c),k in zip(pure_items,chosen):new_pure.extend([s]*(c-k))
                    if sel_db:
                        ug=[]; ua=sel_sum
                        for i in sorted(sel_db):
                            group,a=db[i]; ug.extend(group); ua+=a
                        new_db.append((tuple(sorted(ug)),ua))
                    else:
                        new_pure.append(sel_sum)
                    target=canon_state(new_db,new_pure)
                out[state_index[target]]+=w_db*w_pure
                return
            s,c=pure_items[t]
            for k in range(c+1):
                chosen[t]=k
                rec(t+1,w_pure*comb(c,k)*((z*s)**k),sel_count+k,sel_sum+s*k)
        rec(0,1,0,0)
    return dict(out)

def compose(A,B):
    out=[]
    for i in range(len(A)):
        r=defaultdict(int)
        for j,a in A[i].items():
            for k,b in B[j].items():r[k]+=a*b
        out.append({k:v for k,v in r.items() if v})
    return out

def mat_add(A,B):
    out=[]
    for ra,rb in zip(A,B):
        r=defaultdict(int); r.update(ra)
        for j,b in rb.items():r[j]+=b
        out.append({j:v for j,v in r.items() if v})
    return out

def sub_scalar_I(T,c):
    out=[]
    for i,row in enumerate(T):
        r=dict(row);r[i]=r.get(i,0)-c
        if r.get(i)==0:r.pop(i,None)
        out.append(r)
    return out

def rows_equal(A,B):return all(a==b for a,b in zip(A,B))

def apply_row(row,T):
    out=[0]*len(row)
    for i,a in enumerate(row):
        if a:
            for j,w in T[i].items():out[j]+=a*w
    return out

def apply_col(T,col):
    return [sum(w*col[j] for j,w in r.items()) for r in T]

# polynomial in x,y represented dict (i,j)->Fraction
def poly_add(A,B,scale=Fraction(1)):
    C=dict(A)
    for k,v in B.items():
        C[k]=C.get(k,Fraction(0))+scale*v
        if C[k]==0:del C[k]
    return C

def poly_mul(A,B):
    C=defaultdict(Fraction)
    for (i,j),a in A.items():
        for (p,q),b in B.items():C[(i+p,j+q)]+=a*b
    return {k:v for k,v in C.items() if v}

def binom_coeff(n):
    c=[Fraction(1)]
    for t in range(n):
        d=[Fraction(0)]*(len(c)+1)
        for i,a in enumerate(c):d[i]+=-t*a;d[i+1]+=a
        c=d
    f=factorial(n)
    return [a/f for a in c]

def poly_eval(P,x,y):return sum(c*(x**i)*(y**j) for (i,j),c in P.items())
def primitive_digest(P):
    den=1
    def lcm(a,b):return a//gcd(a,b)*b
    for c in P.values():den=lcm(den,c.denominator)
    ints={k:int(c*den) for k,c in P.items()}
    g=0
    for v in ints.values():g=gcd(g,abs(v))
    if g:ints={k:v//g for k,v in ints.items()}
    payload=';'.join(f'{i},{j}:{ints[(i,j)]}' for i,j in sorted(ints))
    return den,g,sha256(payload.encode()).hexdigest(),ints

def infer_d(layers):
    labs=[]
    for kind,marks in layers:
        for mark,e in marks:
            if kind=='S':labs.append(e)
            elif e!='h':labs.append(e[1])
    return max(labs)+1 if labs else 0

class QuotientAlgebra:
    def __init__(self,m,d):
        self.m=m;self.d=d;self.states=quotient_states(m,d);self.idx={s:i for i,s in enumerate(self.states)}
        self.star_cache={};self.h_cache={};self.pair_cache={}
        self.S=self.star(())
        self.H=self.hpresent((),())
        self.P=mat_add(compose(self.S,self.S),self.H)
        self.mu=m+1;self.lam=m*m+4*m+2
        assert {r.get(i,0) for i,r in enumerate(self.S)}=={self.mu}
        assert {r.get(i,0) for i,r in enumerate(self.P)}=={self.lam}
        self.N=sub_scalar_I(self.S,self.mu);self.Q=sub_scalar_I(self.P,self.lam)
        # exact commutation follows combinatorially from disjoint layer order; entrywise recheck through width 17.
        if m<=17:
            assert rows_equal(compose(self.N,self.Q),compose(self.Q,self.N))
        # off-diagonal only => strict coarsening; verify no diagonal residues
        assert all(i not in r for i,r in enumerate(self.N))
        assert all(i not in r for i,r in enumerate(self.Q))
        ones=[1]*len(self.states)
        self.w={}
        ncols=[ones]
        for _ in range(1,m+1):ncols.append(apply_col(self.N,ncols[-1]))
        assert not any(ncols[m])
        for j in range(m):
            cur=ncols[j];self.w[(0,j)]=cur
            for i in range(1,m-j):
                cur=apply_col(self.Q,cur);self.w[(i,j)]=cur
            # boundary i+j=m must vanish
            if m-j>=1:
                bd=apply_col(self.Q,cur)
                assert not any(bd)
        self.bx=[binom_coeff(i) for i in range(m)];self.by=[binom_coeff(i) for i in range(m)]
        self.start=self.idx[discrete_state(m,d)]
    def star(self,req):
        req=tuple(req)
        if req not in self.star_cache:
            self.star_cache[req]=[transition_merge(s,req,self.idx,1) for s in self.states]
        return self.star_cache[req]
    def hpresent(self,U,V):
        key=(tuple(U),tuple(V))
        if key not in self.h_cache:
            req=tuple(U)+tuple(V)
            self.h_cache[key]=[transition_merge(s,req,self.idx,2) for s in self.states]
        return self.h_cache[key]
    def pair(self,forced):
        # forced iterable containing 'h' and/or ('u',t), ('v',t)
        forced=tuple(forced)
        key=tuple(sorted(forced,key=lambda x:(0,-1) if x=='h' else (1 if x[0]=='u' else 2,x[1])))
        if key in self.pair_cache:return self.pair_cache[key]
        hf='h' in forced
        U=tuple(x[1] for x in forced if x!='h' and x[0]=='u')
        V=tuple(x[1] for x in forced if x!='h' and x[0]=='v')
        H=self.hpresent(U,V)
        if hf:T=H
        else:T=mat_add(compose(self.star(U),self.star(V)),H)
        self.pair_cache[key]=T
        return T
    def response(self,layers,cond):
        row=[0]*len(self.states);row[self.start]=1
        for kind,marks in layers:
            forced=[edge for mark,edge in marks if mark in cond]
            T=self.star(forced) if kind=='S' else self.pair(forced)
            row=apply_row(row,T)
        R={}
        for (i,j),col in self.w.items():
            a=sum(u*v for u,v in zip(row,col))
            if not a:continue
            s=Fraction(a,self.lam**i*self.mu**j)
            term={}
            for dx,cx in enumerate(self.bx[i]):
                for dy,cy in enumerate(self.by[j]):
                    if cx and cy:term[(dx,dy)]=s*cx*cy
            R=poly_add(R,term)
        return R

def certify_orbit(m,name,layers,cache):
    d=infer_d(layers)
    key=(m,d)
    if key not in cache:cache[key]=QuotientAlgebra(m,d)
    A=cache[key]
    C0=A.response(layers,set());Ce=A.response(layers,{'e'});Cf=A.response(layers,{'f'});Cef=A.response(layers,{'e','f'})
    R=poly_add(poly_mul(Ce,Cf),poly_mul(C0,Cef),Fraction(-1))
    neg=[(ij,c) for ij,c in R.items() if c<0]
    a=sum(kind=='P' for kind,_ in layers);b=sum(kind=='S' for kind,_ in layers)
    xmin=1 if a==0 else 0; ymin=0
    first=poly_eval(R,xmin,ymin)
    den,g,dig,ints=primitive_digest(R)
    return dict(name=name,d=d,states=len(A.states),deg=max(i+j for i,j in R),terms=len(R),first=first,neg=neg,digest=dig,ints=ints,C=(C0,Ce,Cf,Cef),a=a,b=b)

# Generic orbit classifier for actual graph edges
def classify_pair(edge1,edge2,k):
    a,b=edge1,edge2
    def side(e):
        if e[0]=='match':return ('P',e[1],'h',None)
        _,t,r=e
        if r<2*k:return ('P',r//2,'spoke',(r%2,t))
        return ('S',r-2*k,'spoke',(None,t))
    A,B=side(a),side(b)
    if A[0]=='S' and B[0]=='S':
        if A[1]==B[1]:return 'SS_same_layer_diff_terminal'
        return 'SS_diff_layers_same_terminal' if A[3][1]==B[3][1] else 'SS_diff_layers_diff_terminal'
    if A[0]=='S' or B[0]=='S':
        P,S=(B,A) if A[0]=='S' else (A,B)
        if P[2]=='h':return 'PS_matching_ordinary'
        return 'PS_spokes_same_terminal' if P[3][1]==S[3][1] else 'PS_spokes_diff_terminal'
    if A[1]==B[1]:
        if A[2]=='h' or B[2]=='h':return 'P_same_h_spoke'
        ea,ta=A[3];eb,tb=B[3]
        if ea==eb:return 'P_same_same_endpoint_diff_terminal'
        return 'P_same_opposite_same_terminal' if ta==tb else 'P_same_opposite_diff_terminal'
    if A[2]=='h' and B[2]=='h':return 'PP_diff_matching_matching'
    if A[2]=='h' or B[2]=='h':return 'PP_diff_matching_spoke'
    return 'PP_diff_spokes_same_terminal' if A[3][1]==B[3][1] else 'PP_diff_spokes_diff_terminal'

def graph_edges(m,k,r):
    E=[]
    for t in range(m):
        for R in range(2*k+r):E.append(('spoke',t,R))
    for q in range(k):E.append(('match',q))
    return E

def generic_orbit_check(m,k=2,r=2):
    E=graph_edges(m,k,r);cnt=Counter()
    for i in range(len(E)):
        for j in range(i+1,len(E)):cnt[classify_pair(E[i],E[j],k)]+=1
    assert set(cnt)=={n for n,_ in ORBITS}
    return len(E),len(E)*(len(E)-1)//2,dict(cnt)

def actual_graph(m,k,r):
    right=2*k+r;edges=[]
    for t in range(m):
        for R in range(right):edges.append((t,m+R,('spoke',t,R)))
    for q in range(k):edges.append((m+2*q,m+2*q+1,('match',q)))
    return m+right,edges

def brute_all(m,k,r):
    n,E=actual_graph(m,k,r);q=len(E)
    Z=0;Ze=[0]*q;Zef=[[0]*q for _ in range(q)]
    for mask in range(1<<q):
        par=list(range(n));rank=[0]*n;inc=[];ok=True
        def find(x):
            while par[x]!=x:
                par[x]=par[par[x]];x=par[x]
            return x
        for i,(u,v,_) in enumerate(E):
            if (mask>>i)&1:
                a,b=find(u),find(v)
                if a==b:ok=False;break
                if rank[a]<rank[b]:a,b=b,a
                par[b]=a
                if rank[a]==rank[b]:rank[a]+=1
                inc.append(i)
        if not ok:continue
        Z+=1
        for i in inc:Ze[i]+=1
        for aa in range(len(inc)):
            for bb in range(aa+1,len(inc)):
                i,j=inc[aa],inc[bb];Zef[i][j]+=1;Zef[j][i]+=1
    reps={};mind=None
    for i in range(q):
        for j in range(i+1,q):
            name=classify_pair(E[i][2],E[j][2],k);reps.setdefault(name,(i,j))
            d=Ze[i]*Ze[j]-Z*Zef[i][j]
            if mind is None or d<mind[0]:mind=(d,i,j)
    assert set(reps)=={n for n,_ in ORBITS}
    return n,E,Z,Ze,Zef,reps,mind

def predicted_counts(info,k,r,m):
    x=k-info['a'];y=r-info['b'];assert x>=0 and y>=0
    lam=m*m+4*m+2;mu=m+1
    return tuple(int((lam**x)*(mu**y)*poly_eval(C,x,y)) for C in info['C'])

def regression_m2_k2_r2():
    m,k,r=2,2,2
    n,E,Z,Ze,Zef,reps,mind=brute_all(m,k,r)
    cache={};out=[]
    for name,layers in ORBITS:
        info=certify_orbit(m,name,layers,cache)
        i,j=reps[name]
        direct=(Z,Ze[i],Ze[j],Zef[i][j])
        pred=predicted_counts(info,k,r,m)
        assert direct==pred or direct==(pred[0],pred[2],pred[1],pred[3]),(name,direct,pred)
        delta=direct[1]*direct[2]-direct[0]*direct[3]
        assert delta>0
        out.append((name,direct,delta))
    return len(E),Z,len(E)*(len(E)-1)//2,mind,out

# known digests from full Bell m6/7 certificate, used as an independent implementation cross-check
KNOWN={
6:{
'SS_same_layer_diff_terminal':'79c81f5b7fd273e42fb70ac5e0ddaca7124ba48f35902fa1beeda714d70f7874',
'SS_diff_layers_same_terminal':'505a87571038f5bfeb586fd7361890b82e3e9d0e91e36a0cf46d7f4f871f5d23',
'SS_diff_layers_diff_terminal':'e1dda33da33f256abfd113a60f01c47ec7311f684ab3efa75ff27dca50ccad13',
'P_same_h_spoke':'b940bab1aa4a09b908f9ba630c4f703be181e8c93cafe8408a64f541cf9828a6',
'P_same_same_endpoint_diff_terminal':'ff172d026c2c1966591098cdb81f5590d07ea5e6510747c5322981ea4af6fa17',
'P_same_opposite_same_terminal':'135c09c66a5ddd108c963e02d18d44d45080363a928060ff6f6e29adba4144ea',
'P_same_opposite_diff_terminal':'e7034efe391cde7581ea5a80081def9e6875c1f970a7844f2e9dfb69bf63cf78',
'PP_diff_matching_matching':'001a433952e6b8a6c37f30e93e573abbb45335f1dbb5ec6f35a3750a6cb895be',
'PP_diff_matching_spoke':'eabf082e4fea898a1398892f45efc81571c0c1413014835aafc1806ee320d7c8',
'PP_diff_spokes_same_terminal':'2ad4c561b197336ee863177d7ad090bfb2aba83c7c139a897708084daf176d76',
'PP_diff_spokes_diff_terminal':'5c9c1f64a524d28da96d033c6617544616edf3955a4b23d6f22a603e38ce1d40',
'PS_matching_ordinary':'a16abf59cde4d4af166c0d491a89a46c8b86f9f06578ac349ed79be4bf7841ec',
'PS_spokes_same_terminal':'e94b457830817014a45ee5e3dfebd00813fc39f1147c25f3b653726aed42f525',
'PS_spokes_diff_terminal':'aa1e4418e8c66e92638215a768fde2180d0a94e2519993618a444955b0931119'},
7:{
'SS_same_layer_diff_terminal':'b813fb43ac74d3b1d943520c88c6622fdef5a6ef3578f1fb3cf4ddf46a9b3da4',
'SS_diff_layers_same_terminal':'00653763d6ce157273365137ad8d6293c3605e78d3929b445c97823ae71f6767',
'SS_diff_layers_diff_terminal':'402a1a61bd77fd14df164c7ac362479f1fd922b357ee551b3fa57659747827e3',
'P_same_h_spoke':'2086190baed20b3aed0b9981dd55c9acfcfe1f010fde0297ec228ad6ab615775',
'P_same_same_endpoint_diff_terminal':'8f109a06a068747927000c8085243b9be4f96fd650f8a7898a64563b44fc178f',
'P_same_opposite_same_terminal':'642017e37213bec24ad832641c16098e55a8f92ce3532a2d25f555dfbd06d0b1',
'P_same_opposite_diff_terminal':'33fe9f984404ca2c6b0a72fc42ad72c2fdc1792e3002dedbbc06cc0d1691be4b',
'PP_diff_matching_matching':'88ca5175feabb371ca2c982c6322ea0959773afb97aa0e38096ae6ad298812bd',
'PP_diff_matching_spoke':'2b230df950757cd4183cee2424e44b9dd254942f3d9b57f7b605ea0ffdf9affb',
'PP_diff_spokes_same_terminal':'9910d427e0156269d1ea6b296c8b0dbf2893b067799f60455d8f98449f2c1788',
'PP_diff_spokes_diff_terminal':'93eab96194e47ea9accfefb5cdb42a800531085e9d9876d0c7be1b6364a6a57d',
'PS_matching_ordinary':'5d894be46262a159438b70eddbb94d7db75e120078ee31ad09aff2a32aa4a89c',
'PS_spokes_same_terminal':'46796234e3fba04ba913b413b2171c0248aea0d8feeb2382597f2db632b914c2',
'PS_spokes_diff_terminal':'10412f63c9172e39290f2115b79ed86b8abe6fadcf30fc53961ba013a3f4085f'}
}

def main():
    t0=time.time()
    print('PROB10-07 matched-biclique stabilizer-quotient exact certificate')
    print('scope=uniform measure on ALL forests of G_m(k,r)=K_{m,2k+r}+M_k; exact integer/Fraction arithmetic')
    print('pair_layer=no-h:T_U*T_V; h-present:H_UV with optional selected block weight 2|B|; P=S^2+H')
    e,z,pairs,mind,reg=regression_m2_k2_r2()
    reg_payload=';'.join(f'{name}:{counts}:{delta}' for name,counts,delta in reg)
    print(f'DIRECT_REGRESSION G2(2,2) edges={e} forests={z} pairs={pairs} minDelta={mind[0]} all14=PASS sha256={sha256(reg_payload.encode()).hexdigest()}')
    allcache={}
    for m in WIDTHS:
        infos=[]
        for name,layers in ORBITS:
            info=certify_orbit(m,name,layers,allcache)
            if info['neg']:
                print('NEGATIVE_COEFFICIENT',m,name,info['neg'][:10])
                raise AssertionError((m,name,'negative coefficient'))
            assert info['first']>0
            if m in KNOWN:
                assert info['digest']==KNOWN[m][name],(m,name,info['digest'],KNOWN[m][name])
            infos.append(info)
        ge,gp,gc=generic_orbit_check(m)
        assert len(gc)==14
        payload=';'.join(f"{q['name']}:{q['digest']}:{q['first']}:{q['deg']}:{q['terms']}" for q in infos)
        agg=sha256(payload.encode()).hexdigest()
        print(f'WIDTH m={m} d0={len(quotient_states(m,0))} d1={len(quotient_states(m,1))} d2={len(quotient_states(m,2))} generic_edges={ge} generic_pairs={gp} orbits=14 all_coeff_nonnegative=PASS all_first_positive=PASS max_degree={max(q["deg"] for q in infos)} min_terms={min(q["terms"] for q in infos)} fullBell_digest_match={"PASS" if m in KNOWN else "NA"} orbit_aggregate_sha256={agg}')
    print(f'elapsed_seconds={time.time()-t0:.3f}')
    print('PROB10_07_MATCHED_BICLIQUE_QUOTIENT_EXACT_PASS')
if __name__=='__main__':main()
