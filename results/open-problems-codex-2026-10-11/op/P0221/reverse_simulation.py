"""Small seeded online routing experiment; evidence, not proof."""
import itertools, json, math, random
from pathlib import Path

class UF:
    def __init__(self,n): self.p=list(range(n))
    def f(self,x):
        while self.p[x]!=x: x=self.p[x]
        return x
    def join(self,x,y):
        x,y=self.f(x),self.f(y)
        if x!=y: self.p[max(x,y)]=min(x,y)

def trial(n,rng):
    h=.8; eta=.2; b=.4; eps=.2; M=2
    a=(1+3*eps)/h; cap=a*b; tmax=h*(1-eta)
    edges=list(itertools.combinations(range(n),2)); N=len(edges)
    virt=UF(n); phys=UF(n); phi=list(range(n)); unseen=set(range(N))
    observations=[]; t=0.; reassignments=0
    def H(t): return N*cap*t-N*math.log(1-t/h)
    while t<tmax and unseen:
        target=H(t)+rng.expovariate(1)
        if target>=H(tmax): break
        lo,hi=t,tmax
        for _ in range(32):
            mid=(lo+hi)/2
            if H(mid)<target: lo=mid
            else: hi=mid
        t=(lo+hi)/2
        blocks={}
        for v in range(n): blocks.setdefault(virt.f(v),[]).append(v)
        def key(u,v):
            I,J=virt.f(u),virt.f(v)
            if I==J: return ('internal',I)
            i,j=len(blocks[I]),len(blocks[J])
            if i>=M and j>=M: return ('LL',*sorted((I,J)))
            if i>=M: return ('LS',I,j)
            if j>=M: return ('LS',J,i)
            return ('SS',*sorted((i,j)))
        potentials={}
        remaining={}
        for e,(u,v) in enumerate(edges):
            k=key(u,v)
            potentials[k]=potentials.get(k,0)+1
            if e in unseen: remaining.setdefault(k,[]).append(e)
        aux=[]
        for k,ids in remaining.items():
            if k[0]=='internal': aux.append((len(ids)/(h-t),ids,0.,1.))
            else:
                aux.append(((1-b)*len(ids)/(h-t),ids,b,1.))
                extra=max(0.,b*len(ids)/(h-t)-cap*potentials[k])
                if extra: aux.append((extra,ids,0.,b))
        dom=N*cap+N/(h-t)
        assert N*cap+sum(row[0] for row in aux)<=dom+1e-8
        pick=rng.random()*dom
        retained=False; physical_pair=None
        if pick<N*cap:
            pu,pv=rng.choice(edges); w=rng.random()*cap
            u,v=phi[pu],phi[pv]; k=key(u,v)
            ids=remaining.get(k,[])
            if k[0]=='internal' or not ids: continue
            d=b*len(ids)/(h-t); ell=cap*potentials[k]
            if rng.random()>min(1.,d/ell): continue
            e=rng.choice(ids); x,y=edges[e]
            I,J=virt.f(u),virt.f(v)
            X,Y=virt.f(x),virt.f(y)
            # Orient targets to the physical candidate's class.
            def c(j): return ('large',j) if len(blocks[j])>=M else ('small',len(blocks[j]))
            if c(I)!=c(X) or c(J)!=c(Y): x,y=y,x; X,Y=Y,X
            assert c(I)==c(X) and c(J)==c(Y)
            cm={I:X,J:Y}
            for size in range(1,n+1):
                left=[j for j,B in blocks.items() if len(B)==size and j not in cm]
                right=[j for j,B in blocks.items() if len(B)==size and j not in cm.values()]
                cm.update(zip(left,right))
            sigma={u:x,v:y}
            for source,destination in cm.items():
                left=[z for z in blocks[source] if z not in sigma]
                right=[z for z in blocks[destination] if z not in sigma.values()]
                assert len(left)==len(right)
                sigma.update(zip(left,right))
            phi=[sigma[z] for z in phi]
            assert set(phi)==set(range(n)) and phi[pu]==x and phi[pv]==y
            mark=w/a; retained=True; physical_pair=(pu,pv); reassignments+=1
        else:
            pick-=N*cap
            chosen=None
            for rate,ids,low,high in aux:
                if pick<rate: chosen=(ids,low,high); break
                pick-=rate
            if chosen is None: continue
            ids,low,high=chosen; e=rng.choice(ids)
            mark=low+(high-low)*rng.random()
        assert e in unseen
        unseen.remove(e); observations.append((e,t/h,mark))
        x,y=edges[e]
        if virt.f(x)!=virt.f(y):
            if retained:
                pu,pv=physical_pair
                assert phys.f(pu)!=phys.f(pv)
                phys.join(pu,pv)
            virt.join(x,y)
        for r in range(n):
            image={virt.f(phi[v]) for v in range(n) if phys.f(v)==phys.f(r)}
            assert len(image)==1
    return observations,reassignments

rng=random.Random(2211011)
out=[]
for n in (3,5):
    trials=2000; N=n*(n-1)//2
    sx=sy=sxy=sz=marks=marksum=cheap=reassignments=0.
    for _ in range(trials):
        obs,updates=trial(n,rng)
        x=sum(t<=.25 for e,t,w in obs); y=sum(.25<t<=.5 for e,t,w in obs)
        sx+=x; sy+=y; sxy+=x*y; sz+=len(obs)
        marks+=len(obs); marksum+=sum(w for e,t,w in obs)
        cheap+=sum(w<=.4 for e,t,w in obs); reassignments+=updates
    row=dict(n=n,trials=trials,first_bin_mean=sx/trials,second_bin_mean=sy/trials,
             target_bin_mean=N/4,bin_covariance=sxy/trials-sx*sy/trials**2,
             target_bin_covariance=-N/16,total_mean=sz/trials,target_total_mean=.8*N,
             mark_mean=marksum/marks,cheap_fraction=cheap/marks,
             physical_reassignments=int(reassignments))
    assert abs(row['first_bin_mean']-N/4)<.15
    assert abs(row['second_bin_mean']-N/4)<.15
    assert abs(row['total_mean']-.8*N)<.15
    assert abs(row['mark_mean']-.5)<.03
    assert abs(row['cheap_fraction']-.4)<.03
    out.append(row)
Path(__file__).with_name('reverse_simulation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
