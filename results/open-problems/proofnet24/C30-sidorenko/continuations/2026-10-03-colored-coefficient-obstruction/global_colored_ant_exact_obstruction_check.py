#!/usr/bin/env python3
"""Independent exact colored ML10 check from literal even edge subsets.

No imports of an author checker, flow enumeration, or transfer-word list.
"""
from collections import Counter
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent

def edge_patterns():
    # Five rung edges and ten crossing edges form C10 plus its diameters.
    edges=[]
    for i in range(5):
        edges += [((i,0),(i,1)),((i,0),((i+1)%5,1)),
                  ((i,1),((i+1)%5,0))]
    patterns=[]
    for mask in range(1<<15):
        degrees=Counter()
        for j,(u,v) in enumerate(edges):
            if mask>>j&1:degrees[u]+=1;degrees[v]+=1
        if all(d%2==0 for d in degrees.values()):
            patterns.append(tuple(tuple((mask>>(3*i+j))&1 for j in range(3))
                                  for i in range(5)))
    assert len(patterns)==64
    assert Counter(sum(sum(x)for x in p) for p in patterns)=={0:1,4:5,6:15,8:30,10:13}
    return patterns

def block_matrices(a,b):
    q=len(a);profiles=(np.array(a,dtype=object),np.array(b,dtype=object))
    H=np.array([[(-1)**((chi&u).bit_count()) for u in range(q)] for chi in range(q)],dtype=object)
    matrices={}
    for c0 in range(2):
        for c1 in range(2):
            for c2 in range(2):
                key=(c0,c1,c2)
                matrices[key]=np.array([[[profiles[c0][g]*sum(
                    H[chi,t]*profiles[c1][t^h]*profiles[c2][t^g]
                    for t in range(q)) for h in range(q)]for g in range(q)]for chi in range(q)],dtype=object)
    return matrices

def full_matrices(a,b):
    q=len(a);profiles=(np.array(a,dtype=object),np.array(b,dtype=object))
    x,y=np.divmod(np.arange(q*q),q)
    i=x[:,None]^y[:,None];j=x[:,None]^y[None,:];k=x[None,:]^y[:,None]
    return {(c0,c1,c2):profiles[c0][i]*profiles[c1][j]*profiles[c2][k]
            for c0 in range(2)for c1 in range(2)for c2 in range(2)}

def group_traces(patterns,matrices,blocks):
    values=Counter()
    for p in patterns:
        M=matrices[p[0]]
        for triple in p[1:]:M=M@matrices[triple]
        trace=sum(np.trace(x)for x in M) if blocks else np.trace(M)
        values[sum(sum(x)for x in p)]+=int(trace)
    return values

def direct_fourier_C6(patterns,a,b):
    # Independent edge-frequency Kirchhoff flow formula. Each of the three
    # quotient frequency bits is any of the 64 even subsets of the graph.
    q=len(a)
    assert q==8
    H=np.array([[(-1)**((i&j).bit_count())for j in range(q)]for i in range(q)],dtype=object)
    fourier=(H@np.array(a,dtype=object),H@np.array(b,dtype=object))
    bits=np.array([sum((list(t)for t in p),[])for p in patterns],dtype=np.uint8)
    i,j,k=np.indices((64,64,64),dtype=np.uint8)
    frequencies=(bits[i.reshape(-1)]+2*bits[j.reshape(-1)]+4*bits[k.reshape(-1)])
    total=0
    for p in patterns:
        selected=sum((list(t)for t in p),[])
        if sum(selected)!=6:continue
        product=np.ones(64**3,dtype=object)
        for edge,color in enumerate(selected):product*=fourier[color][frequencies[:,edge]]
        total+=sum(product)
    return int(total)

def main():
    patterns=edge_patterns();q=8
    a=(3,3,503,3,3,503,3,503)
    b=(-1,2,0,2,2,0,-2,0)
    assert sum(a)==1524 and all(x>abs(y)for x,y in zip(a,b))
    block=group_traces(patterns,block_matrices(a,b),True)
    full=group_traces(patterns,full_matrices(a,b),False)
    assert block==full
    coefficients={k:q**5*v for k,v in block.items()}
    expected=-809116997184077332220240713482240
    assert coefficients[6]==expected<0
    flow=direct_fourier_C6(patterns,a,b)
    assert flow==expected
    # A strictly positive 16-state actual convolution kernel has mean one.
    denominator=sum(a)**15
    report={'status':'PASS exact actual-host negative C6; no Sidorenko counterexample claimed',
            'q':q,'full_host_states':2*q,'a_integer':a,'b_integer':b,
            'profile_denominator':sum(a),'mean_kernel':1,
            'actual_kernel_minimum':f'{q*min(x-abs(y)for x,y in zip(a,b))}/{sum(a)}',
            'literal_even_pattern_counts':{str(k):v for k,v in Counter(sum(sum(x)for x in p)for p in patterns).items()},
            'exact_raw_colored_coefficients':{str(k):str(v) for k,v in coefficients.items()},
            'normalized_coefficient_common_denominator':str(denominator),
            'independent_block_and_full_pair_transfer_match':True,
            'independent_direct_Kirchhoff_Fourier_C6_match':True,
            'direct_C6_flow_terms':15*64**3,
            'C6_negative_exact':True}
    (HERE/'global_colored_ant_exact_obstruction_checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items()if k not in ('normalized_coefficient_common_denominator','exact_raw_colored_coefficients')},indent=2))
    print('C6 numerator:',expected)

if __name__=='__main__':main()
