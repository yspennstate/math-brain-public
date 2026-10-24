"""High-precision stress tests: cross-block terms much smaller than within-block terms."""
import pathlib,json,itertools
import mpmath as mp
P=pathlib.Path(__file__).resolve().parent
mp.mp.dps=80
els=list(itertools.product(range(4),range(2)));idx={g:i for i,g in enumerate(els)};n=8
def mul(a,b):return ((a[0]+(-1)**a[1]*b[0])%4,(a[1]+b[1])%2)
def inv(a):return ((-(-1)**a[1]*a[0])%4,a[1])
def cosets(H):
 unused=set(els);cs=[]
 while unused:
  g=min(unused);C={mul(g,h) for h in H};cs.append(sorted(idx[h] for h in C));unused-=C
 return cs
# Hermitian rational/complex convolution values, indexed by group differences.
raw={g:mp.mpc((3*g[0]+2*g[1]+1)%5-2,(g[0]+g[1])%3-1) for g in els}
raw[(0,0)]=0
f={g:(raw[g]+mp.conj(raw[inv(g)]))/2 for g in els}
Hfull=mp.matrix([[f[mul(inv(g),h)] for h in els] for g in els])
records=[]
for subgroup,Hset in [('rotations_C4',{(j,0) for j in range(4)}),('reflection_C2',{(0,0),(0,1)})]:
 blocks=cosets(Hset);labels={i:k for k,C in enumerate(blocks) for i in C};m=len(blocks[0]);k=len(blocks)
 Ain=mp.matrix([[Hfull[i,j] if labels[i]==labels[j] else 0 for j in range(n)] for i in range(n)])
 Bout=mp.matrix([[Hfull[i,j] if labels[i]!=labels[j] else 0 for j in range(n)] for i in range(n)])
 # Event: at least one full coset for C4; at least two full cosets for C2.
 needed=1 if m==4 else 2
 accepted=[mask for mask in range(1<<n) if sum(all(mask>>i&1 for i in C) for C in blocks)>=needed]
 mob=[int(mask in accepted) for mask in range(1<<n)]
 for i in range(n):
  for mask in range(1<<n):
   if mask>>i&1:mob[mask]-=mob[mask^(1<<i)]
 for centre in ['0.2','0.4','0.7']:
  t=mp.mpf(centre)
  for sign in [-1,1]:
   for a in [mp.mpf('0.0'),mp.mpf('0.01'),mp.mpf('0.03')]:
    for exponent in [2,3,5,7]:
     b=sign*mp.mpf(10)**(-exponent)
     Q=t*mp.eye(n)+a*Ain+b*Bout
     evals=mp.eighe(Q,eigvals_only=True)
     assert 0<min(evals) and max(evals)<1
     det=mp.re(mp.det(Q));p=mp.root(det,n)
     lhs=mp.mpf(0)
     for mask,c in enumerate(mob):
      if c:
       ix=[i for i in range(n) if mask>>i&1]
       M=mp.matrix([[Q[i,j] for j in ix] for i in ix])
       lhs+=c*mp.re(mp.det(M))
     rhs=sum(p**mask.bit_count()*(1-p)**(n-mask.bit_count()) for mask in accepted)
     gap=lhs-rhs
     assert gap>=-mp.mpf('1e-65')
     records.append({'subgroup':subgroup,'event_full_blocks_at_least':needed,'t':centre,'within_scale':str(a),'cross_scale':str(b),'gap':mp.nstr(gap,60),'gap_over_cross_squared':mp.nstr(gap/b**2,50)})
P.joinpath('near_flat_results.json').write_text(json.dumps(records,indent=2))
print('HIGH_PRECISION_NEAR_FLAT_CHECKS_PASS',len(records),'spatial event comparisons')
print('minimum gap',min(mp.mpf(v['gap']) for v in records))
print('minimum gap/cross_squared',min(mp.mpf(v['gap_over_cross_squared']) for v in records))
