#!/usr/bin/env python3
"""Class catalog and exact-integer Rayleigh/stability falsification grid.
Passing the finite grid is only a necessary condition, never a certificate.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import csv,itertools,json
import numpy as np

out=[]
for n in range(1,5):
    r=np.load(f'census_n{n}.npz'); w=r['weights']; N,m=w.shape
    # Real fields are integers to keep every evaluated inequality exact.
    fields=[-4,-2,-1,0,1,2,4]
    stable=np.ones(N,bool); rayleigh=np.ones(N,bool); witness=None
    for i in range(n):
        for j in range(i+1,n):
            others=[k for k in range(n) if k not in [i,j]]
            for vals in itertools.product(fields,repeat=len(others)):
                cs=[np.zeros(N,dtype=np.int64) for _ in range(4)]
                for s in range(m):
                    fac=1
                    for k,t in zip(others,vals):
                        if s>>k&1: fac*=t
                    cs[((s>>i)&1)+2*((s>>j)&1)]+=w[:,s]*fac
                delta=cs[1]*cs[2]-cs[0]*cs[3]; fail=delta<0
                if witness is None and np.any(fail&r['NA']):
                    t=int(np.flatnonzero(fail&r['NA'])[0])
                    witness=dict(table=t,pair=[i,j],other_coordinates=others,fields=list(vals),delta_numerator=int(delta[t]))
                stable &= ~fail
                if all(t>=0 for t in vals): rayleigh &= ~fail
    out.append(dict(n=n,real_field_grid=fields,stable_grid_survivors=int(stable.sum()),NA_stable_grid_survivors=int((stable&r['NA']).sum()),positive_field_grid_survivors=int(rayleigh.sum()),NA_not_stable_witness=witness))
    if n==4:
        groups={}
        permutations=list(itertools.permutations(range(n)))
        maps=[[sum(((s>>j)&1)<<perm[j] for j in range(n)) for s in range(m)] for perm in permutations]
        for t in np.flatnonzero(r['logsub']):
            key=min(tuple(int(w[t,s]) for s in smap) for smap in maps)
            if key not in groups:groups[key]=dict(table=int(t),count=0,NA=bool(r['NA'][t]),product=bool(r['product'][t]),I=float(r['I'][t]),erasure=float(r['erasure'][t]),stable_grid_pass=bool(stable[t]))
            groups[key]['count']+=1
        with open('logsub_catalog.csv','w') as f:
            c=csv.writer(f);c.writerow(['representative_table','function_count','NA','product','I','erasure_bits','stable_grid_pass','canonical_weight_numerators_denominator_256'])
            for key,row in sorted(groups.items(),key=lambda x:x[1]['table']):
                c.writerow([row[k] for k in ['table','count','NA','product','I','erasure','stable_grid_pass']]+[' '.join(map(str,key))])
        out[-1]['logsub_spectrum_types_mod_coordinate_permutations']=len(groups)
        out[-1]['NA_and_logsub']=int((r['NA']&r['logsub']).sum())
        out[-1]['NA_not_logsub']=int((r['NA']&~r['logsub']).sum())
        out[-1]['logsub_not_NA']=int((~r['NA']&r['logsub']).sum())
with open('structural.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
