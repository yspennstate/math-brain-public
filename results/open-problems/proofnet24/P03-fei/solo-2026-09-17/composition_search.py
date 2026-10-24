#!/usr/bin/env python3
"""Compact exact-identity recursion for disjoint NAND compositions.

Means and coefficients start dyadic; this explorer uses floating arithmetic.
The recurrence itself is algebraically exact; results are not certificates.
"""
import json
import math
from pathlib import Path
import numpy as np
from experiments import walsh, ent_terms, stats


def h(x):
    x=np.asarray(x,dtype=float)
    return ent_terms(x)


def edge(r,s):
    # Stable homogeneous binary-entropy formula, including zero masses.
    r,s=np.broadcast_arrays(np.asarray(r,dtype=float),np.asarray(s,dtype=float))
    m=r+s
    t=np.divide(r,m,out=np.zeros_like(m),where=m>0)
    return m*(h(t)+h(1-t))


def indicator_state(a):
    N=len(a); n=N.bit_length()-1
    w=walsh(a); coeff=w/N
    alpha=float(a.mean())
    singles=coeff[[1<<i for i in range(n)]]
    B=0.0
    for i in range(n):
        q=coeff.reshape(-1,2,1<<i)**2
        B+=float(edge(q[:,0,:],q[:,1,:]).sum())
    return dict(alpha=alpha,singles=singles,H=float(h(coeff**2).sum()),B=B,multiplicity=1,n=n)


def boolean_metrics(st):
    alpha=st['alpha']; t=st['singles']; mult=st['multiplicity']
    H=4*st['H']-4*float(h(alpha**2))-8*alpha*(1-alpha)+float(h((1-2*alpha)**2))
    B=4*st['B']+mult*float((edge((1-2*alpha)**2,4*t*t)-4*edge(alpha**2,t*t)).sum())
    I=mult*float((2*np.abs(t)).sum())
    return dict(n=st['n'],alpha=alpha,H=H,B=B,I=I,
                H_over_I=H/I if I else 0,B_over_I=B/I if I else 0)


def nand(st,k=2):
    alpha=st['alpha']; t=st['singles']; mult=st['multiplicity']
    p=alpha**k; factor=alpha**(k-1); newt=-factor*t
    return dict(alpha=1-p,singles=newt,multiplicity=k*mult,n=k*st['n'],
        H=k*factor*st['H']+float(h((1-p)**2)-h(p*p)),
        B=k*factor*st['B']+k*mult*float((edge((1-p)**2,newt*newt)-edge(p*p,newt*newt)).sum()))


def verify():
    records=[]
    for n in range(1,5):
        for m in range(1,(1<<n)):
            a=(np.arange(1<<n)<m).astype(np.int64)
            st=indicator_state(a)
            for k in [2,3]:
                if n*k>12:continue
                prod=a.copy()
                for _ in range(k-1):prod=np.kron(prod,a)
                truth=1-prod
                direct=stats(1-2*truth)
                comp=boolean_metrics(nand(st,k))
                for name in ['H','B','I']:
                    assert abs(comp[name]-float(direct[name]))<1e-9,(n,m,k,name,comp,direct)
                records.append([n,m,k])
    return {'checked_compositions':len(records),'status':'floating consistency check of exact recurrence'}


def main():
    output={'verification':verify(),'runs':[]}
    phi=(math.sqrt(5)-1)/2
    for nbase in [8,12,16,20]:
        N=1<<nbase
        for target in [phi,2/3,1/3,0.5]:
            m=round(target*N)
            st=indicator_state((np.arange(N)<m).astype(np.int64))
            seq=[]
            for depth in range(51):
                rec=boolean_metrics(st); rec['depth']=depth
                if rec['I']<1e-8 or not (1e-8<rec['alpha']<1-1e-8):break
                seq.append(rec)
                st=nand(st)
            output['runs'].append({'base_dimension':nbase,'base_size':m,'target_bias':target,'sequence':seq})
    Path('composition_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output['verification']))
    for row in output['runs']:
        best=max(row['sequence'],key=lambda x:x['B_over_I'])
        print(json.dumps({'base_dimension':row['base_dimension'],'bias':row['target_bias'],'best':best}))


if __name__=='__main__':main()
