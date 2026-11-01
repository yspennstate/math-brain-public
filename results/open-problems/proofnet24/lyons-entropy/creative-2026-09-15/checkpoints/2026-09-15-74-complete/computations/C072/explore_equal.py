exec(open('computations/C072/explore.py').read().split('rng=')[0])
rng=np.random.default_rng(1721)
for s in [3.,100.,1e5]:
 best=(-1,None)
 for it in range(1000):
  magn=rng.integers(1,4,size=6)
  U=rng.choice([-1,1],size=(6,3))*magn[:,None]
  if np.linalg.matrix_rank(U)<3:continue
  G,C,H,J1,GN=matrices(s,U)
  dr=np.array([1,1,-2.]);f=dr@C@dr; I=dr@G@dr
  if f>best[0]:best=(f,(U,I,np.linalg.eigvalsh(H),dr@J1@dr))
  if f>1e-5:print('FOUND',s,it,'U',U,'F',f,'I',I,'eigH',np.linalg.eigvalsh(H),'linear',dr@J1@dr,flush=True);break
 else:print('none',s,best,flush=True)
