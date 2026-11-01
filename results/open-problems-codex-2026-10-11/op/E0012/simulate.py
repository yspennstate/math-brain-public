"""Bounded exact Gillespie simulations; finite transients cannot settle E0012."""
import math, random, time, pathlib, json

def run(a,b,g,seed,L=24,horizon=3000,seconds=55):
    rng=random.Random(seed); n=L*L
    nb=[(((i//L-1)%L)*L+i%L,((i//L+1)%L)*L+i%L,
         (i//L)*L+(i%L-1)%L,(i//L)*L+(i%L+1)%L) for i in range(n)]
    state=[rng.choice((1,2)) for _ in range(n)]
    k1=[sum(state[j]==1 for j in ns) for ns in nb]
    k2=[sum(state[j]==2 for j in ns) for ns in nb]
    rates=[0.0]*n; tree=[0.0]*(n+1)
    def rate(i):
        return (a*k1[i]+b*k2[i])/4 if state[i]==0 else (1.0 if state[i]==1 else 1+g*k1[i]/4)
    def update(i,newrate):
        delta=newrate-rates[i]; rates[i]=newrate; j=i+1
        while j<=n: tree[j]+=delta; j+=j&-j
    def total():
        ans=0.; j=n
        while j: ans+=tree[j]; j-=j&-j
        return ans
    for i in range(n):update(i,rate(i))
    counts=[state.count(i) for i in range(3)]
    t=0.; events=0; samples=[{'time':0,'counts':counts.copy()}]; nextsample=100.
    start=time.monotonic()
    while t<horizon and events<2000000:
        if events%256==0 and time.monotonic()-start>seconds:break
        tot=total()
        if tot<=0:break
        newt=t+rng.expovariate(tot)
        while nextsample<=min(newt,horizon):
            samples.append({'time':nextsample,'counts':counts.copy()});nextsample+=100
        if newt>horizon:t=horizon;break
        t=newt; u=rng.random()*tot; idx=0; bit=1<<(n.bit_length()-1)
        while bit:
            nxt=idx+bit
            if nxt<=n and tree[nxt]<=u:u-=tree[nxt];idx=nxt
            bit>>=1
        assert idx<n and rates[idx]>0
        old=state[idx]
        new=0 if old else (1 if rng.random()*rates[idx]<a*k1[idx]/4 else 2)
        state[idx]=new;counts[old]-=1;counts[new]+=1
        for j in nb[idx]:
            k1[j]+=(new==1)-(old==1);k2[j]+=(new==2)-(old==2)
        for j in (idx,*nb[idx]):update(j,rate(j))
        events+=1
        if events%4096==0:
            assert counts==[state.count(i) for i in range(3)]
            assert math.isclose(total(),sum(rates),rel_tol=1e-10,abs_tol=1e-7)
            assert all(k1[i]==sum(state[j]==1 for j in nb[i]) and k2[i]==sum(state[j]==2 for j in nb[i]) for i in range(n))
        if counts[1]==0 or counts[2]==0:break
    samples.append({'time':t,'counts':counts.copy()})
    return {'a':a,'b':b,'g':g,'seed':seed,'L':L,'target_time':horizon,'reached_time':t,
            'events':events,'wall_seconds':time.monotonic()-start,'samples':samples,
            'interpretation':'finite-torus transient only; no infinite-volume survival or noncoexistence conclusion'}

path=pathlib.Path('simulations.jsonl')
for seed,g in ((1201,20),(1202,20),(1203,100),(1204,100)):
    r=run(1.8,4.,g,seed)
    with path.open('a',encoding='utf8') as f:f.write(json.dumps(r)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='samples'}),flush=True)
