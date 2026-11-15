"""NUMERICAL independent matrix audit, not a proof or a covering argument."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json
from pathlib import Path
import numpy as np
from map_residual import value,moments,endpoint,chart_excluded,residual

def direct(u,w,a,r,N):
    lam=(2+a*(1+r))/4;Q=np.outer(u,u)+np.outer(w,w)
    L5=lam*(np.eye(5)-np.ones((5,5))/5)-a*np.outer(u,u)-a*r*np.outer(w,w)
    L=np.zeros((N,N));L[:5,:5]=L5
    G=lam*(np.eye(N)-np.ones((N,N))/N)-L
    Pi=np.zeros((N,N));Pi[:5,:5]=np.eye(5)-np.ones((5,5))/5-Q
    X1=2*(lam*np.trace(G)-np.sum(G*G));X2=2*N/(N-2)*np.sum(Pi*G*G)
    X3=(1-lam)/(N-2)*(2*np.trace(G)-2*N/(N-2)*np.sum(np.diag(Pi)*np.diag(G)))
    S5=0.
    for i in range(5):
        for j in range(i+1,5):S5+=-L5[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j])
    return X1+X2+X3-2*S5

def main():
    data=np.load('residual_samples.npz');maxerr=0.;mins={N:float('inf')for N in(6,7,10)};n=len(data['r'])
    for i in range(n):
        u,w,r,a=data['u'][i],data['w'][i],float(data['r'][i]),float(data['a'][i]);m=moments(u,w)
        assert residual(u,w,r,a)is not None
        for N in mins:
            T=direct(u,w,a,r,N);mins[N]=min(mins[N],T)
            if N==6:maxerr=max(maxerr,abs(T-value(m,a,r)))
            if T<0:raise RuntimeError('Negative matrix candidate at '+str((i,N,T)))
    mm=json.load(open('residual_map.json'))['minima']['T'];u,w=np.array(mm['u']),np.array(mm['w']);least=direct(u,w,mm['a'],mm['r'],6)
    maxerr=max(maxerr,abs(least-mm['T']));assert maxerr<1e-11
    out=dict(label='NUMERICAL',points=n,all_filters_rechecked=True,max_T6_formula_matrix_discrepancy=maxerr,direct_matrix_minima_on_N6_residual_sample=mins,least_local_T6_direct=least)
    Path('numeric_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
    with open('LOG.md','a')as f:f.write('\nNUMERICAL: independent full-matrix audit rechecked all '+str(n)+' residual samples and every numerical filter. Maximum N=6 formula discrepancy '+str(maxerr)+'. N=6,7,10 sample minima '+str(mins)+'. None negative; N=7,10 values refer to the N=6 residual sample, not samples of their full residual domains.\n')
if __name__=='__main__':main()
