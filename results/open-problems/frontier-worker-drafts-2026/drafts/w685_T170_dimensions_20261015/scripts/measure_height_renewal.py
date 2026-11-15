"""Numerical renewal screen; exact closure, scalar mass and row checks pending."""
from pathlib import Path
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import json,time,ctypes,sys
from datetime import datetime,timezone
from fractions import Fraction as Q
from height_profiles import profiles,scalar_total_float,scalar_short_float
from measure_chord5 import available_memory
ROOT=Path(__file__).resolve().parents[1]

def matrices(graph,d,a,z):
    import numpy as np
    from scipy.sparse import csr_matrix
    n=len(graph['states']);out={}
    for mark in (0,1):
        for signwanted in (-1,1):
            data=[];indices=[];pointer=[0]
            for both in graph['rows']:
                for j,sign,r,final,c0,c1,e,o,previous,p,q in both[mark]:
                    if sign!=signwanted:continue
                    if not final:factor=1/a
                    else:
                        x=a+c0+previous+e;y=a+c1+e+o
                        if p==0:left0=1/x+e/x**2;left1=e/x
                        else:left0=1/x**2+2*e/x**3;left1=e/x**2
                        if q==0:value=left0*(1/y+o/y**2)+left1*(1/y**2+2*o/y**3)
                        else:value=left0*o/y+left1*o/y**2
                        factor=a*a**(p-q)*value
                    multiplicity=1 if r==0 else d-r
                    assert multiplicity>=0
                    data.append(multiplicity*z**sign*factor);indices.append(j)
                pointer.append(len(data))
            out[(mark,signwanted)]=csr_matrix((data,indices,pointer),shape=(n,n))
    return out
def main():
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(),0x4000)
    free=available_memory()
    if free is not None and free<2*1024**3:print('WAIT: less than2GB free.',flush=True);return
    import numpy as np
    cutoff=int(sys.argv[1]) if len(sys.argv)>1 else 13
    graph=json.loads((ROOT/'scripts/height_renewal_graph.json').read_text(encoding='utf-8'))
    point=json.loads((ROOT/'logs/height_bridge_tail_certificate.json').read_text(encoding='utf-8'))
    rational=lambda name:Q(int(point[name]['n']),int(point[name]['d']))
    d=21;s=float(rational('s'));z=float(rational('z'));a=s+1
    words=profiles(cutoff);suffixes={word[k:] for word,h in words for k in range(1,len(word)+1)}
    estimate=len(suffixes)*len(graph['states'])*8+256000000
    resource=dict(at=datetime.now(timezone.utc).isoformat(),available_physical_bytes=free,estimated_peak_bytes=estimate,cores=1,priority='below normal',cutoff=cutoff,profiles=len(words),suffixes=len(suffixes))
    (ROOT/f'logs/height_renewal_measure_resource_K{cutoff}.json').write_text(json.dumps(resource,indent=2)+'\n',encoding='utf-8')
    assert estimate<1000000000,'Reduce profile cutoff before allocating this cache.'
    ops=matrices(graph,d,a,z);n=len(graph['states'])
    w=np.array([(a/(a+state[6]))**(state[7]+1) for state in graph['states']])
    boundary=np.array([state[1][-1][1]==1 for state in graph['states']]);ids=np.where(boundary)[0]
    btotal=scalar_total_float(d,a,z);bshort=scalar_short_float(words,d,a,z);tail=btotal-bshort;assert tail>0
    print('K',cutoff,'states',n,'boundary',len(ids),'profiles',len(words),'suffixes',len(suffixes),'scalar_total',btotal,'scalar_tail',tail,flush=True)
    def apply(v):
        full=np.zeros(n);full[ids]=v;cache={():full}
        def value(suffix):
            if suffix not in cache:cache[suffix]=ops[(0,suffix[0])]@value(suffix[1:])
            return cache[suffix]
        total=np.zeros(n)
        for word,height in words:total+=value(word[1:])
        result=(ops[(1,1)]@total)[ids]
        result+=tail*float(np.max(v/w[ids]))*w[ids]
        return result
    v=w[ids].copy();start=time.monotonic();dest=ROOT/f'logs/height_renewal_measure_K{cutoff}.json'
    initial=dest
    if not initial.exists() and len(sys.argv)>2:
        initial=ROOT/f'logs/height_renewal_measure_K{int(sys.argv[2])}.json'
    if initial.exists():
        saved=json.loads(initial.read_text(encoding='utf-8'));v=np.array(saved['vector'])
    for iteration in range(100):
        new=(v+apply(v))*.5;new/=np.max(new/w[ids]);diff=float(np.max(np.abs(new-v)));v=new
        if iteration%10==0:print('iteration',iteration,'diff',diff,'seconds',time.monotonic()-start,flush=True)
        if diff<2e-12 or time.monotonic()-start>110:break
    value=apply(v);ratios=value/v
    obj=dict(at=datetime.now(timezone.utc).isoformat(),d=d,s=s,z=z,cutoff=cutoff,states=n,boundary_ids=ids.tolist(),profiles=len(words),suffixes=len(suffixes),scalar_total=btotal,scalar_short=bshort,scalar_tail=tail,rho_upper_float=float(ratios.max()),rho_lower_float=float(ratios.min()),vector=v.tolist(),iterations_this_run=iteration+1,seconds=time.monotonic()-start,status='numerical evidence only; independent graph semantics and interval renewal row certificate pending')
    dest.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');print('RESULT',cutoff,'rho',obj['rho_lower_float'],obj['rho_upper_float'],'seconds',obj['seconds'],flush=True)
if __name__=='__main__':main()
