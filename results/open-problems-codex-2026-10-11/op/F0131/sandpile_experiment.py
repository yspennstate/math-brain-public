import numpy as np,time,json,math
from numba import njit
from pathlib import Path
@njit(cache=False)
def stabilize(n,H,R):
 L=2*R+1; size=L*L
 a=np.full(size,-H,np.int64);u=np.zeros(size,np.int64);queued=np.zeros(size,np.uint8);q=np.zeros(size,np.int64)
 origin=R*L+R;a[origin]+=n;q[0]=origin;queued[origin]=1;head=0;tail=1;count=1;steps=0
 while count:
  z=q[head];head=(head+1)%size;count-=1;queued[z]=0
  k=a[z]//4
  if k<=0:continue
  if z<L or z>=size-L or z%L==0 or z%L==L-1:raise ValueError('box reached')
  a[z]-=4*k;u[z]+=k;steps+=1
  for w in (z-1,z+1,z-L,z+L):
   a[w]+=k
   if a[w]>=4 and queued[w]==0:
    q[tail]=w;tail=(tail+1)%size;count+=1;queued[w]=1
 return a.reshape((L,L)),u.reshape((L,L)),steps

def check(n,H,a,u,R):
 initial=np.full(a.shape,-H,np.int64);initial[R,R]+=n
 lap=-4*u.copy();lap[1:]+=u[:-1];lap[:-1]+=u[1:];lap[:,1:]+=u[:,:-1];lap[:,:-1]+=u[:,1:]
 assert np.array_equal(a,initial+lap)
 assert np.max(a)<=3 and np.min(a)>=min(-H,0)
 assert int((a+H).sum())==n
 assert np.array_equal(u,u.T) and np.array_equal(u,u[::-1]) and np.array_equal(u,u[:,::-1])
 assert not np.any(u[:2]) and not np.any(u[-2:]) and not np.any(u[:,:2]) and not np.any(u[:,-2:])

if __name__=='__main__':
 Path('experiments').mkdir(exist_ok=True)
 for H in [-2,-1,0,1,2]:
  for n in [1024,4096,16384,65536]:
   R=math.ceil(math.sqrt(n))+8;t=time.perf_counter();a,u,steps=stabilize(n,H,R);check(n,H,a,u,R)
   y,x=np.nonzero(u);x=x-R;y=y-R;ax=int(x.max());diag=int((x+y).max())
   row=dict(H=H,n=n,sites=len(x),axis=ax,diag_integer=diag,diag_axis_ratio=diag/(math.sqrt(2)*ax),steps=steps,seconds=time.perf_counter()-t)
   if H==-2:assert len(x)==(2*ax+1)**2
   for theta in [0,math.pi/12,math.pi/6,math.pi/4]:row['support_'+str(round(theta*180/math.pi))]=float(np.max(x*math.cos(theta)+y*math.sin(theta))/math.sqrt(n))
   with open('experiments/results.jsonl','a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
   np.savez_compressed(f'experiments/H{H}_n{n}.npz',height=a,odometer=u,R=R)
   print(json.dumps(row),flush=True)
