"""Independent exhaustive edge-subset audit of symbolic K_{m,s} proof.

Does not call the transfer constructors or any partition-state routine.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json
import sys


def direct(m,s,weight):
    edges=[(i,m+j)for j in range(s)for i in range(m)]
    marked={'same_hub':(0,1),'same_terminal':(0,m),'disjoint':(0,m+1)}
    n=m+s
    Z=0;single=[0]*len(edges);joint={kind:0 for kind in marked}
    for mask in range(1<<len(edges)):
        parent=list(range(n));cyclic=False
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for i,(u,v)in enumerate(edges):
            if mask>>i&1:
                a,b=root(u),root(v)
                if a==b:cyclic=True;break
                parent[a]=b
        if cyclic:continue
        k=mask.bit_count();Z+=weight**k
        for i in range(len(edges)):
            if mask>>i&1:single[i]+=weight**(k-1)
        for kind,(i,j)in marked.items():
            if mask>>i&1 and mask>>j&1:joint[kind]+=weight**(k-2)
    return {kind:single[i]*single[j]-Z*joint[kind]for kind,(i,j)in marked.items()}


def evaluate_certificate(cert,s,weight):
    t=s-2;a=1+cert['m']*weight
    out={}
    for kind,entry in cert['types'].items():
        P=sum(comb(t,k)*sum(F(v)*weight**int(i)for i,v in row.items())for k,row in enumerate(entry['coefficients'])if k<=t)
        out[kind]=P*F(a)**(2*s-2*cert['m'])
    return out


def main():
    folder=Path(__file__).parent
    certs=[]
    for name in ['complete_bipartite_symbolic_results.json','complete_bipartite_symbolic_results_7_8.json']:
        certs+=json.loads((folder/name).read_text())
    reports=[]
    for m,s in [(3,2),(3,3),(4,2),(4,3),(5,2),(5,3),(6,2),(6,3),(7,2),(8,2)]:
        cert=next(c for c in certs if c['m']==m)
        for weight in [1,2]:
            expected=evaluate_certificate(cert,s,weight)
            actual=direct(m,s,weight)
            assert expected==actual,(m,s,weight,expected,actual)
            assert all(v>0 for v in actual.values())
            reports.append({'m':m,'s':s,'lambda':weight,'rayleigh_differences':{k:str(v)for k,v in actual.items()},'exact_transfer_match':True})
            print('verified',m,s,weight,flush=True)
    for c in certs:
        for kind,entry in c['types'].items():
            assert all(F(v)>=0 for row in entry['coefficients']for v in row.values())
            assert any(F(v)>0 for v in entry['coefficients'][0].values())
    report={'independent_direct_checks':reports,'coefficient_sign_checks':len(certs)*3,'all_passed':True}
    (folder/'complete_bipartite_direct_audit_results.json').write_text(json.dumps(report,indent=2))
    print('All exact direct enumeration and coefficient sign checks passed.',flush=True)


if __name__=='__main__':main()
