"""Deterministic law iteration, not Monte Carlo. Floating point evidence only.

Store a[k]=m**k P(X=k), convolve the positive part by FFT, keep k<=K,
and move discarded ordinary probability to zero. Separate the delta mass
before FFT to avoid cancellation at survival probabilities of order n^-2.
No projection onto the critical manifold is used.
"""
import os
for v in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
 os.environ[v]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10: os.setpriority(os.PRIO_PROCESS,0,10)
import argparse, json, csv, time, math, resource
from pathlib import Path
import numpy as np
from scipy.fft import rfft, irfft, next_fast_len
ROOT=Path(__file__).resolve().parents[1]

def initial(m,b,K,dtype):
 a=np.zeros(K+1,dtype=dtype)
 p=dtype(1)/(1+dtype((m-1)*b-1)*dtype(m)**b)
 a[0]=1-p; a[b]=p*dtype(m)**b
 return a

def advance(a,m,N,w,active=None):
 b=a.copy(); b[0]=0; a0=a[0]
 f=rfft(b,n=N,workers=1)
 # positive-index coefficients of (a0 + B)^m
 conv=irfft(f*f,n=N,workers=1)
 if m==3:
  conv=3*a0*conv+irfft(f*f*f,n=N,workers=1)
 K=len(a)-1
 out=np.zeros_like(a)
 M=K if active is None else min(K,m*active-1)
 out[1:M+1]=conv[2:M+2]
 linear_stop=min(M,K-1)
 out[1:linear_stop+1]+=m*a0**(m-1)*a[2:linear_stop+2]
 out[1:]/=m
 negative=-np.minimum(out[1:],0).sum()
 np.maximum(out,0,out=out)
 out[0]=1-np.dot(out[1:len(w)],w[1:])
 return out,float(negative)

def metrics(a,m,n,w,rs):
 k=np.arange(len(w),dtype=a.dtype); p=a[:len(w)]*w; q=p[1:].sum()
 row={'n':n,'n2_q':float(n*n*q),'q':float(q),'tilted_mass':float(a.sum()),
      'critical_defect':float(np.dot((m-1)*np.arange(len(a),dtype=a.dtype)-1,a))}
 for r in rs:
  mu=np.dot(k[1:]**r,p[1:]); row['n2_moment_'+str(r)]=float(n*n*mu)
  row['conditional_moment_'+str(r)]=float(mu/q) if q else 0
 for j in range(1,11):row['cond_p_'+str(j)]=float(p[j]/q) if q else 0
 target=(m-1)*np.power(float(m),-np.arange(1,100,dtype=float))
 cond=np.asarray(p[1:100]/q,dtype=float)
 row['conditional_TV_99']=float((np.abs(cond-target).sum()+abs(1-cond.sum())+m**(-99))/2)
 return row

def run(m,b,K,steps,dtype,tag):
 typ=np.longdouble if dtype=='longdouble' else np.float64
 # All representable weights; exponential underflow is recorded as floating-point error.
 w=np.power(typ(m),-np.arange(K+1,dtype=typ))
 a=initial(m,b,K,typ); active=b; N=next_fast_len(m*K+1); rs=[0.5,1.0,2.0,3.0]
 rows=[]; neg=0.; t=time.monotonic()
 checkpoints=set([1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,steps])
 for n in range(steps+1):
  if n in checkpoints:
   z=metrics(a,m,n,w,rs);z['negative_tilted_mass_clipped_cumulative']=neg;rows.append(z)
   print(tag,n,z['n2_q'],z['n2_moment_1.0'],z['critical_defect'],round(time.monotonic()-t,1),flush=True)
  if n<steps:
   N_step=next_fast_len(m*active+1)
   a,d=advance(a,m,N_step,w,active=active);neg+=d
   active=min(K,m*active-1)
 path=ROOT/'data'/f'{tag}.csv'
 with path.open('w') as f:
  writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
 meta={'m':m,'initial_support':[0,b],'initial_positive_probability':str(1/(1+((m-1)*b-1)*m**b)),
       'cap':K,'steps':steps,'dtype':str(np.dtype(typ)),'mantissa_bits':np.finfo(typ).nmant,
       'maximum_fft_length':N,'reachable_support_mask':True,'workers':1,'nice':os.getpriority(os.PRIO_PROCESS,0),
       'seconds':time.monotonic()-t,'maxrss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
       'numerics':'Floating point; cutoff and roundoff are distinct. Not an interval certificate.'}
 (ROOT/'data'/f'{tag}_metadata.json').write_text(json.dumps(meta,indent=2))
 return a
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--m',type=int,required=True);p.add_argument('--b',type=int,required=True)
 p.add_argument('--cap',type=int,default=16384);p.add_argument('--steps',type=int,default=10000)
 p.add_argument('--dtype',choices=['longdouble','float64'],default='longdouble');p.add_argument('--tag',required=True)
 args=p.parse_args();run(args.m,args.b,args.cap,args.steps,args.dtype,args.tag)
