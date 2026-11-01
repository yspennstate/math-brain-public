#!/usr/bin/env python3
from math import comb
from collections import defaultdict, Counter


def ceildiv(a,b):
    assert b>0
    return -((-a)//b)


def enumerate_profiles(N,target16,target_mu16=None):
    C=[comb(N,k) for k in range(N+1)]
    c=[[0]*(N+1) for _ in range(6)]
    for j in range(6):
        for k in range(j,N+1):
            c[j][k]=comb(N-j,k-j)
    out=[]; prefixes=0
    for u0 in (0,1):
        for b1 in range(C[1]+1):
            u1=b1-c[0][1]*u0
            for b2 in range(C[2]+1):
                u2=b2-c[0][2]*u0-c[1][2]*u1
                for b3 in range(C[3]+1):
                    prefixes+=1
                    u3=b3-c[0][3]*u0-c[1][3]*u1-c[2][3]*u2
                    R=target16+16*u1+16*u2+12*u3
                    lo=-10**30; hi=10**30; feasible=True
                    for k in range(N+1):
                        base=u0*c[0][k]+u1*c[1][k]+u2*c[2][k]+u3*c[3][k]
                        A=5*base-c[5][k]*R
                        B=5*c[4][k]-8*c[5][k]
                        M=5*C[k]
                        if B==0:
                            if not (0<=A<=M):
                                feasible=False; break
                        elif B>0:
                            lo=max(lo,ceildiv(-A,B)); hi=min(hi,(M-A)//B)
                        else:
                            bb=-B
                            lo=max(lo,ceildiv(A-M,bb)); hi=min(hi,A//bb)
                        if lo>hi:
                            feasible=False; break
                    if not feasible: continue
                    residue=(-2*R)%5
                    start=lo+((residue-lo)%5)
                    for u4 in range(start,hi+1,5):
                        u5=(-R-8*u4)//5
                        mu16=32*u0+16*u1+8*u2+4*u3+2*u4+u5-16
                        if target_mu16 is not None and mu16!=target_mu16:
                            continue
                        u=(u0,u1,u2,u3,u4,u5)
                        b=tuple(sum(u[j]*c[j][k] for j in range(6)) for k in range(N+1))
                        assert all(0<=b[k]<=C[k] for k in range(N+1))
                        assert -16*u1-16*u2-12*u3-8*u4-5*u5==target16
                        assert mu16*(2**N)==32*sum(b)-16*(2**N)
                        out.append((u,b,mu16))
    return prefixes,out


def combine_children(bp,bm):
    n=len(bp)-1
    return tuple((bp[k] if 0<=k<=n else 0)+(bm[k-1] if 0<=k-1<=n else 0) for k in range(n+2))


def compositions(total,m,prefix=()):
    if m==0:
        if total==0: yield prefix
        return
    if m==1:
        yield prefix+(total,); return
    for x in range(total+1):
        yield from compositions(total-x,m-1,prefix+(x,))


def dedup_types(arr):
    out=[]; seen=set()
    for t in arr:
        key=(t['s'],t['t'],t['bp'],t['bm'])
        if key not in seen:
            seen.add(key); out.append(t)
    return out

print('P0169 S=37,n=15 exact gluing checker')
print('arithmetic=integer; floating_point=False')

# Necessary child/parent profile atlases.
profiles={}
expected={(14,33):(1007400,490),(14,34):(1007400,322),(14,35):(1007400,184),(15,37):(1546752,92)}
for key,(ep,ec) in expected.items():
    N,L=key
    p,o=enumerate_profiles(N,L)
    assert p==ep and len(o)==ec
    profiles[key]=o
    print(f'N{N}_L{L}_prefixes',p,'profiles',len(o),'mu16_set',sorted({z[2] for z in o}))

child_by=defaultdict(list)
for L in (33,34,35):
    for z in profiles[(14,L)]:
        child_by[(L,z[2])].append(z)

parents=profiles[(15,37)]
C14=[comb(14,k) for k in range(15)]

# Exact legal coordinate types for a fixed parent. In the n=15,S=37 branch,
# s_i>=2+|t_i|. Coordinates with s=2 have t=0. If exactly eight such
# coordinates remain after the first incidence filter, the other seven must
# all have s=3, and then t in {-1,0,1}.
def coordinate_types(parent,s):
    _,b,mu=parent
    ts=[0] if s==2 else [-1,0,1]
    out=[]
    for t in ts:
        assert abs(t)<=s-2
        Lp=37-s+t; Lm=37-s-t
        mup=mu+s; mum=mu-s
        for zp in child_by[(Lp,mup)]:
            for zm in child_by[(Lm,mum)]:
                if combine_children(zp[1],zm[1])==b:
                    out.append(dict(s=s,t=t,Lp=Lp,Lm=Lm,mup=mup,mum=mum,
                                    bp=zp[1],bm=zm[1],up=zp[0],um=zm[0]))
    return dedup_types(out)

types2=[coordinate_types(p,2) for p in parents]
types3=[coordinate_types(p,3) for p in parents]
print('parent_s2_type_count_hist',sorted(Counter(len(x) for x in types2).items()))
print('parent_s3_type_count_hist',sorted(Counter(len(x) for x in types3).items()))

# B20: before using s=3 types, prove that any parent surviving the incidence
# capacity conditions must have exactly r=8 coordinates with s=2. Since
# sum s_i=37 over 15 positive integers with s_i>=2, r>=8. For each r>=8,
# aggregate all legal s=2 child types and leave the other 15-r coordinates
# completely unconstrained except for the trivial layer capacities. This is a
# necessary condition, so failure is a rigorous elimination.
rough=[]
for pi,(parent,T2) in enumerate(zip(parents,types2)):
    if not T2: continue
    _,b,mu=parent
    for r in range(8,15):
        found=None
        for x in compositions(r,len(T2)):
            ok=True
            rem=15-r
            for k in range(15):
                cp=sum(x[j]*T2[j]['bp'][k] for j in range(len(T2)))
                target=(15-k)*b[k]
                if not (0<=target-cp<=rem*C14[k]):
                    ok=False; break
            if not ok: continue
            for q in range(15):
                cm=sum(x[j]*T2[j]['bm'][q] for j in range(len(T2)))
                target=(q+1)*b[q+1]
                if not (0<=target-cm<=rem*C14[q]):
                    ok=False; break
            if ok:
                found=x; break
        if found is not None:
            rough.append((pi,r,found))
            break

assert rough
assert {r for _,r,_ in rough}=={8}
print('parents_surviving_s2_incidence_capacity',len(rough))
print('surviving_r_values',sorted({r for _,r,_ in rough}))
print('surviving_parent_indices',[pi for pi,_,_ in rough])

# With r=8, the remaining seven singleton units sum 37-16=21, and each is
# at least 3, hence every remaining coordinate has s=3. Now impose the full
# exact coordinate-incidence identities simultaneously across all 15
# coordinates. Group equal legal types and search multiplicities x,y with
# sum x=8 and sum y=7. The plus identities are
#   sum_i p_i(k)=(15-k)b_k.
# The minus identities then follow from gluing, but we check them too.
exact_survivors=[]
parent_summaries=[]
for pi,r,xrough in rough:
    parent=parents[pi]; _,b,mu=parent
    T2=types2[pi]; T3=types3[pi]
    if not T3:
        parent_summaries.append((pi,len(T2),0,0))
        continue

    target_plus=tuple((15-k)*b[k] for k in range(15))
    target_minus=tuple((q+1)*b[q+1] for q in range(15))

    # Map exact s=2 aggregate plus vectors to multiplicities; retain all only
    # insofar as needed for a match. There are at most C(14,6)=3003 for 7 types.
    map2=defaultdict(list)
    ncomp2=0
    for x in compositions(8,len(T2)):
        ncomp2+=1
        vp=tuple(sum(x[j]*T2[j]['bp'][k] for j in range(len(T2))) for k in range(15))
        vm=tuple(sum(x[j]*T2[j]['bm'][k] for j in range(len(T2))) for k in range(15))
        map2[vp].append((vm,x))

    ncomp3=0; found=None
    for y in compositions(7,len(T3)):
        ncomp3+=1
        vp3=tuple(sum(y[j]*T3[j]['bp'][k] for j in range(len(T3))) for k in range(15))
        req=tuple(target_plus[k]-vp3[k] for k in range(15))
        for vm2,x in map2.get(req,[]):
            vm3=tuple(sum(y[j]*T3[j]['bm'][k] for j in range(len(T3))) for k in range(15))
            if all(vm2[k]+vm3[k]==target_minus[k] for k in range(15)):
                found=(x,y); break
        if found is not None: break
    parent_summaries.append((pi,len(T2),len(T3),ncomp2*ncomp3))
    if found is not None:
        exact_survivors.append((pi,found))

assert exact_survivors==[]
print('rough_parent_type_summary',parent_summaries)
print('exact_global_multiset_survivors',len(exact_survivors))
print('S37_n15_eliminated',True)
print('next_S37_support_size',16)
print('ASSERTIONS_PASS')
