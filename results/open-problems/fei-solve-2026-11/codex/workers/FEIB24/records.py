"""Reconstruct the reported structured examples directly from literal DNFs."""
import itertools,json
import numpy as np
from analysis import evaluate
terms=[]
for g in range(3):
 for choices in itertools.product(range(2),repeat=3):terms.append(sum(1<<(6*g+2*j+c) for j,c in enumerate(choices)))
idx=np.arange(1<<18);f=np.full(len(idx),-1,dtype=np.int8)
for term in terms:f[(idx&term)==term]=1
assert np.array_equal(f,np.load('witnesses/profile_best.npz')['f'])
s=evaluate(f)
row=dict(formula='OR_{g=0..2} AND_{j=0..2} (x_{6g+2j+1} OR x_{6g+2j+2})',minterms=terms,dnf=' OR '.join('('+' AND '.join('x%d'%(i+1) for i in range(18) if t>>i&1)+')' for t in terms),stats=s)
json.dump(row,open('record18.json','w'),indent=2)
idx=np.arange(1<<20);f=np.full(len(idx),-1,dtype=np.int8)
for j in range(10):f[(idx>>(2*j)&3)==3]=1
np.savez_compressed('witnesses/tribes_10x2.npz',f=f)
json.dump(evaluate(f),open('tribes_10x2.json','w'),indent=2)
print('literal DNF reconstructions passed')
