import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json,math
from pathlib import Path
import numpy as np
from compute import metrics
rows=[]
for k in [1,2,3,4,8,16,32,64]:
    data_gap=math.log2(2-2.**(-k));address_gap=math.log2(8/3)
    row=dict(k=k,data_Inf=2.**(-k),data_gap_bits=data_gap,data_local_charge_constant=data_gap*2.**k,
             uniform_coordinate_charge_constant=(k*address_gap+2.**k*data_gap)/(1+k/2))
    if k<=3:
        n=k+(1<<k);N=1<<n;x=np.arange(N,dtype=np.int64);f=1-2*((x>>(k+(x&((1<<k)-1))))&1)
        d=metrics(f);checks=[]
        for i in [0,k]:
            lo=x[(x&(1<<i))==0];d0=metrics(f[lo]);d1=metrics(f[lo|(1<<i)])
            observed=float(d['L'][0,0]-(d0['L'][0,0]+d1['L'][0,0])/2)
            expected=address_gap if i==0 else data_gap
            assert abs(observed-expected)<1e-12
            checks.append(dict(coordinate=i,kind='address' if i==0 else 'data',observed_gap_bits=observed,expected_gap_bits=expected,Inf=float(d['up'][0,1<<i])))
        row['truth_table_checks']=checks
    rows.append(row)
Path('restriction_address.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
