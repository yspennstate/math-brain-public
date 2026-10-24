"""Finite-volume checks only; no asymptotic claim is based on these samples."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np, json, pathlib, time
ROOT=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(11920261012)

def graph(d,n,positive):
 steps=[]
 for j in range(d):
  v=tuple(int(i==j) for i in range(d)); steps.append(v)
  if not positive: steps.append(tuple(-a for a in v))
 layers=[[(0,)*d]]; pred=[]
 for i in range(1,n):
  prev=layers[-1]; cur=sorted({tuple(a+b for a,b in zip(x,v)) for x in prev for v in steps})
  idx={x:j for j,x in enumerate(prev)}
  lists=[[idx[y] for v in steps if (y:=tuple(a-b for a,b in zip(x,v))) in idx] for x in cur]
  maxlen=max(map(len,lists)); arr=np.full((len(cur),maxlen),-1,dtype=int)
  for j,l in enumerate(lists): arr[j,:len(l)]=l
  pred.append(arr); layers.append(cur)
 succ=[]
 for i in range(n-1):
  lists=[[] for _ in layers[i]]
  for k,l in enumerate(pred[i]):
   for j in l:
    if j>=0: lists[j].append(k)
  arr=np.full((len(lists),max(map(len,lists))),-1,dtype=int)
  for j,l in enumerate(lists): arr[j,:len(l)]=l
  succ.append(arr)
 return layers,pred,succ

def gather(a,idx):
 return np.where(idx[None,:,:]>=0,a[:,np.maximum(idx,0)],-np.inf)

def lse(a,axis):
 m=np.max(a,axis=axis,keepdims=True)
 return (m+np.log(np.exp(a-m).sum(axis=axis,keepdims=True))).squeeze(axis)

def evaluate(xs,gr,beta):
 layers,pred,succ=gr; b=xs[0].shape[0]; n=len(xs)
 alpha=[xs[0] if beta is None else beta*xs[0]]; choices=[]
 for i in range(1,n):
  a=gather(alpha[-1],pred[i-1])
  if beta is None:
   choices.append(np.argmax(a,axis=2)); val=a.max(axis=2)+xs[i]
  else: val=lse(a,2)+beta*xs[i]
  alpha.append(val)
 if beta is None:
  pos=alpha[-1].argmax(axis=1); f=alpha[-1][np.arange(b),pos]
  ps=[np.zeros_like(x) for x in xs]
  for i in range(n-1,-1,-1):
   ps[i][np.arange(b),pos]=1
   if i>0: pos=pred[i-1][pos,choices[i-1][np.arange(b),pos]]
 else:
  z=lse(alpha[-1],1); back=np.zeros_like(xs[-1]); ps=[None]*n
  ps[-1]=np.exp(alpha[-1]-z[:,None])
  for i in range(n-2,-1,-1):
   back=lse(gather(beta*xs[i+1]+back,succ[i]),2)
   ps[i]=np.exp(alpha[i]+back-z[:,None])
  f=z/beta
 for p in ps: assert np.max(np.abs(p.sum(axis=1)-1))<1e-10
 return f,ps

def overlap(a,b): return sum((x*y).sum(axis=1) for x,y in zip(a,b))

def experiment(d,n,positive,beta,samples=2500):
 gr=graph(d,n,positive); times=[0,.01,.1,.5,2.]
 nodes,weights=np.polynomial.laguerre.laggauss(20)
 vals=[]; q0=[]; energy=[]; qs=[[] for _ in times]; integrals=[]
 for start in range(0,samples,250):
  batch=min(250,samples-start)
  xs=[rng.normal(size=(batch,len(l))) for l in gr[0]]
  ys=[rng.normal(size=x.shape) for x in xs]
  f,p=evaluate(xs,gr,beta); vals.extend(f.tolist()); q0.extend(overlap(p,p).tolist())
  energy.extend(sum((x*pp).sum(axis=1) for x,pp in zip(xs,p)).tolist())
  for j,t in enumerate(times):
   xt=[np.exp(-t)*x+np.sqrt(-np.expm1(-2*t))*y for x,y in zip(xs,ys)]
   _,pt=evaluate(xt,gr,beta); qs[j].extend(overlap(p,pt).tolist())
  integ=np.zeros(batch)
  for t,w in zip(nodes,weights):
   xt=[np.exp(-t)*x+np.sqrt(-np.expm1(-2*t))*y for x,y in zip(xs,ys)]
   _,pt=evaluate(xt,gr,beta); integ+=w*overlap(p,pt)
  integrals.extend(integ.tolist())
 result={'d':d,'n':n,'positive_coordinate_steps':positive,'beta':beta,'samples':samples,
  'variance_G_unbiased':float(np.var(vals,ddof=1)),
  'overlap_integral_20_point_laguerre':float(np.mean(integrals)),
  'Q0':float(np.mean(q0)),
  'Q_at_t':{str(t):float(np.mean(q)) for t,q in zip(times,qs)},
  'mean_gibbs_energy':float(np.mean(energy)),
  'description':'Monte Carlo means with fixed seed; quadrature error and sampling error remain, not a proof'}
 if beta:
  residual=np.asarray(energy)-beta*(n-np.asarray(q0))
  result['IBP_residual_mean']=float(residual.mean())
  result['IBP_residual_standard_error']=float(residual.std(ddof=1)/np.sqrt(samples))
  D=d if positive else 2*d
  result['low_temperature_lower_bound']=float(n*(1-np.sqrt(2*np.log(D))/beta))
 return result

def finite_difference():
 gr=graph(3,4,False); xs=[rng.normal(size=(1,len(l))) for l in gr[0]]
 beta=2.; f,p=evaluate(xs,gr,beta); eps=1e-5; errors=[]
 for i,layer in enumerate(xs):
  for j in range(min(4,layer.shape[1])):
   xp=[v.copy() for v in xs]; xm=[v.copy() for v in xs]
   xp[i][0,j]+=eps; xm[i][0,j]-=eps
   fd=(evaluate(xp,gr,beta)[0][0]-evaluate(xm,gr,beta)[0][0])/(2*eps)
   errors.append(abs(fd-p[i][0,j]))
 return {'gradient_max_error':max(errors),'coordinates_checked':len(errors),'epsilon':eps}

if __name__=='__main__':
 begin=time.time(); results={'finite_difference':finite_difference(),'experiments':[]}
 for args in [(3,10,True,None),(3,7,False,4.),(1,10,True,4.)]:
  r=experiment(*args); results['experiments'].append(r)
  (ROOT/'checks_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
  print(json.dumps(r),flush=True)
 results['elapsed_seconds']=time.time()-begin
 (ROOT/'checks_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results['finite_difference']), 'seconds',results['elapsed_seconds'])
