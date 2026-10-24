import json,time,importlib.util
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter

# Use only utilities from the earlier paired helper, without executing its search loops.
ROOT=Path(__file__).resolve().parents[1]
helper=(ROOT/'code'/'check_transport.py').read_text().split('for k,m in [(1,1),(2,1)]:')[0]
scope={'__file__':str(ROOT/'code'/'check_transport.py')}
exec(compile(helper,str(ROOT/'code'/'check_transport.py'),'exec'),scope)
walsh,sign,H,plus,law,I=map(scope.get,['walsh','sign','H','plus','law','I'])
START=time.perf_counter();ASSERTIONS=0;COUNTS=Counter();CORRELATION=Counter();ADMISSION=Counter()

def check(ok):
    global ASSERTIONS
    ASSERTIONS+=1
    assert ok,ASSERTIONS
    if time.perf_counter()-START>60:raise RuntimeError('Frozen 60-second cap')

def basis_case(g,k,group,seed=None,t=None):
    nx=len(g);m=k.bit_length();nb=1<<m
    codes=[1<<b if b<k else 0 for b in range(nb)]
    w=walsh(g);pg=[Q(a*a,nx*nx) for a in w]
    f=[sign(a&b)*g[x]*sign(codes[b]&x) for b in range(nb) for a in range(nb) for x in range(nx)]
    fw=walsh(f);den=len(f)**2
    px=[Q(0)]*nx;iy=ix=Q(0)
    for ti in range(nb):
        for s in range(nb):
            for v in range(nx):
                idx=v+nx*s+nx*nb*ti
                check(fw[idx]==nb*sign(s&ti)*w[v^codes[s]])
                p=Q(fw[idx]**2,den)
                px[v]+=p;ix+=p*v.bit_count();iy+=p*(s.bit_count()+ti.bit_count())
    check(iy==m)
    check(ix==I(pg)+Q(k-2*I(pg),nb))
    check(H([Q(a*a,den) for a in fw])==plus((1,{2:Q(2*m)}),(1,H(pg))))
    expected=[(1-Q(k,nb))*pg[v]+sum((pg[v^(1<<i)] for i in range(k)),Q(0))/nb for v in range(nx)]
    check(px==expected)
    # Signed spectra keep every phase row's entropy and coordinate erasure.
    for c in codes:
        shifted=[pg[v^c] for v in range(nx)]
        check(H(shifted)==H(pg))
    branches=[tuple(sign(c&x) for c in codes) for x in range(nx)]
    check(len(set(branches))==nx)
    check(all(z[k]==1 for z in branches)) # zero code fixes the global sign.
    uniform=all(p==Q(1,nx) for p in pg)
    dependent=any([pg[v^c] for v in range(nx)]!=pg for c in codes)
    check(dependent==(not uniform))
    CORRELATION['dependent' if dependent else 'independent_bent_seed_control']+=1
    character=any(abs(z)==nx for z in w)
    if not character:
        check(any(0<abs(z)<nx for z in w))
        check(codes[k]==0)
        ADMISSION['excluded_intermediate_row_amplitude']+=1
    else:
        support=set(range(k,nb));base=next(iter(support));direction={b^base for b in support}
        affine=all(a^b in direction for a in direction for b in direction)
        check(affine==((nb-k)&(nb-k-1)==0))
        ADMISSION['admitted_character_affine_cells' if affine else 'excluded_nonaffine_character_cell']+=1
    if seed is not None:
        sp=law(seed)
        check(H(pg)==plus((t,H(sp))))
        check(I(pg)==t*I(sp)+1)
        check(dependent)
        # The balanced seed has its final spectral bit constantly one.
        check(sum((p for v,p in enumerate(pg) if not (v>>(k-1)&1)),Q(0))==0)
        check(sum((p for v,p in enumerate(px) if not (v>>(k-1)&1)),Q(0))==Q(1,nb))
        # Direct physical edge count independently checks phase selector energy.
        edgeI=Q(sum(f[z]!=f[z^(1<<i)] for z in range(len(f)) for i in range(k)),len(f))
        check(edgeI==ix)
        jt=m+1+Q(k-2*(t*I(sp)+1),nb)
        check(ix+iy==t*I(sp)+jt)
        check(m<jt<m+2)
    COUNTS[group]+=1

def tensor_seed(seed,n,t):
    k=n*t+1;g=[]
    for x in range(1<<k):
        z=(-1)**((x>>(n*t))&1)
        for j in range(t):z*=seed[(x>>(n*j))&((1<<n)-1)]
        g.append(z)
    return g,k

def receipt():
    out={'status':'PASS','helper_version':'A079-basis-tags-v2','cases':dict(COUNTS),'total_cases':sum(COUNTS.values()),'spectral_dependence':dict(CORRELATION),'A034_admission':dict(ADMISSION),'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer signed Walsh; Fraction; exact prime-log entropy identities; physical selector edge counts','independent_review':False}
    (ROOT/'out'/'basis_tags_validation.json').write_text(json.dumps(out,indent=2)+'\n');return out

for k in [1,2,3]:
    for mask in range(1<<(1<<k)):
        g=[(-1)**((mask>>x)&1) for x in range(1<<k)]
        basis_case(g,k,'exhaustive_seed')
receipt()
for n in [1,2]:
    for mask in range(1<<(1<<n)):
        seed=[(-1)**((mask>>x)&1) for x in range(1<<n)]
        for t in [1,2]:
            g,k=tensor_seed(seed,n,t);basis_case(g,k,'balanced_tensor',seed,t)
receipt()
for mask in [1,23]:
    seed=[(-1)**((mask>>x)&1) for x in range(8)]
    for t in [1,2]:
        g,k=tensor_seed(seed,3,t);basis_case(g,k,'three_bit_tensor',seed,t)
print(json.dumps(receipt(),indent=2))
