"""Independent direct high-precision convolution checks, plus FFT cap comparisons."""
import os
for v in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[v]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import mpmath as mp, numpy as np, json, time
from scipy.fft import next_fast_len
from iterate import initial,advance
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
mp.mp.dps=70

def convolution(a,b,K):
 out=[mp.mpf(0)]*(min(K+1,len(a)+len(b)-1))
 for i,x in enumerate(a):
  if not x:continue
  for j in range(min(len(b),len(out)-i)):
   if b[j]:out[i+j]+=x*b[j]
 return out

out=[]
for m,b in [(2,2),(2,5),(3,1),(3,3)]:
 t=time.monotonic();K=128;steps=100
 p=mp.mpf(1)/(1+((m-1)*b-1)*m**b)
 a=[mp.mpf(0)]*(b+1);a[0]=1-p;a[b]=p*m**b
 af=initial(m,b,K,np.float64); w=np.exp(-np.arange(K+1)*np.log(float(m)))
 N=next_fast_len(m*K+1)
 for n in range(steps):
  conv=a
  for j in range(m-1):conv=convolution(conv,a,K+1)
  an=[x/m for x in conv[1:K+2]]
  # output 0 contains convolution coefficients 0 and 1, but normalization is more stable.
  an[0]=1-mp.fsum(an[k]*mp.mpf(m)**(-k) for k in range(1,len(an)))
  a=an
  af,_=advance(af,m,N,w)
 q=mp.fsum(a[k]*mp.mpf(m)**(-k) for k in range(1,len(a)))
 mu=mp.fsum(k*a[k]*mp.mpf(m)**(-k) for k in range(1,len(a)))
 qf=np.dot(af[1:],w[1:]);muf=np.dot(np.arange(1,K+1)*af[1:],w[1:])
 row={'m':m,'b':b,'n':steps,'cap':K,'dps':mp.mp.dps,'n2_q_mp':str(steps**2*q),
      'n2_mean_mp':str(steps**2*mu),'q_relative_fft_error':float(abs(mp.mpf(float(qf))/q-1)),
      'mean_relative_fft_error':float(abs(mp.mpf(float(muf))/mu-1)),
      'seconds':time.monotonic()-t}
 out.append(row);print(row,flush=True)
(ROOT/'data'/'direct_mp_checks.json').write_text(json.dumps(out,indent=2))
