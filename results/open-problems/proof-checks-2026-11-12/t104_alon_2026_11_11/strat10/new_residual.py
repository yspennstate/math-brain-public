"""PROVED finite residual witnesses and precise new residual predicates.
OPEN: sign throughout that residual is not inferred from finite witnesses.
"""
import itertools,json
from pathlib import Path
from fractions import Fraction as F
import cells,cubic_cells
from rational_rays import frame_data
from residual_witness import verify as verify_old
from certify_samples import integer_frame
from precise_charts import source_chart
from cover_face import ROOT,split_box
BANKS=['moment_cells.json','allN_optimized_cells.json','fine_cells.json','cubic_cells.json','stacked_cells.json','cubic_allN_cells.json']

def bank():
    return [(name,i,rec,cubic_cells if 'cubic_multipliers'in rec else cells)for name in BANKS for i,rec in enumerate(json.load(open(name)))]

def point_bounds(source,fraction):
    r=F(source['r']);data=frame_data(source['U'],source['W'],r);a=data['a']*fraction
    vals=[];ceil=F(14,25)
    for name,i,rec,module in bank():
        if F(rec['rlo'])<=r<=F(rec['rhi']):
            v=module.vector_from_record(rec);vals.append([name,i,str(module.lower_value(data['moments'],a,r,v)),str(module.lower_value(data['moments'],data['a'],r,v))]);ceil=max(ceil,F(rec['ahi']))
    from analytic_moments import lower_value as analytic_lower
    for j in range(2):vals.append(['analytic_moments',j,str(analytic_lower(data['moments'],a,r,j)),str(analytic_lower(data['moments'],data['a'],r,j))])
    return data,a,ceil,vals

def reachable(coords,nodes):
    ids=[];stack=[(0,[tuple(map(F,p))for p in ROOT])]
    # If chart outside canonical root, it cannot lie in its positive leaves.
    if any(c.hi<lo or hi<c.lo for c,(lo,hi)in zip(coords,stack[0][1])):return []
    while stack:
        i,box=stack.pop()
        if any(c.hi<lo or hi<c.lo for c,(lo,hi)in zip(coords,box)):continue
        n=nodes[i]
        if n['kind']=='split':
            left,right=split_box(box,n['axis']);stack.extend([(n['children'][0],left),(n['children'][1],right)])
        else:ids.append(i)
    return sorted(ids)

def verify(source,fraction=F(1)):
    old=verify_old(source);data,a,ceil,vals=point_bounds(source,fraction)
    assert 0<fraction<=1 and a>ceil and max(F(v[2])for v in vals)<0 and max(F(v[3])for v in vals)<0
    nodes=json.load(open('global_cover.json'))['nodes']
    local_boxes=json.load(open('new_face_boxes.json'))+json.load(open('baseline_positive_partition_boxes.json'))['boxes']
    boxes=[[(F(a),F(b))for a,b in rec['box']]for rec in local_boxes]
    charts=[];pairs=list(itertools.combinations(range(5),2))
    for edge,w in zip(pairs,data['weights']):
        if w:continue
        for ordered in(edge,edge[::-1]):
            for rest in itertools.permutations([i for i in range(5)if i not in edge]):
                cc,perm,d=source_chart(source,rest+ordered)
                for sign in(-1,1):
                    coords=[-v if sign<0 and i in(2,4,5)else v for i,v in enumerate(cc)]
                    assert all(any(v.hi<lo or hi<v.lo for v,(lo,hi)in zip(coords,box))for box in boxes)
                    ids=reachable(coords,nodes);assert all(nodes[i]['kind']!='positive'for i in ids)
                    charts.append(dict(permutation=list(rest+ordered),sign=sign,reachable_leaves=ids))
    # The pressure family has r=1; avoid it exactly for the retained witness.
    assert F(source['r'])<1
    return dict(old=old,actual_a=str(a),ceiling=str(ceil),lower_bound_values=vals,charts=charts)

def discover():
    # Exact, concise perturbations of the two-edge limit are tested first.
    for k in (1000,10000,100000,1000000,10000000):
        U=[-4*k,k+1,k+1,k-1,k-1];W=[0,1,-1,-1,1]
        V=[x+k*y for x,y in zip(U,W)];norm=sum(x*x for x in V);dot=sum(x*y for x,y in zip(V,W));WW=[norm*y-dot*x for x,y in zip(V,W)]
        source=dict(U=V,W=WW,r=str(F(k-1,k)))
        try:proof=verify(source)
        except AssertionError:continue
        out=dict(label='PROVED finite membership and positive sign; OPEN neighborhood',source=source,verification=proof)
        Path('new_residual_witness.json').write_text(json.dumps(out,indent=2)+'\n')
        print('PROVED: concise exact final-residual witness',source,'T6',proof['old']['T6'],flush=True)
        with open('LOG.md','a')as f:f.write('\nPROVED (new_residual_witness.json; verify_new_residual.py): exact connected endpoint at r<1 misses all new moment tests and all positive face boxes in every chart. The final residual is nonempty; the finite witness has positive T6='+proof['old']['T6']+'.\n')
        return
    import numpy as np
    from map_residual import moments,endpoint,PAIRS
    from fast_conic import ns
    data=np.load('residual_samples.npz');records=bank();nodes=json.load(open('global_cover.json'))['nodes']
    bb=np.array([[[float(F(v))for v in pair]for pair in c['box']]for c in json.load(open('new_face_boxes.json'))])
    candidates=np.argsort(-data['a'])
    for idx in candidates:
        u,w,r=data['u'][idx],data['w'][idx],float(data['r'][idx]);E,edge=endpoint(u,w,r);m=moments(u,w)
        vv=[]
        for name,i,c,module in records:
            if float(F(c['rlo']))<=r<=float(F(c['rhi'])):
                vector=list(map(float,module.vector_from_record(c)))
                if len(vector)==25:vector +=[0.]*5
                vv.append(ns['lower_value'](m[:3],E,r,vector))
        if max(vv)>=-1e-8:continue
        # Cheap chart-center screen before exact rationalization.
        lam=(2+E*(1+r))/4;gap=E*(np.outer(u,u)+r*np.outer(w,w));ee=PAIRS[int(edge)];good=True
        for k,j in(ee,ee[::-1]):
            first=5*gap[k]/lam;second=5*E*np.sqrt(r)/lam*(u[k]*w-w[k]*u)
            for rest in itertools.permutations([i for i in range(5)if i not in ee]):
                for sign in(-1,1):
                    x=np.array([first[k],first[rest[0]],sign*second[rest[0]],first[rest[1]],sign*second[rest[1]],sign*second[j]])
                    if np.any(np.all((x>=bb[:,:,0])&(x<=bb[:,:,1]),axis=1)):good=False;break
                    ids=reachable([__import__('face_intervals').Interval(F(v))for v in x],nodes)
                    if any(nodes[i]['kind']=='positive'for i in ids):good=False;break
                if not good:break
            if not good:break
        if not good:continue
        U,W=integer_frame(u,w);source=dict(U=U,W=W,r=str(F(r).limit_denominator(10**7)))
        try:proof=verify(source)
        except AssertionError:continue
        out=dict(label='PROVED finite membership and positive sign; OPEN neighborhood',source=source,verification=proof)
        Path('new_residual_witness.json').write_text(json.dumps(out,indent=2)+'\n')
        print('PROVED: exact witness in new residual, r',source['r'],'a',proof['actual_a'],'T6',proof['old']['T6'],flush=True)
        with open('LOG.md','a')as f:f.write('\nPROVED (new_residual_witness.json; verify_new_residual.py): an exact connected endpoint misses every new pointwise moment test and every old/new/local/global positive face box in all charts. The new residual is nonempty; its displayed T6 is positive. The pressure-family theorem does not apply because r<1.\n')
        return
    raise RuntimeError('OPEN: no exact new-residual witness found in this finite bank')
if __name__=='__main__':discover()
