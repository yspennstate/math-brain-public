"""Referee checks for the second attempt. All computations remain small."""
import numpy as np, itertools, math, json, pathlib, time
ROOT=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
els=list(itertools.permutations(range(3)));idx={g:i for i,g in enumerate(els)}
ident=tuple(range(3))
def mul(g,h):return tuple(g[h[i]] for i in range(3))
def inv(g):return tuple(g.index(i) for i in range(3))
def subgroup(gs):
    seen={ident};todo=[ident]
    while todo:
        x=todo.pop()
        for g in gs:
            y=mul(x,g)
            if y not in seen:seen.add(y);todo.append(y)
    return seen
def sign(g):return sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))%2
R=[]
for g in els:
    z=np.zeros((6,6))
    for x in els:z[idx[x],idx[mul(x,g)]]=1
    R.append(z)
even=[i for i,g in enumerate(els) if sign(g)==0]
Pi=sum((R[i] for i in even),np.zeros((6,6)))/3
evals,V=np.linalg.eigh(Pi);basis=V[:,evals<.5]
assert basis.shape==(6,4)
pairs=[(i,j) for i,j in itertools.product(range(6),repeat=2) if len(subgroup([els[i],els[j]]))==6]
assert len(pairs)==18
rho=.5+math.sqrt(3)/4
out={'s3_generating_pairs':18,'fiber_grid':{},'finite_generation':[],'quotient_moments':[],'profile_comparison':[]}
best=(-1,None)
angles=np.arange(48)*2*math.pi/48
for i,j in pairs:
    comm=mul(mul(mul(els[i],els[j]),inv(els[i])),inv(els[j]))
    assert len(subgroup([comm]))==3
    for alpha in angles:
        z=np.exp(1j*alpha)
        for beta in angles:
            w=np.exp(1j*beta)
            Q=.5*np.eye(6)+(z*R[i]+z.conjugate()*R[i].T+w*R[j]+w.conjugate()*R[j].T)/8
            assert np.linalg.norm(Q@Pi-Pi@Q)<1e-12
            ev=np.linalg.eigvalsh(basis.T@Q@basis)
            assert ev.min()>-1e-12 and ev.max()<=rho+1e-12
            if ev.max()>best[0]:best=(float(ev.max()),[i,j,float(alpha),float(beta)])
out['fiber_grid']={'points_per_angle':48,'block_tests':18*48**2,'max_eigenvalue':best[0],'attained_at':best[1],'rho':rho}
# Exact BFS in S3 x C_p for every pair at p=5; criterion and total count.
p=5;gen=0
for i,j in itertools.product(range(6),repeat=2):
    for a,b in itertools.product(range(p),repeat=2):
        seen={(ident,0)};todo=[(ident,0)]
        while todo:
            x,c=todo.pop()
            for h,z in [(els[i],a),(els[j],b)]:
                y=(mul(x,h),(c+z)%p)
                if y not in seen:seen.add(y);todo.append(y)
        ok=len(seen)==6*p
        assert ok == ((i,j) in pairs and (a,b)!=(0,0))
        gen+=ok
assert gen==18*(p*p-1)
out['finite_generation'].append({'p':p,'total_pairs':36*p*p,'generating_pairs':gen})
# Exact finite averaging of quotient Fourier moments (floating-point values).
for p in [5,7,11,17,31]:
    a,b=np.indices((p,p));mask=(a!=0)|(b!=0)
    C=np.cos(2*math.pi*np.arange(p)[:,None]*np.arange(p)[None,:]/p)
    for signs in [(1,1),(1,0),(0,1)]:
        for t in [1,p,3*p]:
            moment=np.zeros((p,p))
            for v in [0,1]:
                for j in range(p):
                    if (v,j)==(0,0):continue
                    lam=.5+.25*((-1)**(v*signs[0])*C[j,:,None]+(-1)**(v*signs[1])*C[j,None,:])
                    moment+=lam**(2*t)
            avg=float(moment[mask].mean())
            bound=(4.**(-t)+2*(p-1)*(1/p+math.sqrt(math.pi)/(2*math.sqrt(t)))**2)/(1-p**-2)
            assert avg<=bound+1e-10
            out['quotient_moments'].append({'p':p,'signs':signs,'t':t,'mean_L2_squared':avg,'B_bound':bound})
# Direct full-group TV recursion against projected recursion and all bounds.
rng=np.random.default_rng(93)
for p in [5,11,31,101]:
    cases=6
    for z in range(cases):
        i,j=pairs[int(rng.integers(len(pairs)))];a,b=map(int,rng.integers(p,size=2))
        if a==b==0:a=1
        law=np.zeros((6,p));law[idx[ident],0]=1
        perm=[]
        for h,c in [(els[i],a),(inv(els[i]),-a),(els[j],b),(inv(els[j]),-b)]:
            # Forward law push: new[y]=old[y h^-1].
            pre=np.array([idx[mul(y,inv(h))] for y in els])
            perm.append((pre,c))
        maxerr=0;tm=None
        for t in range(1,8*p+1):
            new=.5*law
            for pre,c in perm:new+=np.roll(law[pre,:],c,axis=1)/8
            law=new
            quotient=np.vstack([law[[i for i,g in enumerate(els) if sign(g)==s],:].sum(axis=0) for s in [0,1]])
            dg=float(.5*np.abs(law-1/(6*p)).sum());da=float(.5*np.abs(quotient-1/(2*p)).sum())
            assert abs(law.sum()-1)<1e-10
            assert dg+1e-10>=da
            assert dg-da<=math.sqrt(p)*rho**t+1e-10
            if (sign(els[i])==1 and a!=0) or (sign(els[j])==1 and b!=0):
                worst_upper=.5*math.sqrt(2/math.expm1(t/(p*p)))
            else:
                worst_upper=.5*math.sqrt(2/math.expm1(4*t/(p*p))+p*4.**(-t))
            assert da<=worst_upper+1e-10
            maxerr=max(maxerr,dg-da)
            if dg<=.25 and tm is None:tm=t
        lower=.75/4*max(math.sqrt(.75*p)-1,0)**2
        if tm is not None:assert tm+1e-10>=lower
        out['profile_comparison'].append({'p':p,'h_indices':[i,j],'cyclic':[a,b],'max_TV_gap':maxerr,'mixing_time_quarter':tm,'lower_bound':lower})
out['elapsed_seconds']=time.monotonic()-start
out['memory_design']='Largest dense phase array is 31x31. Full-group laws have at most 606 entries. No large matrices.'
(ROOT/'second_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:out[k] for k in ['s3_generating_pairs','fiber_grid','finite_generation','elapsed_seconds','memory_design']},indent=2))
print('Quotient moment cases:',len(out['quotient_moments']),'full profile cases:',len(out['profile_comparison']))
