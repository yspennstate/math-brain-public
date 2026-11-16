"""Independent small-graph checks for samplers, spectra and component calculation."""
import json, math
from pathlib import Path
from simulate import (bernoulli_indices,upper_pairs,largest,tree_core_edges,
                      tree_core_radius,star_clique_radius,Host,planted_host)
import numpy as np

def union_largest(n,u,v):
    parent=list(range(n));sz=[1]*n
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for a,b in zip(u,v):
        a,b=root(int(a)),root(int(b))
        if a!=b:
            if sz[a]<sz[b]:a,b=b,a
            parent[b]=a;sz[a]+=sz[b]
    return max(sz)


def matrix(n,u,v):
    a=np.zeros((n,n));a[u,v]=1;a[v,u]=1;return a


def main():
    rng=np.random.default_rng(351028)
    for n in range(2,60):
        u,v=upper_pairs(n,np.arange(n*(n-1)//2))
        uu,vv=np.triu_indices(n,1)
        assert np.array_equal(u,uu) and np.array_equal(v,vv)
    for N,p in [(17,.3),(1000,.001),(12,.9),(20,0),(20,1)]:
        hist=np.zeros(N);counts=[];trials=6000
        for _ in range(trials):
            x=bernoulli_indices(N,p,rng)
            assert len(x)==len(np.unique(x)) and np.all((x>=0)&(x<N))
            hist[x]+=1;counts.append(len(x))
        if 0<p<1:
            z=(np.mean(counts)-N*p)/math.sqrt(N*p*(1-p)/trials)
            assert abs(z)<5
            assert np.max(abs(hist-trials*p))<6*math.sqrt(trials*p*(1-p))
    residuals={}
    n,u,v=tree_core_edges(12,16,2)
    a=matrix(n,u,v)
    exact=float(np.linalg.eigvalsh(a)[-1]);quot=tree_core_radius(12,16,2)
    assert abs(exact-quot)<1e-10
    residuals['tree_full_vs_quotient']=abs(exact-quot)
    full=np.kron(a,np.ones((2,2)))
    assert abs(np.linalg.eigvalsh(full)[-1]-2*quot)<1e-10
    residuals['blowup_full_vs_product']=abs(float(np.linalg.eigvalsh(full)[-1])-2*quot)
    m,t=7,11;n=m+t;u,v=np.triu_indices(m,1)
    u=np.r_[u,np.zeros(t,dtype=int)];v=np.r_[v,np.arange(m,n)]
    exact=float(np.linalg.eigvalsh(matrix(n,u,v))[-1])
    assert abs(exact-star_clique_radius(m,t))<1e-10
    residuals['star_clique_full_vs_quotient']=abs(exact-star_clique_radius(m,t))
    cases=[Host('bipartite',19,12,math.sqrt(7*12),84,{'s':7,'t':12},'bipartite'),
           Host('star_clique',18,17,star_clique_radius(7,11),32,{'m':7,'t':11},'star_clique'),
           planted_host(200,42)]
    nb,u,v=tree_core_edges(12,16,1)
    cases.append(Host('blowup',nb*2,34,2*tree_core_radius(12,16,1),len(u)*4,
                      {'multiplicity':2},'blowup',u,v))
    for host in cases:
        allu,allv=host.sample(1,rng)
        assert len(allu)==host.potential_edges
        keys=np.minimum(allu,allv)*host.n+np.maximum(allu,allv)
        assert len(np.unique(keys))==len(keys) and np.all(allu!=allv)
        assert np.bincount(np.r_[allu,allv],minlength=host.n).max()==host.delta
        for _ in range(30):
            u,v=host.sample(.2,rng)
            assert largest(host.n,u,v)==union_largest(host.n,u,v)
    # Exact moment recurrence, checked against the closed form used in the proof.
    b=108;a0=1-math.exp(-.98/101);mu=b*a0;var=b*a0*(1-a0)
    mean=second=1.
    for h in range(1,60):
        second=mu*mu*second+var*mean;mean*=mu
        formula=1+var/(mu*(mu-1))*(1-mu**(-h))
        assert abs(second/mean**2-formula)<1e-11
    result={'status':'PASS','triangle_decoders':58,'sampler_trials':30000,
            'independent_component_comparisons':120,'spectral_differences':residuals,
            'moment_recurrence_generations':59,'explicit_blowup_mean_floor':mu,
            'explicit_exponent':math.log(mu)/math.log(b)}
    Path('data/verification.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
