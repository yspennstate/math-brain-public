"""NUMERICAL: coverage of the finite old-residual sample; no volume/proof claim."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,itertools
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import numpy as np
from new_residual import bank
from fast_conic import ns
from map_residual import moments,endpoint,PAIRS,value
from cover_face import ROOT,split_box

def main():
    d=np.load('residual_samples.npz');u,w,r,a=d['u'],d['w'],d['r'],d['a'];m=moments(u,w);E,edges=endpoint(u,w,r)
    pa=np.full(len(r),-np.inf);pe=pa.copy()
    for name,i,c,module in bank():
        vec=list(map(float,module.vector_from_record(c)))
        if len(vec)==25:vec +=[0.]*5
        valid=(r>=float(F(c['rlo'])))&(r<=float(F(c['rhi'])))
        pa=np.maximum(pa,np.where(valid,ns['lower_value'](m[:3],a,r,vec),-np.inf));pe=np.maximum(pe,np.where(valid,ns['lower_value'](m[:3],E,r,vec),-np.inf))
    eta=2+2*r/(r*r+4*r+1)
    rb=[eta*(3*m[0]-1.5)-m[2],r*r*(eta*(3*m[1]-1.5)-m[2])]
    for v in rb:
        pa=np.maximum(pa,ns['cells'].base_value(m[:3],a,r)+a*a*v);pe=np.maximum(pe,ns['cells'].base_value(m[:3],E,r)+E*E*v)
    nodes=json.load(open('global_cover.json'))['nodes'];thresholds={};stack=[(0,[tuple(map(F,p))for p in ROOT])]
    while stack:
        i,b=stack.pop();n=nodes[i]
        if n['kind']=='split':
            axis=n['axis'];thresholds[i]=float(sum(b[axis])/2);left,right=split_box(b,axis);stack.extend([(n['children'][0],left),(n['children'][1],right)])
    root=np.array([[float(F(v))for v in p]for p in ROOT]);local=np.array([[[float(F(v))for v in p]for p in c['box']]for c in json.load(open('new_face_boxes.json'))])
    def positive(x):
        if np.any(x<root[:,0])or np.any(x>root[:,1]):return False
        i=0
        while nodes[i]['kind']=='split':
            n=nodes[i];i=n['children'][int(x[n['axis']]>thresholds[i])]
        return nodes[i]['kind']=='positive'
    counts=Counter();remaining=[]
    for k in range(len(r)):
        if max(pa[k],pe[k])>=0:counts['moment']+=1;continue
        ee=PAIRS[int(edges[k])];lam=(2+E[k]*(1+r[k]))/4;gap=E[k]*(np.outer(u[k],u[k])+r[k]*np.outer(w[k],w[k]));covered=None
        for ii,jj in(ee,ee[::-1]):
            first=5*gap[ii]/lam;second=5*E[k]*np.sqrt(r[k])/lam*(u[k,ii]*w[k]-w[k,ii]*u[k])
            for rest in itertools.permutations([i for i in range(5)if i not in ee]):
                for sign in(-1,1):
                    x=np.array([first[ii],first[rest[0]],sign*second[rest[0]],first[rest[1]],sign*second[rest[1]],sign*second[jj]])
                    if np.any(np.all((x>=local[:,:,0])&(x<=local[:,:,1]),axis=1)):covered='new_local_box';break
                    if positive(x):covered='positive_partition';break
                if covered:break
            if covered:break
        if covered:counts[covered]+=1
        else:
            counts['uncovered_in_finite_audit']+=1;remaining.append(dict(index=k,r=float(r[k]),a=float(a[k]),a_over_E=float(a[k]/E[k]),T=float(value(m[:,k],a[k],r[k]))))
    out=dict(label='NUMERICAL',old_residual_points=len(r),coverage_counts=dict(counts),least_uncovered=sorted(remaining,key=lambda p:p['T'])[:20],note='Finite floating coverage audit; not a proof of point membership, graph volume, or continuous coverage. Raw random sample excludes the separate local-search points.')
    assert sum(counts.values())==len(r);Path('new_coverage_map.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
    with open('LOG.md','a')as f:f.write('\nNUMERICAL: finite after-map coverage counts '+str(dict(counts))+' out of '+str(len(r))+'. No measure or continuous sign conclusion is drawn.\n')
if __name__=='__main__':main()
