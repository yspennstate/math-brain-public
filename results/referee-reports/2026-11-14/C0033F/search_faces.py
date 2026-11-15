"""60+ digit search of the strict domain and all realizable spectral/graph strata.

Boundary statistics are attained interior values along approaches to the face.
They are not definitions of m on a singular kernel or certified face infima.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource,random,math
from pathlib import Path
import mpmath as mp
from mp_core import evaluate,strict,strings,coordinates,rotation,cyclic

PATH=Path('data/face_search.json')

def number(z):return mp.mpf(str(z))

def lanczos(lam,weights):
 D=mp.diag(lam);u=mp.matrix([number(z) for z in weights]);u/=mp.norm(u);cols=[];old=mp.zeros(3,1);beta=0
 for i in range(3):
  cols.append(u);w=D*u-beta*old;alpha=(u.T*w)[0];w-=alpha*u
  for c in cols:w-=(c.T*w)[0]*c
  if i<2:beta=mp.norm(w);old=u;u=w/beta
 V=mp.matrix([[cols[j][i] for j in range(3)] for i in range(3)])
 return V.T

def make(desc):
 L=number(desc['L']);k0,k1=desc['spec'];nmid=3-k0-k1
 target=[mp.mpf(0)]*k0+[1/(1+mp.exp(-number(z))) for z in desc['middle']]+[mp.mpf(1)]*k1
 lam=[]
 for i,l in enumerate(target):
  if l==0:lam.append(mp.exp(-L*number(desc['rates'][i])))
  elif l==1:lam.append(1-mp.exp(-L*number(desc['rates'][i])))
  else:lam.append(l)
 graph=desc['graph']
 if graph=='triangle':
  aa=[mp.pi/(2*(1+mp.exp(-number(z)))) for z in desc['angles']]
  U=rotation(1,2,aa[2])*rotation(0,2,aa[1],number(desc['phase']))*rotation(0,1,aa[0])
 elif graph=='path':
  U=lanczos(target,desc['weights'])
 elif graph=='block':
  order=desc['order'];lam=[lam[i] for i in order]
  U=rotation(1,2,mp.pi/(2*(1+mp.exp(-number(desc['angles'][0])))))
 elif graph=='diagonal':U=mp.eye(3)
 else:raise ValueError(graph)
 if graph in ('block','diagonal'):
  pp=[number(z) for z in desc['perturb']]
  U=rotation(0,1,mp.exp(-L*pp[0]))*rotation(0,2,mp.exp(-L*pp[1]),number(desc['phase']))*rotation(1,2,mp.exp(-L*pp[2]))*U
 q=U*mp.diag(lam)*U.H
 return (q+q.H)/2

def descriptor(rng,graph,spec,L,j):
 k0,k1=spec;nmid=3-k0-k1
 mid=sorted([rng.uniform(-3,3) for _ in range(nmid)])
 if nmid==3 and j%3==0:mid=sorted([rng.uniform(-.3*L,.3*L) for _ in range(3)])
 d=dict(graph=graph,spec=list(spec),L=L,middle=mid,rates=[rng.uniform(.35,2.5) for _ in range(3)],angles=[rng.uniform(-3,3) for _ in range(3)],phase=rng.uniform(-math.pi,math.pi),weights=[rng.uniform(.2,1) for _ in range(3)],perturb=[rng.uniform(.15,2) for _ in range(3)])
 if graph=='triangle' and j%3==1:d['angles']=[rng.uniform(-.5,.5)*L for _ in range(3)]
 if graph=='block':
  target=[0]*k0+list(range(2,2+nmid))+[1]*k1
  orders=[]
  for i in range(3):
   rest=[z for z in range(3) if z!=i]
   if target[rest[0]]!=target[rest[1]]:orders.append([i]+rest)
  if not orders:return None
  d['order']=rng.choice(orders)
 if graph=='path' and spec not in [(0,0),(1,0),(0,1),(1,1)]:return None
 if graph=='triangle' and spec in [(3,0),(0,3)]:return None
 return d

def main():
 rng=random.Random(33603);start=time.monotonic();out=dict(seed=33603,groups={},failures=[],attempts=0,negative=[],precision_rule='120+ceil(12 L/log(10)); all atom arithmetic mpmath',thread_count=1)
 def save():
  out.update(seconds=time.monotonic()-start,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20,priority=os.getpriority(os.PRIO_PROCESS,0))
  tmp=PATH.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(PATH)
 def test(d):
  name=f"{d['graph']}_{d['spec'][0]}_{d['spec'][1]}";g=out['groups'].setdefault(name,dict(attempts=0,accepted=0,minimum_product=None,minimum_margin=None,by_L={}))
  out['attempts']+=1;g['attempts']+=1
  mp.mp.dps=120+math.ceil(12*d['L']/math.log(10))
  try:
   q=make(d)
   if not strict(q):raise ArithmeticError('not strict')
   ev=evaluate(q);val=ev['logscale']*ev['margin'];g['accepted']+=1
   row=dict(descriptor=d,precision=mp.mp.dps,**strings(dict(margin=ev['margin'],Lambda=ev['logscale'],product=val,pmin=ev['pmin']),70))
   if g['minimum_product'] is None or val<number(g['minimum_product']['product']):g['minimum_product']=row
   if g['minimum_margin'] is None or ev['margin']<number(g['minimum_margin']['margin']):g['minimum_margin']=row
   ll=str(d['L']);gg=g['by_L'].setdefault(ll,dict(accepted=0,minimum=None));gg['accepted']+=1
   if gg['minimum'] is None or val<number(gg['minimum']['product']):gg['minimum']=row
   if ev['margin']<0:out['negative'].append(row);save();raise RuntimeError('negative margin; must audit')
  except (ValueError,ArithmeticError,ZeroDivisionError) as err:
   if len(out['failures'])<100:out['failures'].append(dict(descriptor=d,error=str(err),precision=mp.mp.dps))
  if out['attempts']%100==0:save()
 specs=[(0,0),(1,0),(0,1),(2,0),(0,2),(1,1),(2,1),(1,2),(3,0),(0,3)]
 for L in (10,40,120,300):
  for graph in ('triangle','path','block','diagonal'):
   for spec in specs:
    for j in range(50):
     d=descriptor(rng,graph,spec,L,j)
     if d is not None:test(d)
   print('done',L,graph,out['attempts'],time.monotonic()-start,flush=True);save()
 save();print('complete',out['attempts'],out['seconds'],flush=True)
if __name__=='__main__':main()
