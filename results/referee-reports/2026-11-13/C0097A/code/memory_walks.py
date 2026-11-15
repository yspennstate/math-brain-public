#!/usr/bin/env python3
"""Finite-memory quotient matrices and exact Taylor coefficients; no lace enumeration."""
from collections import defaultdict
from pathlib import Path
import json,time,resource
ROOT=Path(__file__).resolve().parents[1]

def canonical(word):
    axes={};out=[]
    for a in word:
        if abs(a) not in axes:axes[abs(a)]=(len(axes)+1)*(1 if a>0 else -1)
        out.append(axes[abs(a)]*(1 if a>0 else -1))
    return tuple(out)

def legal(word):
    # A loop in the complete retained word is forbidden.
    p=defaultdict(int);seen={tuple()}
    for a in word:
        p[abs(a)]+=1 if a>0 else -1
        key=tuple((k,v) for k,v in sorted(p.items()) if v)
        if key in seen:return False
        seen.add(key)
    return True

def states_of_length(L):
    states=[()]
    for length in range(L):
        new=[]
        for w in states:
            k=max(map(abs,w),default=0)
            for a in list(range(1,k+2))+list(range(-1,-k-1,-1)):
                v=w+(a,)
                if legal(v):new.append(v)
        states=new
    assert len(states)==len(set(states))
    return sorted(states)

def quotient(tau):
    L=tau-1;states=states_of_length(L);ids={w:i for i,w in enumerate(states)}
    reset=ids[tuple(range(1,L+1))];dest=[];B=[];trans=[]
    for w in states:
        k=max(map(abs,w));new=ids[canonical((w+(k+1,))[-L:])]
        dest.append(new);row=defaultdict(int);row[new]-=2*k
        old=[]
        for a in list(range(1,k+1))+list(range(-1,-k-1,-1)):
            v=w+(a,)
            if legal(v):
                target=ids[canonical(v[-L:])];row[target]+=1;old.append(target)
        B.append(dict(row));trans.append((new,k,old))
    for i in range(len(states)):
        j=i
        for _ in range(L):j=dest[j]
        assert j==reset
    assert dest[reset]==reset
    assert max(sum(abs(x) for x in row.values()) for row in B)<=4*L
    return states,reset,dest,B,trans

def coefficients(tau,N=12):
    states,reset,dest,B,trans=quotient(tau);L=tau-1;size=len(states)
    vectors=[[1]*size];lam=[1]
    for n in range(1,N+1):
        bv=[sum(c*vectors[-1][j] for j,c in row.items()) for row in B]
        lam.append(bv[reset])
        y=[bv[i]-sum(lam[j]*vectors[n-j][i] for j in range(1,n+1)) for i in range(size)]
        assert y[reset]==0
        v=[0]*size;Ay=y
        for _ in range(L):
            v=[x+y for x,y in zip(v,Ay)];Ay=[Ay[j] for j in dest]
        assert not any(Ay)
        assert v[reset]==0
        # (I-A)v = y verifies the eigenvector equation at every computed order.
        assert [v[i]-v[dest[i]] for i in range(size)]==y
        vectors.append(v)
    return states,lam,trans

def quotient_count(states,trans,d,n):
    L=len(states[0]);assert n>=L
    counts=[]
    for w in states:
        k=max(map(abs,w));weight=1
        for j in range(k):weight*=2*(d-j)
        counts.append(weight)
    for _ in range(n-L):
        nxt=[0]*len(states)
        for i,(new,k,old) in enumerate(trans):
            nxt[new]+=counts[i]*2*(d-k)
            for j in old:nxt[j]+=counts[i]
        assert min(nxt)>=0
        counts=nxt
    return sum(counts)

def literal_count(tau,d,n):
    origin=(0,)*d
    def walk(path):
        if len(path)==n+1:return 1
        total=0;position=path[-1]
        for axis in range(d):
            for sign in [-1,1]:
                v=list(position);v[axis]+=sign;v=tuple(v)
                if v not in path[-tau:]:total+=walk(path+[v])
        return total
    return walk([origin])

if __name__=='__main__':
    start=time.monotonic();out=[]
    for tau in [2,4,6]:
        states,lam,trans=coefficients(tau)
        # Direct d=2 literal path enumeration independently checks forbidden-window indexing.
        q=quotient_count(states,trans,2,8);literal=literal_count(tau,2,8)
        assert q==literal
        item=dict(tau=tau,states=len(states),normalized_coefficients=lam,
                  mu_coefficients_powers_0_through_11=lam[1:],
                  rigorous_radius_lower_bound=f'1/{24*(tau-1)**2}',
                  A_power_reset_verified=True,eigenvector_equations_verified_through=12,
                  literal_vs_quotient_d2_length8=q)
        out.append(item);print(item)
    assert out[0]['normalized_coefficients']==[1,-1]+[0]*11
    (ROOT/'data'/'memory_walks.json').write_text(json.dumps(dict(results=out,
        seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        threads=1),indent=2)+'\n')
    print('all memory-walk checks passed;',round(time.monotonic()-start,3),'s')
