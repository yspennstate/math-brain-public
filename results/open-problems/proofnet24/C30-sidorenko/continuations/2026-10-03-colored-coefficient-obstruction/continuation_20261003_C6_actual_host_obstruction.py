"""Exact counterexample to positivity of every binary colored coefficient.
All arithmetic is integral; the identity is the previously regenerated two-block
trace expansion. The independent ant checker uses literal source masks and
translation character blocks, without importing this file.
"""
from pathlib import Path
import json
import numpy as np
from continuation_20261003_global_colored_transfer_search import COLORS,word_orbits

def coefficients(a,b):
 q=len(a);x,y=np.divmod(np.arange(q*q),q);u,v=x.copy(),y.copy()
 indices=[x[:,None]^y[:,None],x[:,None]^v[None,:],u[None,:]^y[:,None]]
 profiles=[np.array(a,dtype=object),np.array(b,dtype=object)];M={}
 for name,color in COLORS.items():
  m=np.ones((q*q,q*q),dtype=object)
  for c,index in zip(color,indices):m*=profiles[c][index]
  M[name]=m
 values={}
 for degree,words in word_orbits().items():
  value=0
  for word,c in words.items():
   m=M[word[0]]
   for name in word[1:]:m=m@M[name]
   value+=c*sum(m[i,i] for i in range(q*q))
  values[degree]=int(q**5*value)
 return values

def main():
 a=[3,3,503,3,3,503,3,503];b=[-1,2,0,2,2,0,-2,0]
 assert all(x>abs(y) for x,y in zip(a,b))
 values=coefficients(a,b);den=sum(a)**15
 assert values[6]==-809116997184077332220240713482240
 out={'status':'EXACT counterexample to all binary colored coefficients being nonnegative; not a Sidorenko counterexample',
 'q':8,'full_host_size':16,'a':a,'b':b,'normalizing_sum':sum(a),
 'kernel_definition':'W((t,x),(s,y))=8*(a[x xor y]+(-1)^(t+s)*b[x xor y])/1524',
 'strictly_positive_kernel_min_numerator':8*min(x-abs(y) for x,y in zip(a,b)),
 'kernel_min_denominator':sum(a),'density_coefficient_denominator':str(den),
 'colored_coefficient_numerators':{str(k):str(v) for k,v in values.items()},
 'total_binary_averaging_difference_numerator':str(sum(v for k,v in values.items() if k)),
 'full_host_density_numerator':str(sum(values.values())),
 'averaged_host_density_numerator':str(values[0]),
 'total_averaging_difference_is_positive':sum(v for k,v in values.items() if k)>0,
 'independent_checker':'global_colored_ant_exact_obstruction_check.py'}
 assert out['total_averaging_difference_is_positive']
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
