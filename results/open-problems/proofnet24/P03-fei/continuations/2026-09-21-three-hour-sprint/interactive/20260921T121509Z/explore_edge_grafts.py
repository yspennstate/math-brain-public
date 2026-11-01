"""Exploration of balanced monotone grafts on the recovered n18 seed.

All ranking scores are exploratory float64. Final witnesses require a
separate exact reconstruction and rational-interval certificate.
"""
import numpy as np, math, json
from cancellation_composition import fwht, walsh_state, phi
from reconstruct_external_seed import core_and_hosts


def context():
 base, hosts=core_and_hosts()
 a=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
 for h in hosts:a[h]=0
 A=fwht(a).astype(float)/512
 Q=[]
 for lo,hi in hosts:
  assert lo.bit_count()==4 and hi.bit_count()==5
  assert (lo^hi).bit_count()==1
  q=np.zeros(512,dtype=np.int64);q[lo]=1;q[hi]=-1
  Q.append(fwht(q)/512)
 return a,A,np.array(Q),hosts


def entropy(v):
 p=np.asarray(v)**2;m=p>0
 return float(np.sum(-p[m]*np.log2(p[m])))


def main():
 a,A,Q,hosts=context();w=1/256
 H0=entropy(A)+9*16*w;I0=261/128
 r0=H0/(I0-1)
 out={'seed':{'H':H0,'I':I0,'amplified':r0},'majority3_grafts':[]}
 for j in range(9):
  b=.5; hg=2; ig=1.5
  h=entropy(A+b*Q[j])+8*16*w +w*(hg-phi(b*b)+16*(1-b*b))
  i=I0+w*(ig-1)
  out['majority3_grafts'].append({'host':j,'cells':hosts[j],'H':h,'I':i,'amplified':h/(i-1),'delta':h/(i-1)-r0})
 print(json.dumps(out,indent=2))
 from pathlib import Path
 (Path(__file__).resolve().parent/'edge_graft_exploration.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
