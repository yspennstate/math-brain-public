import numpy as np, math, cmath, itertools, json, pathlib, time
P=pathlib.Path(__file__).parent

def kernel_grid(N):
 k=2*np.pi*(np.arange(N)+.5)/N
 A=1/(2*np.cos(k[:,None])+2j*np.cos(k[None,:]))
 G=np.fft.ifft2(A)
 def kernel(d):
  x,y=d
  return G[x%N,y%N]*cmath.exp(1j*np.pi*(x+y)/N)
 return kernel

def edge(a,b):
 x,y=a;xx,yy=b
 if xx<x or yy<y:
  s,e=edge(b,a);return -s,e
 if xx==x+1:return (1 if (x+y)%2==0 else -1),tuple(sorted([(x,y-1),(x,y)]))
 return (1 if (x-1+y)%2==0 else -1),tuple(sorted([(x-1,y),(x,y)]))

def local_mean(points,s,G):
 # All paths start at (0,0); caller uses a resonant total charge len(points)*s.
 alpha=2*np.pi*s;coeff={};D=0
 for x,y in points:
  path=[(t,0) for t in range(x+1)]+[(x,t) for t in range(1,y+1)]
  for a,b in zip(path,path[1:]):
   sign,e=edge(a,b);coeff[e]=coeff.get(e,0)+sign;D+=sign/4
 updates=[]
 for e,c in coeff.items():
  u=cmath.exp(-1j*alpha*c)
  if abs(u-1)<1e-12:continue
  b,w=e
  if sum(b)%2:b,w=w,b
  K=1 if b[1]==w[1] else 1j
  updates.append((b,w,K*(u-1)))
 B=sorted(set(b for b,w,u in updates));bi={b:i for i,b in enumerate(B)}
 T=np.eye(len(B),dtype=complex)
 for b,w,u in updates:
  for j,bb in enumerate(B):T[bi[b],j]+=u*G((w[0]-bb[0],w[1]-bb[1]))
 return cmath.exp(1j*alpha*D)*np.linalg.det(T)

start=time.time();G=kernel_grid(128)
assert abs(G((1,0))-.25)<1e-12 and abs(G((0,1))+.25j)<1e-12
coords=[(x,y) for x in range(4) for y in range(4) if (x,y)!=(0,0)]
scan=[]
for other in itertools.combinations(coords,3):
 points=[(0,0),*other];v=local_mean(points,.25,G);scan.append((abs(v),points,v))
scan.sort(reverse=True,key=lambda t:t[0]);selected=scan[:4]
rows=[]
for mag,points,v in selected:
 vals=[]
 for N in [64,128,256,512]:
  g=kernel_grid(N);value=local_mean(points,.25,g)
  vals.append({'quadrature_grid':N,'real':value.real,'imag':value.imag,'modulus':abs(value)})
 rows.append({'distinct_dual_faces':points,'local_cluster_expectations':vals})
res={'scope':'Numerical infinite-plane Fourier quadrature and finite-rank determinant; not a rigorous lower-bound certificate. Uses exact fusion of four s=1/4 charges and local paths.','scanned_clusters':len(scan),'runtime_seconds':time.time()-start,'results':rows,'nearest_kernel_checks':{'G_1_0':[G((1,0)).real,G((1,0)).imag],'G_0_1':[G((0,1)).real,G((0,1)).imag]}}
(P/'distinct_fusion_checks.json').write_text(json.dumps(res,indent=2),encoding='utf8')
for row in rows:print(row['distinct_dual_faces'],row['local_cluster_expectations'])
