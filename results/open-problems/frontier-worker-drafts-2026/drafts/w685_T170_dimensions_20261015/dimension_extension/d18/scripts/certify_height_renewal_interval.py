"""Outward-rounded K21 encoded renewal contraction; no FPP interpretation."""
from pathlib import Path
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from fractions import Fraction as Q
from math import factorial
from functools import lru_cache
from collections import Counter
from datetime import datetime,timezone
import json,hashlib,ctypes,sys,time
from height_profiles import profiles
from certify_scalar_bridge_mass import walk_count
from measure_chord5 import available_memory

ROOT=Path(__file__).resolve().parents[1]
def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))
def sha(name):return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()

def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    free=available_memory()
    if free is not None and free<2*1024**3:raise SystemExit('WAIT: under 2GB free.')
    import numpy as np
    start=time.monotonic()
    K=21;d=int(load('logs/height_bridge_tail_certificate.json')['d'])
    graph=load('scripts/height_renewal_graph.json');point=load('logs/height_bridge_tail_certificate.json')
    scalar=load('logs/scalar_bridge_mass_certificate.json');norm=load('logs/height_renewal_norm_certificate.json')
    point_sha=sha('logs/height_bridge_tail_certificate.json')
    assert scalar['point_sha256']==norm['point_sha256']==point_sha
    assert norm['graph_sha256']==sha('scripts/height_renewal_graph.json')
    get=lambda obj,key:Q(int(obj[key]['n']),int(obj[key]['d']))
    a=get(point,'s')+1;z=get(point,'z')
    assert a==get(scalar,'a') and z==get(scalar,'z')
    states=graph['states'];n=len(states)
    words=profiles(K);suffixes={word[k:] for word,h in words for k in range(1,len(word)+1)}
    estimate=len(suffixes)*n*8+256000000
    assert estimate<1000000000,'Reduce cache before allocating.'
    # Verify the whole length/height polynomial, rather than one numerical value.
    counted=Counter((len(word),h) for word,h in words);bc={}
    for length in range(1,K+1):
        for h in range(1,length+1):
            value=walk_count(length,h)
            value-=sum(bc.get((j,k),0)*walk_count(length-j,h-k)
                       for j in range(1,length) for k in range(1,j+1) if h-k>=1)
            assert value>=0 and value==counted[(length,h)]
            bc[(length,h)]=value
    short=sum((Q(d,1)/a)**length*z**h*count for (length,h),count in counted.items())
    tail=get(scalar,'total_upper')-short
    assert tail>0

    @lru_cache(None)
    def block(c0,c1,E,O,I,p,q):
        x,y=a+c0+I+E,a+c1+E+O
        value=Q(0)
        for even in ((-1,0,1) if E else (-1,)):
            for odd in ((-1,1,2) if O else (-1,)):
                if int(odd==2)!=q:continue
                e0=p+int(even==0);e1=int(even==1)+int(odd==1)
                value+=Q(factorial(e0)*factorial(e1),1)/(x**(e0+1)*y**(e1+1))
        return a*a**(p-q)*value

    def ceil_float(exact):
        value=float(exact)
        if Q.from_float(value)<exact:value=float(np.nextafter(value,np.inf))
        assert Q.from_float(value)>=exact
        return value

    operators={};max_row=0;coefficients=0
    for mark in (0,1):
        for signwanted in (-1,1):
            data=[];indices=[];pointer=[0]
            for both in graph['rows']:
                count=0
                for j,sign,r,final,c0,c1,E,O,I,p,q in both[mark]:
                    if sign!=signwanted:continue
                    factor=block(c0,c1,E,O,I,p,q) if final else 1/a
                    exact=(1 if r==0 else d-r)*z**sign*factor
                    assert exact>0
                    data.append(ceil_float(exact));indices.append(j);count+=1
                max_row=max(max_row,count);coefficients+=count;pointer.append(len(data))
            assert min(data)>2.0**-400 and max(data)<2.0**400
            width=max(pointer[i+1]-pointer[i] for i in range(n))
            packed_data=np.zeros((width,n));packed_indices=np.zeros((width,n),dtype=np.int64)
            for i in range(n):
                count=pointer[i+1]-pointer[i]
                packed_data[:count,i]=data[pointer[i]:pointer[i+1]]
                packed_indices[:count,i]=indices[pointer[i]:pointer[i+1]]
            operators[(mark,signwanted)]=(packed_data,packed_indices)
    assert sys.float_info.radix==2 and sys.float_info.mant_dig==53 and sys.float_info.rounds==1
    def dot_upper(matrix,vec):
        positive=vec[vec>0]
        if len(positive):assert positive.min()>2.0**-400 and positive.max()<2.0**400
        data,indices=matrix
        out=np.zeros(n)
        # Explicit operations: no opaque sparse/BLAS sum and no accumulated
        # error estimate. Each primitive is rounded upward independently.
        for coefficient,target in zip(data,indices):
            value=coefficient*vec[target]
            assert np.isfinite(value).all() and (value>=0).all()
            mask=value>0
            if mask.any():assert value[mask].min()>2.0**-900 and value[mask].max()<2.0**900
            value[mask]=np.nextafter(value[mask],np.inf)
            added=out+value;mask=added>0
            out[mask]=np.nextafter(added[mask],np.inf)
        return out

    selected=load('logs/height_renewal_measure_K21.json')
    ids=selected['boundary_ids'];v=np.array(selected['vector'],dtype=np.float64)
    assert ids==[i for i,state in enumerate(states) if state[1][-1][1]==1]
    assert (v>0).all()
    w=[(a/(a+state[6]))**(state[7]+1) for state in states]
    C=max(Q.from_float(float(v[k]))/w[i] for k,i in enumerate(ids))
    full=np.zeros(n);full[ids]=v;cache={():full}
    def suffix_value(word):
        if word not in cache:cache[word]=dot_upper(operators[(0,word[0])],suffix_value(word[1:]))
        return cache[word]
    total=np.zeros(n)
    for word,h in words:
        val=suffix_value(word[1:]);added=total+val;mask=added>0
        total[mask]=np.nextafter(added[mask],np.inf)
    upper_short=dot_upper(operators[(1,1)],total)[ids]
    largest=Q(0)
    for k,i in enumerate(ids):
        ratio=(Q.from_float(float(upper_short[k]))+tail*C*w[i])/Q.from_float(float(v[k]))
        assert ratio<1,(i,float(ratio))
        largest=max(largest,ratio)
    scale=10**18
    ceil_units=(largest.numerator*scale+largest.denominator-1)//largest.denominator
    assert ceil_units<scale
    inputs=['scripts/height_renewal_graph.json','logs/height_bridge_tail_certificate.json',
            'logs/scalar_bridge_mass_certificate.json','logs/height_renewal_norm_certificate.json',
            'logs/height_renewal_measure_K21.json','scripts/height_profiles.py',
            'scripts/certify_height_renewal_interval.py']
    out=dict(at=datetime.now(timezone.utc).isoformat(),d=d,cutoff=K,states=n,boundary_rows=len(ids),
             profiles=len(words),suffixes=len(suffixes),max_row_entries=max_row,coefficients_rounded_up=coefficients,
             rho_upper={'n':str(ceil_units),'d':str(scale)},
             estimated_peak_bytes=estimate,available_physical_bytes=free,cores=1,priority='below normal',
             rounding='Every binary64 vector product and addition followed by nextafter toward +infinity; zero remains zero; all nonzero arithmetic verified normal and finite.',
             numpy_version=np.__version__,
             hashes={name:sha(name) for name in inputs},seconds=time.monotonic()-start,
             scope='outward-rounded contraction of the encoded finite-plus-scalar-tail renewal operator; graph semantics and FPP proof require separate verification')
    dest=ROOT/'logs/height_renewal_interval_certificate.json'
    part=dest.with_suffix('.json.part');part.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');part.replace(dest)
    print('PASS outward renewal contraction',len(ids),'rows; rho <=',str(ceil_units)+'/10^18','seconds',out['seconds'],flush=True)

if __name__=='__main__':main()
