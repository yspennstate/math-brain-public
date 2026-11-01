"""Exact complete-flow comparison of all64 two-block transfer words."""
from pathlib import Path
import json
import numpy as np
from continuation_20261003_global_colored_transfer_search import word_orbits,COLORS


def main():
 F=json.loads(Path(__file__).with_name('continuation_20261002_cube8_flow_and_smoothing.json').read_text())['Fourier_polynomial']
 q=4;x,y=np.divmod(np.arange(q*q),q);k,l=x.copy(),y.copy()
 indices=[x[:,None]^y[:,None],x[:,None]^l[None,:],k[None,:]^y[:,None]]
 H=np.array([[(-1)**((i&j).bit_count()) for j in range(q)] for i in range(q)],dtype=object)
 rng=np.random.default_rng(635343);records=[];words=word_orbits()
 for t in range(12):
  plus=np.array(rng.integers(1,10,size=q),dtype=object);minus=np.array(rng.integers(1,10,size=q),dtype=object)
  a=plus+minus;b=plus-minus;profiles=[a,b];M={}
  for name,color in COLORS.items():
   m=np.ones((q*q,q*q),dtype=object)
   for c,index in zip(color,indices):m*=profiles[c][index]
   M[name]=m
  r=[None]*8;r[::2]=list(H@a);r[1::2]=list(H@b);flows={k:0 for k in words}
  for raw,c in F.items():
   n=tuple(map(int,raw.split(',')));size=sum(n[1::2]);v=c
   for j,power in enumerate(n):v*=int(r[j])**power
   flows[size]+=v
  literal={}
  for size,orbits in words.items():
   value=0
   for word,coefficient in orbits.items():
    matrix=M[word[0]]
    for name in word[1:]:matrix=matrix@M[name]
    value+=coefficient*sum(matrix[i,i] for i in range(q*q))
   literal[size]=int(q**5*value)
  assert literal==flows
  records.append({'plus':list(map(int,plus)),'minus':list(map(int,minus)),
                  'coefficients':{str(k):str(v) for k,v in literal.items()},'all_complete_flow_coefficients_match':True})
 out={'status':'PASS twelve exact complete-flow and all-colored transfer comparisons','word_count':sum(sum(c.values()) for c in words.values()),
      'orbits':{str(k):[{'word':w,'coefficient':c} for w,c in C.items()] for k,C in words.items()},'records':records}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print('PASS all5 coefficient groups,12 exact cases')
if __name__=='__main__':main()
