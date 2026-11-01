import ast,time,json,pathlib
from collections import deque
import numpy as np
from scipy.fft import dstn,idstn
P=pathlib.Path('.');start=time.monotonic()
tree=ast.parse(P.joinpath('experiments.py').read_text(encoding='utf-8-sig'));fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='stabilize');ns={'deque':deque,'time':time,'start':start};exec(compile(ast.Module(body=[fn],type_ignores=[]),'experiments.py','exec'),ns);stabilize=ns['stabilize']
def lap(v):
 a=-4*v.copy();a[1:,:]+=v[:-1,:];a[:-1,:]+=v[1:,:];a[:,1:]+=v[:,:-1];a[:,:-1]+=v[:,1:];return a
def potential(e):
 L=e.shape[0];k=np.arange(1,L+1);mu=2-2*np.cos(np.pi*k/(L+1));vf=-idstn(dstn(e.astype(float),type=1,norm='ortho')/(mu[:,None]+mu[None,:]),type=1,norm='ortho');v=np.rint(vf).astype(np.int64)
 assert np.array_equal(lap(v),e)
 return v,float(np.max(np.abs(vf-v)))
def burn_remainder(e):
 L=e.shape[0];X=np.ones((L,L),dtype=bool)
 while X.any():
  deg=np.zeros((L,L),dtype=np.int64);deg[1:,:]+=X[:-1,:];deg[:-1,:]+=X[1:,:];deg[:,1:]+=X[:,:-1];deg[:,:-1]+=X[:,1:]
  remove=X & (e>=deg)
  if not remove.any():return X
  X[remove]=False
 return X
def least_by_sets(L):
 v=np.zeros((L,L),dtype=np.int64);e=lap(v);steps=0
 while True:
  X=burn_remainder(e)
  if not X.any():return v,e,steps
  v-=X.astype(np.int64);e=lap(v);assert e.max()<=3;steps+=1
  if steps>10*(L+1)**2:raise RuntimeError('unexpected descent cap')
with P.joinpath('identity_dirichlet_checks.jsonl').open('w',encoding='utf8') as out:
 for L in [1,2,3,4,5,6,8,10,12,24,48,72]:
  t,_,_=stabilize([6]*(L*L),L);e,_,_=stabilize([6-x for x in t],L);e=np.array(e,dtype=np.int64).reshape(L,L);v,rounderr=potential(e)
  assert e.min()>=0 and e.max()<=3 and v.max()<=0 and not burn_remainder(e).any()
  i=np.arange(1,L+1,dtype=np.int64);bound=-1.5*np.minimum((i*(L+1-i))[:,None],(i*(L+1-i))[None,:]);assert np.all(v>=bound)
  row={'L':L,'integer_laplacian_exact':True,'rounding_error':rounderr,'potential_min_scaled':float(v.min()/(L+1)**2),'height_mean':float(e.mean()),'strip_barrier':True,'recurrent':True}
  if L<=10:
   vb,eb,steps=least_by_sets(L);assert np.array_equal(v,vb) and np.array_equal(e,eb);row['independent_forbidden_set_descent']=True;row['descent_steps']=steps
  if L in [12,24,48,72]:
   r,_,_=stabilize((e+1).ravel().tolist(),L);r=np.array(r,dtype=np.int64).reshape(L,L);u,err=potential(r-1);assert not burn_remainder(r).any();row['all_ones_class_differs']=not np.array_equal(e,r);row['cutoff2_potential_differs']=not np.array_equal(v,u)
   samples=[]
   for x,y in [(1/4,1/4),(1/2,1/2),(1/2,1/4),(1/8,1/2)]:
    ii=max(1,min(L,round(x*(L+1))));jj=max(1,min(L,round(y*(L+1))));samples.append([x,y,int(v[jj-1,ii-1])/((L+1)**2)])
   row['potential_samples']=samples
   P.joinpath(f'identity_potential_L{L}.json').write_text(json.dumps({'L':L,'potential':v.tolist(),'identity':e.tolist()}),encoding='utf8')
  row['seconds']=time.monotonic()-start;out.write(json.dumps(row)+'\n');out.flush();print(json.dumps(row),flush=True)
