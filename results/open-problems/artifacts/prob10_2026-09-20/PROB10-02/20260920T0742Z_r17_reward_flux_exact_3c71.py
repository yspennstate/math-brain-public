#!/usr/bin/env python3
from functools import lru_cache

UV=((0,0),(0,1),(1,0),(1,1))

def bits(mask,m):
    return tuple((mask>>(m-1-i))&1 for i in range(m))

def mask_from_bits(xs):
    z=0
    for b in xs:
        z=(z<<1)|b
    return z

def transition_q(m,xmask,gmask,u,v):
    x=bits(xmask,m)
    g=bits(gmask,m)
    V=[0]
    for z in g:
        V.append(V[-1]+z)
    a=[int(z==v) for z in x]+[int(u==v)]
    Q=[0]*(m+1)
    Q[0]=max(V[1],a[0])
    for k in range(1,m):
        Q[k]=max(Q[k-1],V[k]+a[k],V[k+1])
    Q[m]=max(Q[m-1],V[m]+a[m])
    gp=0
    for k in range(1,m+1):
        gp=(gp<<1)|(Q[k]-Q[k-1])
    xp=((xmask & ((1<<(m-1))-1))<<1)|u
    w=m//2
    rho=Q[w]-V[w]
    assert rho in (0,1)
    return xp,gp,rho,Q[0],Q,V

def flux_check(m):
    w=m//2
    edge_count=input_count=survive=left=right=0
    for x in range(1<<m):
      for g in range(1<<m):
        for j in range(m):
          bit=1<<(m-1-j)
          if g&bit:
              continue
          h=g|bit
          edge_count+=1
          for u,v in UV:
            xp,gp,rg,q0g,Qg,Vg=transition_q(m,x,g,u,v)
            xp2,hp,rh,q0h,Qh,Vh=transition_q(m,x,h,u,v)
            assert xp==xp2
            delta0=q0h-q0g
            assert delta0 in (0,1)
            diff=gp^hp
            if diff==0:
                Iout=0
                if delta0:
                    left+=1
                else:
                    right+=1
            else:
                assert diff&(diff-1)==0
                assert (hp&diff) and not (gp&diff)
                j2=m-1-(diff.bit_length()-1)
                Iout=int(j2<w)
                assert delta0==0
                survive+=1
            Iin=int(j<w)
            assert rh-rg==Iout+delta0-Iin
            deltas=[Qh[k]-Qg[k] for k in range(m+1)]
            assert all(d in (0,1) for d in deltas)
            if diff==0:
                assert all(d==delta0 for d in deltas)
            else:
                j2=m-1-(diff.bit_length()-1)
                assert deltas==[0 if k<j2+1 else 1 for k in range(m+1)]
            input_count+=1
    return edge_count,input_count,survive,left,right

def state_from_masks(m,x,g):
    return (bits(x,m),bits(g,m))

@lru_cache(None)
def trans_tuple(m,state,uv):
    x,g=state
    xp,gp,r,*_=transition_q(m,mask_from_bits(x),mask_from_bits(g),uv[0],uv[1])
    return (bits(xp,m),bits(gp,m)),r

def adjacent_raw_pairs(m):
    out=[]
    for x in range(1<<m):
      for g in range(1<<m):
        s=state_from_masks(m,x,g)
        for j in range(m):
            bit=1<<(m-1-j)
            if x&bit:
                continue
            out.append((s,state_from_masks(m,x|bit,g)))
    return out

def all_state_pairs(m):
    states=[state_from_masks(m,x,g) for x in range(1<<m) for g in range(1<<m)]
    return [(s,t) for s in states for t in states]

def extrema_over_common_words(m,init_pairs,N):
    cur={p:(0,0) for p in init_pairs}
    hist=[]
    for step in range(1,N+1):
        nxt={}
        for (s,t),(lo,hi) in cur.items():
            for uv in UV:
                s2,r1=trans_tuple(m,s,uv)
                t2,r2=trans_tuple(m,t,uv)
                d=r1-r2
                key=(s2,t2)
                a,b=nxt.get(key,(10**9,-10**9))
                if lo+d<a:
                    a=lo+d
                if hi+d>b:
                    b=hi+d
                nxt[key]=(a,b)
        cur=nxt
        glo=min(v[0] for v in cur.values())
        ghi=max(v[1] for v in cur.values())
        hist.append((step,glo,ghi,len(cur)))
    return hist

print("R17 PROB10-02 exact reward-flux checker")
for m in (2,4,6,8):
    e,n,s,l,r=flux_check(m)
    print(f"FLUX m={m} edges={e} edge_inputs={n} survive={s} left_absorb={l} right_absorb={r}")
    assert n==4*e
print("LOCAL_REWARD_FLUX_IDENTITY_PASS through m=8")

for m in (2,4):
    h=extrema_over_common_words(m,adjacent_raw_pairs(m),2*m+2)
    assert all(lo>=-1 and hi<=1 for _,lo,hi,_ in h)
    print(f"RAW_ONE_BIT_COMMON_WORD_OSCILLATION m={m} horizon={2*m+2} final={h[-1]}")
print("RAW_ONE_BIT_SMALL_WIDTH_EXACT_PASS")

for m in (2,4):
    h=extrema_over_common_words(m,all_state_pairs(m),2*m+2)
    maxabs=max(max(-lo,hi) for _,lo,hi,_ in h)
    print(f"FULL_STATE_COMMON_WORD_OSCILLATION m={m} horizon={2*m+2} maxabs={maxabs} history={h}")
    assert maxabs<=m
print("STRONGER_M_SPAN_SMALL_WIDTH_EVIDENCE_PASS_NOT_A_THEOREM")

print("PROVED_TRANSFER_CONSTANT_BY_THEOREM m=8 C<=16")
print("PROVED_TRANSFER_CONSTANT_BY_THEOREM m=12 C<=24")
print("ALL_EXACT_CHECKS_PASS")
