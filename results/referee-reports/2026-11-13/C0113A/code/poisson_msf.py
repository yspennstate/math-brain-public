"""Bounded Poisson MSF diagnostics, with exact finite-metric MST certificates.

Run from the project root: python3 code/poisson_msf.py --replicates 16
Only one numerical thread is used. This measures finite forests, not infinite
connectivity. Nested samples and all random seeds are recorded.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS','BLIS_NUM_THREADS'):
    os.environ[name]='1'
import argparse, csv, hashlib, json, math, resource, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import cKDTree
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components, breadth_first_order
from scipy.stats import t as student_t

ROOT=Path(__file__).resolve().parents[1]
# Inherit nice 10 from the task launcher; only increase niceness if necessary.
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.setpriority(os.PRIO_PROCESS,0,10)
# macOS may reject this limit; expose that fact instead of treating it as active.
try:
    resource.setrlimit(resource.RLIMIT_DATA,(3_200_000_000,3_200_000_000))
    DATA_LIMIT_STATUS={'active':resource.getrlimit(resource.RLIMIT_DATA)[0]<=3_200_000_000}
except (ValueError,OSError) as error:
    DATA_LIMIT_STATUS={'active':False,'error':str(error)}
MAX_PAIRS=4_000_000 # arrays stay far below 4 GB even in the guarded worst case


def metrics(points, pairs, side, periodic):
    delta=np.abs(points[pairs[:,0]]-points[pairs[:,1]])
    if periodic: delta=np.minimum(delta, side-delta)
    return np.sqrt(np.einsum('ij,ij->i',delta,delta))


def sparse_graph(n,pairs,weights):
    return coo_matrix((np.r_[weights,weights],
        (np.r_[pairs[:,0],pairs[:,1]],np.r_[pairs[:,1],pairs[:,0]])),shape=(n,n)).tocsr()


def exact_mst(points,side,periodic):
    """Connected radius graph MST is the complete-metric MST: omitted edges
    are >=radius, while every tree edge is strictly smaller than radius.
    """
    n,d=points.shape
    volume=math.pi**(d/2)/math.gamma(d/2+1)
    radius=(24/volume)**(1/d)
    coords=points+side/2
    tree=cKDTree(coords,boxsize=side if periodic else None)
    for attempt in range(12):
        pairs=tree.query_pairs(radius,output_type='ndarray')
        if len(pairs)>MAX_PAIRS: raise MemoryError('candidate edge cap exceeded')
        weights=metrics(points,pairs,side,periodic)
        graph=sparse_graph(n,pairs,weights)
        mst=minimum_spanning_tree(graph).tocoo()
        if mst.nnz==n-1:
            assert float(mst.data.max())<radius*(1-1e-12)
            selected=np.sort(np.c_[mst.row,mst.col],axis=1)
            return selected,mst.data,pairs,weights,{
                'radius':radius,'candidate_edges':len(pairs),
                'max_mst_edge':float(mst.data.max()),'radius_attempts':attempt+1}
        radius*=1.3
    raise RuntimeError('radius graph failed to connect')


def exterior_wire(points,side,pairs,weights):
    n=len(points)
    delta=side/2-np.abs(points).max(axis=1)
    assert np.all(delta>0)
    edges=np.vstack((pairs,np.c_[np.arange(n),np.full(n,n)]))
    graph=sparse_graph(n+1,edges,np.r_[weights,delta])
    mst=minimum_spanning_tree(graph).tocoo()
    assert mst.nnz==n
    internal=(mst.row<n)&(mst.col<n)
    return np.sort(np.c_[mst.row[internal],mst.col[internal]],axis=1)


def labels_in_window(n,edges,mask):
    keep=mask[edges[:,0]]&mask[edges[:,1]]
    small=edges[keep]
    if len(small):
        graph=coo_matrix((np.ones(2*len(small)),
           (np.r_[small[:,0],small[:,1]],np.r_[small[:,1],small[:,0]])),shape=(n,n)).tocsr()
        _,labels=connected_components(graph,directed=False)
    else: labels=np.arange(n)
    return labels,len(np.unique(labels[mask])),small


def far_pairs(points,mask,side,rng,number=64):
    indices=np.flatnonzero(mask)
    candidates=set()
    if len(indices)<2: return np.empty((0,2),dtype=int)
    for _ in range(number*300):
        i,j=sorted(rng.choice(indices,2,replace=False).tolist())
        if np.linalg.norm(points[i]-points[j])>=side/3:
            candidates.add((i,j))
            if len(candidates)==number: break
    return np.array(sorted(candidates),dtype=int).reshape(-1,2)


def dense_prim(points,side,periodic,wire=False):
    """Independent O(n^2) Prim implementation, only for small validation."""
    delta=np.abs(points[:,None,:]-points[None,:,:])
    if periodic: delta=np.minimum(delta,side-delta)
    weights=np.sqrt((delta**2).sum(axis=2))
    n=len(points)
    if wire:
        allw=np.zeros((n+1,n+1));allw[:n,:n]=weights
        allw[:n,n]=allw[n,:n]=side/2-np.abs(points).max(axis=1)
        weights=allw;n+=1
    np.fill_diagonal(weights,np.inf)
    used=np.zeros(n,dtype=bool);used[0]=True
    best=weights[0].copy();parent=np.zeros(n,dtype=int);result=[]
    for _ in range(n-1):
        j=int(np.argmin(np.where(used,np.inf,best)))
        result.append(tuple(sorted((int(parent[j]),j))));used[j]=True
        improve=(weights[j]<best)&~used
        best[improve]=weights[j,improve];parent[improve]=j
    return set(result)


def validate():
    rng=np.random.default_rng(78113);checks=[]
    for d in (3,4,5):
        side=8.;points=rng.uniform(-side/2,side/2,(120,d))
        for periodic in (False,True):
            selected,_,pairs,weights,meta=exact_mst(points,side,periodic)
            assert set(map(tuple,selected))==dense_prim(points,side,periodic)
            checks.append(f'd={d}, periodic={periodic}: sparse Kruskal equals full-metric Prim')
            if not periodic:
                wired=exterior_wire(points,side,pairs,weights)
                expected={e for e in dense_prim(points,side,False,wire=True) if max(e)<len(points)}
                assert set(map(tuple,wired))==expected
                # Check the actual strict sublevel component certificate for every wire edge.
                delta=side/2-np.abs(points).max(axis=1)
                for i,j in wired:
                    s=np.linalg.norm(points[i]-points[j])
                    short=pairs[weights<s*(1-1e-12)]
                    _,labels=connected_components(sparse_graph(len(points),short,np.ones(len(short))))
                    assert labels[i]!=labels[j]
                    assert any(np.min(delta[labels==labels[v]])>=s-1e-10 for v in (i,j))
                checks.append(f'd={d}: exterior wire equals full Prim and every retained edge has a strict cut certificate')
    return checks


def path_extent(points,edges,source,target):
    graph=sparse_graph(len(points),edges,np.ones(len(edges)))
    _,parents=breadth_first_order(graph,source,directed=False,return_predecessors=True)
    path=[target]
    while path[-1]!=source:
        path.append(int(parents[path[-1]]))
        assert path[-1]>=0
    return float(np.max(np.abs(points[path]))),len(path)


def summarize(rows):
    groups={}
    for row in rows:
        key=(row['d'],row['expected_n'],row['boundary'])
        groups.setdefault(key,[]).append(row)
    result=[]
    for (d,expected,bc),group in sorted(groups.items()):
        values=np.array([r['far_core_fraction'] for r in group if r['far_pair_count']])
        count=len(values)
        mean=float(np.mean(values))
        half=float(student_t.ppf(.975,count-1)*np.std(values,ddof=1)/np.sqrt(count)) if count>1 else 1.
        result.append({'d':d,'expected_n':expected,'side':group[0]['side'],
            'boundary':bc,'replicates':len(group),
            'mean_n':float(np.mean([r['n'] for r in group])),
            'mean_far_core_fraction':mean,'replicate_t95_low':max(0.,mean-half),
            'replicate_t95_high':min(1.,mean+half),
            'fixed_inner_connections':sum(r['fixed_inner_connected'] for r in group),
            'wired_fixed_inner_connections':sum(r['wired_fixed_inner_connected'] for r in group),
            'wired_far_core_fraction':float(np.mean([r['wired_far_core_fraction'] for r in group])),
            'mean_core_components':float(np.mean([r['core_components'] for r in group])),
            'wired_whole_box_far_fraction':float(np.mean([r['wired_whole_box_far_fraction'] for r in group])),
            'wired_whole_box_fixed_connections':sum(r['wired_whole_box_fixed_connected'] for r in group),
            'mean_fixed_path_radius':float(np.mean([r['fixed_path_radius'] for r in group]))})
    return result


def run(replicates,counts,seed):
    start=time.monotonic();checks=validate()
    rows=[];out=ROOT/'data'/'observations.jsonl'
    pair_stream=(ROOT/'data'/'pair_observations.csv').open('w',newline='')
    pair_writer=csv.writer(pair_stream)
    pair_writer.writerow(['d','replicate','expected_n','boundary','i','j','distance','core_connected','wired_core_connected','wired_whole_box_connected'])
    with out.open('w') as stream:
      for d in (3,4,5):
        sides=np.array(counts,dtype=float)**(1/d)
        for rep in range(replicates):
          sample_seed=seed+d*100_000+rep
          rng=np.random.default_rng(sample_seed)
          allpoints=rng.uniform(-sides[-1]/2,sides[-1]/2,(rng.poisson(counts[-1]),d))
          digest=hashlib.sha256(allpoints.tobytes()).hexdigest()
          firstids=np.flatnonzero(np.max(np.abs(allpoints),axis=1)<=sides[0]/4)
          assert len(firstids)>1
          # A single distant pair, fixed across the nested boxes.
          trial=allpoints[firstids]
          delta=trial[:,None,:]-trial[None,:,:]
          ia,ib=np.unravel_index(np.argmax(np.sum(delta**2,axis=2)),(len(trial),len(trial)))
          fixed_ids=(int(firstids[ia]),int(firstids[ib]))
          fixed_distance=float(np.linalg.norm(allpoints[fixed_ids[0]]-allpoints[fixed_ids[1]]))
          prev_lower=False;prev_upper=True;prev_core_free=None
          for expected,side in zip(counts,sides):
            ids=np.flatnonzero(np.max(np.abs(allpoints),axis=1)<side/2)
            points=allpoints[ids];n=len(points)
            fixed_local=tuple(int(np.searchsorted(ids,i)) for i in fixed_ids)
            assert all(ids[i]==g for i,g in zip(fixed_local,fixed_ids))
            core=np.max(np.abs(points),axis=1)<=side/4
            fixed_inner=np.max(np.abs(points),axis=1)<=3*sides[0]/8
            pair_rng=np.random.default_rng(sample_seed+int(expected)*10)
            pairs_to_test=far_pairs(points,core,float(side),pair_rng)
            assert len(pairs_to_test)>0
            for periodic in (False,True):
              step=time.monotonic()
              edges,w,candidates,candidate_weights,meta=exact_mst(points,float(side),periodic)
              corelabels,corecomponents,coreedges=labels_in_window(n,edges,core)
              fixedlabels,_,_=labels_in_window(n,edges,fixed_inner)
              far_fraction=float(np.mean(corelabels[pairs_to_test[:,0]]==corelabels[pairs_to_test[:,1]]))
              fixed_connected=bool(fixedlabels[fixed_local[0]]==fixedlabels[fixed_local[1]])
              path_radius,path_vertices=path_extent(points,edges,*fixed_local)
              if not periodic:
                wired=exterior_wire(points,float(side),candidates,candidate_weights)
                wirelabels,_,_=labels_in_window(n,wired,core)
                wirefixedlabels,_,_=labels_in_window(n,wired,fixed_inner)
                wirealllabels,_,_=labels_in_window(n,wired,np.ones(n,dtype=bool))
                wired_all_far=float(np.mean(wirealllabels[pairs_to_test[:,0]]==wirealllabels[pairs_to_test[:,1]]))
                wired_all_fixed=bool(wirealllabels[fixed_local[0]]==wirealllabels[fixed_local[1]])
                wired_far=float(np.mean(wirelabels[pairs_to_test[:,0]]==wirelabels[pairs_to_test[:,1]]))
                wired_fixed=bool(wirefixedlabels[fixed_local[0]]==wirefixedlabels[fixed_local[1]])
                assert not prev_lower or wired_fixed
                assert not fixed_connected or prev_upper
                assert not wired_fixed or fixed_connected
                prev_lower=wired_fixed;prev_upper=fixed_connected
                free_core_set=set(map(tuple,coreedges))
              else:
                assert set(map(tuple,coreedges))<=free_core_set
                # The common Poisson wired certificate must also appear in the torus MST.
                assert set(map(tuple,wired))<=set(map(tuple,edges))
                assert wired_far<=far_fraction+1e-12
                assert not wired_fixed or fixed_connected
              row={'d':d,'replicate':rep,'sample_seed':sample_seed,'sample_sha256':digest,
                  'expected_n':int(expected),'side':float(side),'n':n,
                  'boundary':'periodic' if periodic else 'free','full_connected':True,
                  'core_n':int(core.sum()),'core_components':corecomponents,
                  'far_pair_count':len(pairs_to_test),'far_core_fraction':far_fraction,
                  'mean_far_pair_distance':float(np.linalg.norm(points[pairs_to_test[:,0]]-points[pairs_to_test[:,1]],axis=1).mean()),
                  'fixed_root_global_indices':fixed_ids,'fixed_root_coordinates':allpoints[list(fixed_ids)].tolist(),
                  'fixed_root_distance':fixed_distance,'fixed_inner_side':float(.75*sides[0]),
                  'fixed_inner_connected':fixed_connected,'wired_fixed_inner_connected':wired_fixed,
                  'wired_far_core_fraction':wired_far,
                  'wired_whole_box_far_fraction':wired_all_far,
                  'wired_whole_box_fixed_connected':wired_all_fixed,
                  'fixed_path_radius':path_radius,'fixed_path_vertex_count':path_vertices,
                  'seconds':time.monotonic()-step,**meta}
              rows.append(row);stream.write(json.dumps(row)+'\n');stream.flush()
              for i,j in pairs_to_test:
                pair_writer.writerow([d,rep,int(expected),row['boundary'],int(i),int(j),
                    float(np.linalg.norm(points[i]-points[j])),int(corelabels[i]==corelabels[j]),
                    int(wirelabels[i]==wirelabels[j]),int(wirealllabels[i]==wirealllabels[j])])
              pair_stream.flush()
          print(json.dumps({'d':d,'replicate_done':rep,'elapsed_seconds':round(time.monotonic()-start,1)}),flush=True)
    pair_stream.close()
    summary=summarize(rows)
    with (ROOT/'data'/'summary.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(summary[0]));writer.writeheader();writer.writerows(summary)
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin': peak*=1024
    metadata={'numpy':np.__version__,'scipy':scipy.__version__,'python':sys.version,
        'replicates':replicates,'expected_counts':counts,'base_seed':seed,
        'nice':os.getpriority(os.PRIO_PROCESS,0),'numerical_threads':1,
        'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':peak,
        'data_segment_limit':DATA_LIMIT_STATUS,
        'validation':checks,'observations':len(rows),
        'note':'Far pairs within a sample are dependent. CIs use independent replicate fractions. Fixed roots and inner windows are held constant within each nested realization. Full MST connectivity is tautological.'}
    assert peak<4_000_000_000
    (ROOT/'data'/'run_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--replicates',type=int,default=16)
    parser.add_argument('--counts',type=int,nargs='+',default=[1024,4096,16384,65536])
    parser.add_argument('--seed',type=int,default=1132026)
    parser.add_argument('--validate-only',action='store_true');args=parser.parse_args()
    if args.validate_only: print(json.dumps(validate(),indent=2))
    else: run(args.replicates,args.counts,args.seed)
