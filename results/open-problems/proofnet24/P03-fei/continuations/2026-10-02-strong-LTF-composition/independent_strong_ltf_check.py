"""Exact identity / finite inequality checks for strong FEI and composition."""
from fractions import Fraction as F
from math import log2
from pathlib import Path
import json
from independent_hamming_band_check import monotone_masks


def walsh(v):
    out=list(v);step=1
    while step<len(out):
        for left in range(0,len(out),2*step):
            for i in range(left,left+step):
                a,b=out[i],out[i+step]
                out[i],out[i+step]=a+b,a-b
        step*=2
    return out


def spectral_entropy(v):
    N=len(v)
    return sum(F(a*a,N*N)*log2(F(N*N,a*a))for a in walsh(v)if a)


def physical(v):
    n=(len(v)-1).bit_length();N=len(v)
    return [F(sum(v[x]!=v[x^(1<<i)]for x in range(N)),N)for i in range(n)]


def variance(v):
    return 1-F(sum(v),len(v))**2


report={'status':'PASS','scope':'finite sanity checks; analytic proof remains essential',
        'variance_recursions':0,'near_dictator_unate_checks':0,
        'max_near_dictator_increment_over_delta':0.,'balanced_compositions':[]}

for n in range(1,6):
    N=1<<n
    masks=monotone_masks(n)
    if n==5:masks=masks[::17]
    for mask in masks:
        f=[1 if(mask>>x)&1 else -1 for x in range(N)]
        inf=physical(f);V=variance(f);H=spectral_entropy(f)
        for i in range(n):
            branches=[]
            for sign in(0,1):
                branches.append([f[(x&((1<<i)-1))|((x>>i)<<(i+1))|(sign<<i)]
                                 for x in range(N//2)])
            m,p=branches;alpha=inf[i]
            assert V-(variance(p)+variance(m))/2==alpha**2
            assert sum(inf)-(sum(physical(p))+sum(physical(m)))/2==alpha
            D=sum(inf)-V
            assert D-((sum(physical(p))-variance(p))+(sum(physical(m))-variance(m)))/2==alpha*(1-alpha)
            report['variance_recursions']+=1
            if alpha>F(1,2):
                delta=1-alpha
                inc=H-(spectral_entropy(p)+spectral_entropy(m))/2
                if not delta:
                    assert abs(inc)<1e-12
                else:
                    assert inc<=8*float(delta)+1e-11
                    report['max_near_dictator_increment_over_delta']=max(
                        report['max_near_dictator_increment_over_delta'],inc/float(delta))
                report['near_dictator_unate_checks']+=1


def ltf(weights,threshold):
    return [1 if sum(w*(2*((x>>i)&1)-1)for i,w in enumerate(weights))>threshold else -1
            for x in range(1<<len(weights))]


for sizes,outerweights,threshold in [([3,3,3],[1,1,1],0),([3,3,3],[1,1,1],2),
                                    ([3,3,3,3],[1,1,1,1],2),([3,5,3],[1,2,3],1),
                                    ([3,3,3],[-1,2,3],-2)]:
    children=[ltf([1]*n,0)for n in sizes]
    assert all(sum(g)==0 for g in children)
    outer=ltf(outerweights,threshold)
    n=sum(sizes)
    composed=[]
    for x in range(1<<n):
        offset=0;outerindex=0
        for i,(size,child)in enumerate(zip(sizes,children)):
            val=child[(x>>offset)&((1<<size)-1)]
            outerindex|=(val==1)<<i;offset+=size
        composed.append(outer[outerindex])
    childI=[sum(physical(g))for g in children];outerIi=physical(outer)
    expectedI=sum(u*v for u,v in zip(outerIi,childI))
    expectedH=spectral_entropy(outer)+sum(float(ii)*spectral_entropy(g)for ii,g in zip(outerIi,children))
    assert sum(physical(composed))==expectedI
    assert variance(composed)==variance(outer)
    assert abs(spectral_entropy(composed)-expectedH)<1e-10
    report['balanced_compositions'].append({'child_dimensions':sizes,'outer_weights':outerweights,
        'threshold':threshold,'dimension':n,'influence_exact':str(expectedI),
        'variance_exact':str(variance(composed)),'entropy_identity_error':spectral_entropy(composed)-expectedH})

out=Path(__file__).with_name('independent_strong_ltf_checks.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
