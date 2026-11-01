#!/usr/bin/env python3
"""Exact M=7, K=4 uncapped renewal Bellman lower certificate for binary LCS.

Floating relative-value iteration only proposes an integer potential.  The
proof pass clears all transition probabilities and recomputes every Bellman
residual in integer arithmetic.  The run-length tail category is exact, not
truncated: category M means G>=M and the geometric excess is integrated using
the inherited exact tail-difference identities.
"""
from fractions import Fraction
import hashlib
import time
import numpy as np

M=7
K=4
ITERATIONS=46
SCALE=10_000_000
FLOAT=np.float32
D=2**(M-1)
C=6*D
W=np.array([D//(2**k) for k in range(1,M)]+[1],dtype=np.int64)
P=W.astype(FLOAT)/FLOAT(D)
ZERO=M-1
SH0=(2*M-1,)+(M,)*(2*K)
SHT=(2,M)+(M,)*(2*K)
BASE=(ZERO,)+(0,)*(2*K)
EXCHANGE=tuple(range(K,2*K))+tuple(range(0,K))

def avg_A_last(x):
    return np.tensordot(x,P,axes=([K-1],[0]))

def avg_B_last(x):
    return np.tensordot(x,P,axes=([2*K-1],[0]))

def bellman_float(phi0,phiT):
    left=np.empty((M,)*(2*K+1),dtype=FLOAT)
    for ia in range(M):
        x=ia+1
        for ib in range(M):
            y=ib+1
            if x<M and y<M:
                val=min(x,y)+avg_A_last(phi0[ZERO+x-y])
            elif x==M and y<M:
                val=y+avg_A_last(phiT[0,M-y-1])
            elif x<M and y==M:
                val=x+avg_A_last(phiT[1,M-x-1])
            else:
                mix=(phi0[ZERO]+phiT[0,0]+phiT[1,0])/FLOAT(3.0)
                val=FLOAT(M+1/3)+avg_A_last(mix)
            sl=[slice(None)]*(2*K+1)
            sl[0]=ia
            sl[K]=ib
            left[tuple(sl)]=val
    out0=np.empty_like(phi0)
    outT=np.empty_like(phiT)
    out0[ZERO]=np.tensordot(left,P,axes=([2*K],[0]))
    for d in range(1,M):
        right=np.empty((M,)*(2*K),dtype=FLOAT)
        for ib2 in range(M):
            b=ib2+1
            if b<M:
                val=min(d,b)+avg_B_last(phi0[ZERO+d-b])
            else:
                val=d+avg_B_last(phiT[1,M-d-1])
            sl=[slice(None)]*(2*K)
            sl[K]=ib2
            right[tuple(sl)]=val
        shape=list(right.shape)
        shape.insert(K,1)
        choose=np.maximum(left,right.reshape(shape))
        out0[ZERO+d]=np.tensordot(choose,P,axes=([2*K],[0]))
        out0[ZERO-d]=np.transpose(out0[ZERO+d],EXCHANGE)
    for r in range(1,M+1):
        right=np.empty((M,)*(2*K),dtype=FLOAT)
        for ib2 in range(M):
            b=ib2+1
            if b<M:
                if r>b:
                    mix=phiT[0,r-b-1]
                    reward=FLOAT(b)
                elif r==b:
                    mix=FLOAT(.5)*phi0[ZERO]+FLOAT(.5)*phiT[0,0]
                    reward=FLOAT(b)
                else:
                    q=b-r
                    mix=np.zeros_like(phi0[ZERO])
                    for e in range(q):
                        p=FLOAT(2.0**(-(e+1)))
                        j=q-e
                        mix+=p*phi0[ZERO-j]
                    p=FLOAT(2.0**(-(q+1)))
                    mix+=p*phi0[ZERO]+p*phiT[0,0]
                    reward=FLOAT(r+1.0-2.0**(-q))
                val=reward+avg_B_last(mix)
            else:
                q=M-r
                mix=np.zeros_like(phi0[ZERO])
                p=FLOAT((1/3)*2.0**(-q))
                mix+=p*phiT[0,0]+p*phi0[ZERO]
                if q>=1:
                    for j in range(1,q):
                        mix+=FLOAT((1/3)*2.0**(-(q-j)))*phi0[ZERO-j]
                    mix+=FLOAT(1/3)*phi0[ZERO-q]+FLOAT(1/3)*phiT[1,q]
                else:
                    mix+=FLOAT(1/3)*phiT[1,0]
                reward=FLOAT(r+1.0-(2.0**(1-q))/3.0)
                val=reward+avg_B_last(mix)
            sl=[slice(None)]*(2*K)
            sl[K]=ib2
            right[tuple(sl)]=val
        shape=list(right.shape)
        shape.insert(K,1)
        choose=np.maximum(left,right.reshape(shape))
        outT[0,r-1]=np.tensordot(choose,P,axes=([2*K],[0]))
        outT[1,r-1]=np.transpose(outT[0,r-1],EXCHANGE)
    return out0,outT

t0=time.time()
phi0=np.zeros(SH0,dtype=FLOAT)
phiT=np.zeros(SHT,dtype=FLOAT)
for it in range(ITERATIONS):
    F0,FT=bellman_float(phi0,phiT)
    base=F0[BASE]
    phi0=F0-base
    phiT=FT-base
    print('iter',it,'base',float(base),'elapsed',time.time()-t0,flush=True)

P0=np.rint(phi0*SCALE).astype(np.int32)
PT=np.rint(phiT*SCALE).astype(np.int32)
z=((P0[ZERO].astype(np.int64)+np.transpose(P0[ZERO],EXCHANGE).astype(np.int64))//2).astype(np.int32)
P0[ZERO]=z
for d in range(1,M):
    avg=((P0[ZERO+d].astype(np.int64)+np.transpose(P0[ZERO-d],EXCHANGE).astype(np.int64))//2).astype(np.int32)
    P0[ZERO+d]=avg
    P0[ZERO-d]=np.transpose(avg,EXCHANGE)
for r in range(M):
    avg=((PT[0,r].astype(np.int64)+np.transpose(PT[1,r],EXCHANGE).astype(np.int64))//2).astype(np.int32)
    PT[0,r]=avg
    PT[1,r]=np.transpose(avg,EXCHANGE)
assert np.array_equal(P0[ZERO],np.transpose(P0[ZERO],EXCHANGE))
for d in range(1,M):
    assert np.array_equal(P0[ZERO-d],np.transpose(P0[ZERO+d],EXCHANGE))
for r in range(M):
    assert np.array_equal(PT[1,r],np.transpose(PT[0,r],EXCHANGE))
sha0=hashlib.sha256(P0.tobytes(order='C')).hexdigest()
shaT=hashlib.sha256(PT.tobytes(order='C')).hexdigest()

left=np.empty((M,)*(2*K+1),dtype=np.int64)
for ia in range(M):
    x=ia+1
    for ib in range(M):
        y=ib+1
        if x<M and y<M:
            hnum=min(x,y)*SCALE*C+P0[ZERO+x-y].astype(np.int64)*C
        elif x==M and y<M:
            hnum=y*SCALE*C+PT[0,M-y-1].astype(np.int64)*C
        elif x<M and y==M:
            hnum=x*SCALE*C+PT[1,M-x-1].astype(np.int64)*C
        else:
            hnum=M*SCALE*C+(SCALE*C)//3+(C//3)*(P0[ZERO].astype(np.int64)+PT[0,0].astype(np.int64)+PT[1,0].astype(np.int64))
        avg=np.tensordot(hnum,W,axes=([K-1],[0]))
        sl=[slice(None)]*(2*K+1)
        sl[0]=ia
        sl[K]=ib
        left[tuple(sl)]=avg

DEN=SCALE*C*D*D
min_num=None
max_num=None
argmin=None
state_count=0
future=np.tensordot(left,W,axes=([2*K],[0]))
residual=future-P0[ZERO].astype(np.int64)*(C*D*D)
idx=np.unravel_index(int(np.argmin(residual)),residual.shape)
min_num=int(residual[idx])
max_num=int(residual.max())
argmin=('E',0)+tuple(int(i)+1 for i in idx)
state_count+=residual.size

for d in range(1,M):
    right=np.empty((M,)*(2*K),dtype=np.int64)
    for ib2 in range(M):
        b=ib2+1
        if b<M:
            hnum=min(d,b)*SCALE*C+P0[ZERO+d-b].astype(np.int64)*C
        else:
            hnum=d*SCALE*C+PT[1,M-d-1].astype(np.int64)*C
        avg=np.tensordot(hnum,W,axes=([2*K-1],[0]))
        sl=[slice(None)]*(2*K)
        sl[K]=ib2
        right[tuple(sl)]=avg
    shape=list(right.shape)
    shape.insert(K,1)
    choose=np.maximum(left,right.reshape(shape))
    future=np.tensordot(choose,W,axes=([2*K],[0]))
    residual=future-P0[ZERO+d].astype(np.int64)*(C*D*D)
    idx=np.unravel_index(int(np.argmin(residual)),residual.shape)
    value=int(residual[idx])
    if value<min_num:
        min_num=value
        argmin=('E',d)+tuple(int(i)+1 for i in idx)
    max_num=max(max_num,int(residual.max()))
    state_count+=2*residual.size

for r in range(1,M+1):
    right=np.empty((M,)*(2*K),dtype=np.int64)
    for ib2 in range(M):
        b=ib2+1
        if b<M:
            if r>b:
                hnum=b*SCALE*C+PT[0,r-b-1].astype(np.int64)*C
            elif r==b:
                hnum=b*SCALE*C+(C//2)*(P0[ZERO].astype(np.int64)+PT[0,0].astype(np.int64))
            else:
                q=b-r
                hnum=((r+1)*C-C//(2**q))*SCALE
                mix=np.zeros_like(P0[ZERO],dtype=np.int64)
                for e in range(q):
                    j=q-e
                    mix+=(C//(2**(e+1)))*P0[ZERO-j].astype(np.int64)
                coeff=C//(2**(q+1))
                mix+=coeff*P0[ZERO].astype(np.int64)+coeff*PT[0,0].astype(np.int64)
                hnum+=mix
        else:
            q=M-r
            penalty=(2*C)//3 if q==0 else C//(3*(2**(q-1)))
            hnum=((r+1)*C-penalty)*SCALE
            mix=np.zeros_like(P0[ZERO],dtype=np.int64)
            coeff=C//(3*(2**q))
            mix+=coeff*PT[0,0].astype(np.int64)+coeff*P0[ZERO].astype(np.int64)
            if q>=1:
                for j in range(1,q):
                    mix+=(C//(3*(2**(q-j))))*P0[ZERO-j].astype(np.int64)
                mix+=(C//3)*P0[ZERO-q].astype(np.int64)+(C//3)*PT[1,q].astype(np.int64)
            else:
                mix+=(C//3)*PT[1,0].astype(np.int64)
            hnum+=mix
        avg=np.tensordot(hnum,W,axes=([2*K-1],[0]))
        sl=[slice(None)]*(2*K)
        sl[K]=ib2
        right[tuple(sl)]=avg
    shape=list(right.shape)
    shape.insert(K,1)
    choose=np.maximum(left,right.reshape(shape))
    future=np.tensordot(choose,W,axes=([2*K],[0]))
    residual=future-PT[0,r-1].astype(np.int64)*(C*D*D)
    idx=np.unravel_index(int(np.argmin(residual)),residual.shape)
    value=int(residual[idx])
    if value<min_num:
        min_num=value
        argmin=('T+',r)+tuple(int(i)+1 for i in idx)
    max_num=max(max_num,int(residual.max()))
    state_count+=2*residual.size

expected=(4*M-1)*M**(2*K)
assert state_count==expected
assert min_num>0
avg=Fraction(min_num,DEN)
gamma=avg/2
previous=Fraction(249596269,320000000)
published=Fraction(99083249,125000000)
assert gamma>previous
assert gamma<published
print('M =',M)
print('K_future_per_source =',K)
print('quota_count_including_active =',K+1)
print('iterations =',ITERATIONS)
print('future_category_states_checked =',state_count)
print('expected_state_count =',expected)
print('probability_denominator_D =',D)
print('internal_common_denominator_C =',C)
print('potential_scale =',SCALE)
print('potential_sha256_E =',sha0)
print('potential_sha256_T =',shaT)
print('exact_min_residual_numerator =',min_num)
print('exact_max_residual_numerator =',max_num)
print('exact_common_denominator =',DEN)
print('minimizing_state =',argmin)
print('average_reward_lower =',avg)
print('gamma2_renewal_lower =',gamma)
print('gamma2_renewal_lower_decimal =',format(float(gamma),'.15f'))
print('previous_P05_renewal_lower =',previous)
print('increment_over_previous =',gamma-previous)
print('published_global_lower_baseline =',published)
print('gap_to_published_global_lower =',published-gamma)
print('FIXED_GLOBAL_ENDPOINT_MOVEMENT = NO')
print('EXACT_M7_K4_UNCAPPED_BELLMAN_PASS')
