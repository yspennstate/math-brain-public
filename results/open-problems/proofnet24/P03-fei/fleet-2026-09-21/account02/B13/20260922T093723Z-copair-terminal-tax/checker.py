#!/usr/bin/env python3
# Standard-library checker for B13 20260922T093723Z co-pair terminal tax.
# Exhausts Boolean functions modulo global sign through n=4, verifies the
# co-pair identities/inequalities, and certifies the primitive near-tensor
# family used to rule out a raw hidden-curvature O(J) payment from
# all-block terminality + tensor-primitivity alone.

import math
from itertools import combinations

LN2 = math.log(2.0)

def h2(p):
    if p <= 0.0 or p >= 1.0: return 0.0
    return -p*math.log2(p) - (1.0-p)*math.log2(1.0-p)

def jfun(q):
    if q <= 0.0: return 0.0
    if q >= 0.5: return 1.0
    s=math.sqrt(q*(1.0-q))
    return 1.0-h2(0.5+s)

def jprime(q):
    if q <= 0.0: return 2.0/LN2
    if q >= 0.5: return 0.0
    y=2.0*math.sqrt(q*(1.0-q))
    return 2.0*(1.0-2.0*q)/(y*LN2)*math.atanh(y)

def fwht(vals):
    out=[float(v) for v in vals]; h=1; n=len(out)
    while h<n:
        for a in range(0,n,2*h):
            for k in range(h):
                x=out[a+k]; y=out[a+h+k]
                out[a+k]=x+y; out[a+h+k]=x-y
        h*=2
    inv=1.0/n
    return [x*inv for x in out]

def influences(vals,n):
    N=1<<n; ans=[]
    for i in range(n):
        b=1<<i; c=0
        for x in range(N):
            c += vals[x] != vals[x^b]
        ans.append(c/N)
    return ans

def centered(vals,n):
    inf=influences(vals,n)
    T=[i for i,p in enumerate(inf) if p>0.5]
    out=[]
    for x,v in enumerate(vals):
        s=0
        for i in T: s ^= (x>>i)&1
        out.append(-v if s else v)
    return out,[min(p,1-p) for p in inf]

def entropy(ps):
    return -sum(p*math.log2(p) for p in ps if p>0.0)

def pair_stats(vals,n,i,j,probs):
    N=1<<n; cnt=supp=opp=ci1=cj1=nonaff=0
    for x in range(N):
        if ((x>>i)&1) or ((x>>j)&1): continue
        a=vals[x]; b=vals[x^(1<<i)]; c=vals[x^(1<<j)]; d=vals[x^(1<<i)^(1<<j)]
        gi0=(a-b)/2; gi1=(c-d)/2
        supp += (gi0!=0)!=(gi1!=0)
        opp += gi0!=0 and gi0==-gi1
        ui=((a!=b)+(c!=d))/2; uj=((a!=c)+(b!=d))/2
        ci1 += ui==1; cj1 += uj==1
        nonaff += a*b*c*d==-1
        cnt += 1
    p=supp/cnt; o=opp/cnt; ci=ci1/cnt; cj=cj1/cnt; pn=nonaff/cnt
    dist=[0.0]*4
    for S,pr in enumerate(probs):
        dist[((S>>i)&1)+2*((S>>j)&1)] += pr
    return p,o,ci,cj,pn,dist[3],entropy(dist)

def all_pair_checks():
    checks=funcs=0; maxerr=0.0; minslack=1e100
    for n in range(1,5):
        N=1<<n
        for bits in range(1<<(N-1)):
            vals=[1]+[1 if (bits>>(x-1))&1 else -1 for x in range(1,N)]
            vals,q=centered(vals,n); wh=fwht(vals); probs=[z*z for z in wh]
            P=sum(jfun(x) for x in q); funcs+=1
            for i,j in combinations(range(n),2):
                p,o,ci,cj,pn,r,Hij=pair_stats(vals,n,i,j,probs)
                ai=jprime(q[i]); aj=jprime(q[j])
                maxerr=max(maxerr,abs(r-(p+4*o)/4),abs(ci-(q[i]-p/2)),abs(cj-(q[j]-p/2)),abs(pn-p))
                s1=jfun(q[i])+jfun(q[j])-(2*p+ai*ci+aj*cj)
                s2=P-(Hij+ai*ci+aj*cj)
                s3=Hij-2*p
                if min(s1,s2,s3)<-1e-10: raise AssertionError((n,bits,i,j,s1,s2,s3))
                minslack=min(minslack,s1,s2,s3); checks+=1
    return funcs,checks,maxerr,minslack

def base_phi6_margins():
    q=1/32; hp=h2(q); ap=jprime(q); rows=[]
    for a in range(1,7):
        if a<=4: D=a*q; U=a*hp
        elif a==5: D=6*q; U=5*hp-ap*q
        else: D=6*q; U=6*hp
        rows.append((a,U-4*D))
    return rows

def G_value(x,m):
    s=1
    for r in range(m):
        if ((x>>(6*r))&63)==0: s=-s
    if x==(1<<(6*m))-1: s=-s
    return s

def primitive_rectangles(m=3):
    n=6*m; v=(1<<n)-1; tested=0
    for A in range(1,1<<n):
        if not (A&1) or A==v: continue
        B=v^A; split=None
        for r in range(m):
            block=63<<(6*r); aa=A&block; bb=B&block
            if aa and bb: split=(r,aa,bb); break
        if split is None:
            ia=(A&-A).bit_length()-1; ib=(B&-B).bit_length()-1
            pts=[v,v^(1<<ia),v^(1<<ib),v^(1<<ia)^(1<<ib)]
        else:
            _,aa,bb=split; ia=(aa&-aa).bit_length()-1; ib=(bb&-bb).bit_length()-1
            pts=[0,1<<ia,1<<ib,(1<<ia)|(1<<ib)]
        prod=1
        for x in pts: prod*=G_value(x,m)
        if prod!=-1: raise AssertionError((A,split,pts,prod))
        tested+=1
    return tested

def family_bounds():
    q0=1/32; out=[]
    for m in range(3,11):
        N=6*m; delta=2**(1-N); perturb=21*N*delta
        if perturb>=0.075: raise AssertionError((m,perturb))
        face_delta=2**(2-N)
        U4=576*m*(m-1)*(q0*q0-face_delta)
        J=N*(q0+delta)
        out.append((m,N,perturb,U4,J,U4/J))
    return out

def rep_cross():
    m=3; n=18; N=1<<n; vals=[G_value(x,m) for x in range(N)]; inf=influences(vals,n); i,j=0,6
    edge=[0,0]; den=[0,0]; cnt=supp=opp=0
    for x in range(N):
        if (x>>i)&1: continue
        b=(x>>j)&1; den[b]+=1; edge[b]+=vals[x]!=vals[x^(1<<i)]
    a=edge[0]/den[0]; b=edge[1]/den[1]
    ci=.5*max(2*a-1,0)+.5*max(2*b-1,0)
    for x in range(N):
        if ((x>>i)&1) or ((x>>j)&1): continue
        g0=(vals[x]-vals[x^(1<<i)])/2; g1=(vals[x^(1<<j)]-vals[x^(1<<j)^(1<<i)])/2
        supp+=(g0!=0)!=(g1!=0); opp+=g0!=0 and g0==-g1; cnt+=1
    p=supp/cnt; o=opp/cnt; return inf[i],inf[j],p,o,ci,p-2*ci+4*o

if __name__=='__main__':
    funcs,checks,maxerr,minslack=all_pair_checks(); rows=base_phi6_margins(); rects=primitive_rectangles(); fam=family_bounds(); rep=rep_cross()
    print('CO_PAIR_FUNCTIONS',funcs); print('CO_PAIR_PAIR_CHECKS',checks); print('CO_PAIR_MAX_IDENTITY_ERROR',f'{maxerr:.3e}'); print('CO_PAIR_MIN_INEQUALITY_SLACK',f'{minslack:.3e}')
    print('PHI6_K4_MARGINS',[(a,round(x,12)) for a,x in rows]); print('G3_PARTITION_RECTANGLES',rects); print('G3_REP_CROSS',tuple(round(x,12) for x in rep)); print('FAMILY_LOWER_BOUNDS')
    for z in fam: print(' ',z[0],z[1],f'pert={z[2]:.12g}',f'U4>={z[3]:.12g}',f'J<={z[4]:.12g}',f'ratio>={z[5]:.12g}')
    print('PASS')
