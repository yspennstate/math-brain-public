"""Finite-grid LFPP evidence, not a continuum dimension estimator.

One process, inherited nice >=10, BLAS/FFT worker counts one. No network calls.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 code/lfpp_experiment.py
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import csv
import datetime
import heapq
import json
from pathlib import Path
import resource
import time
import numpy as np
import scipy
from scipy.fft import idstn
from scipy.ndimage import map_coordinates
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'

def eigenvalues(n):
    k = np.arange(1, n+1)
    one = 2 - 2*np.cos(np.pi*k/(n+1))
    return one[:, None] + one[None, :]

def gff(n, rng):
    # L = 4I - nearest-neighbour adjacency, zero exterior Dirichlet values.
    # Cov(h)=2*pi*L^{-1}; diagonal divergence is log N, as in the paper.
    return idstn(rng.normal(size=(n,n)) / np.sqrt(eigenvalues(n)),
                 type=1, norm='ortho', workers=1)*np.sqrt(2*np.pi)

def graph(h, xi):
    n = len(h)
    vertices = np.arange(n*n).reshape(n,n)
    left = np.concatenate((vertices[:, :-1].ravel(), vertices[:-1, :].ravel()))
    right = np.concatenate((vertices[:, 1:].ravel(), vertices[1:, :].ravel()))
    w = np.exp(xi*h.ravel())
    cost = (w[left]+w[right])/2
    return coo_matrix((np.concatenate((cost,cost)),
                       (np.concatenate((left,right)),np.concatenate((right,left)))),
                      shape=(n*n,n*n)).tocsr()

def shortest(h, xi, start, end):
    n = len(h)
    start_id, end_id = start[0]*n+start[1], end[0]*n+end[1]
    distance, previous = dijkstra(graph(h,xi), directed=False, indices=start_id,
                                  return_predecessors=True)
    ids = [end_id]
    while ids[-1] != start_id:
        ids.append(int(previous[ids[-1]]))
        if ids[-1] < 0 or len(ids)>n*n:
            raise RuntimeError('Invalid predecessor path')
    ids = np.array(ids[::-1], dtype=np.int64)
    path = np.column_stack((ids//n, ids%n))
    weights = vertex_length_weights(h[path[:,0],path[:,1]],xi)
    cost = float(weights.sum())
    assert np.all(np.abs(np.diff(path,axis=0)).sum(axis=1)==1)
    assert len(np.unique(ids))==len(ids)
    assert np.isclose(cost,distance[end_id],rtol=1e-11,atol=1e-11)
    return path, weights, cost

def vertex_length_weights(values,xi):
    w = np.exp(xi*values)
    edges = (w[:-1]+w[1:])/2
    result = np.zeros(len(w))
    result[:-1] += edges/2
    result[1:] += edges/2
    return result

def circle_average(h, points, radius):
    # Uniform angular quadrature, bilinear interpolation of the lattice field.
    # All requested circles lie strictly within the sampled field.
    theta = np.arange(max(128,int(np.ceil(8*np.pi*radius))))
    theta = theta*2*np.pi/len(theta)
    offsets = np.array([np.cos(theta),np.sin(theta)])*radius
    coordinates = points.T[:,:,None]+offsets[:,None,:]
    assert coordinates.min()>=0 and coordinates.max()<=len(h)-1
    return map_coordinates(h,coordinates,order=1,mode='nearest',prefilter=False).mean(axis=1)

def weighted_quantile(values, weights, q):
    order = np.argsort(values)
    cumulative = np.cumsum(weights[order])
    return float(np.interp(q*cumulative[-1],cumulative,values[order]))

def describe(values,weights):
    weights = weights/weights.sum()
    mean = float(np.sum(weights*values))
    return dict(mean=mean, sd=float(np.sqrt(np.sum(weights*((values-mean)**2)))),
                q05=weighted_quantile(values,weights,.05),
                q50=weighted_quantile(values,weights,.5),
                q95=weighted_quantile(values,weights,.95))

def validate():
    rng = np.random.default_rng(79201)
    path, _, cost = shortest(np.zeros((12,12)),.6,(2,5),(9,5))
    assert cost==7 and len(path)==8
    h = rng.normal(size=(9,9))
    g = graph(h,.4)
    start,end = 2*9+3,7*9+5
    # Independent heap implementation checks scipy's distance on a small graph.
    dist = {start:0.0}
    heap = [(0.0,start)]
    while heap:
        value,u = heapq.heappop(heap)
        if value != dist[u]: continue
        if u==end: break
        for j in range(g.indptr[u],g.indptr[u+1]):
            v,w = int(g.indices[j]),float(g.data[j])
            if value+w<dist.get(v,float('inf')):
                dist[v]=value+w
                heapq.heappush(heap,(value+w,v))
    _,_,scipy_cost = shortest(h,.4,(2,3),(7,5))
    assert np.isclose(scipy_cost,dist[end],rtol=1e-12)
    n=5
    adjacency = graph(np.zeros((n,n)),0).toarray()
    laplacian = 4*np.eye(n*n)-adjacency
    expected = 2*np.pi*np.linalg.inv(laplacian)
    # Empirical covariance independently checks DST normalization, not just its shape.
    draws = np.array([gff(n,rng).ravel() for _ in range(10000)])
    measured = np.einsum('ki,kj->ij',draws,draws,optimize=False)/len(draws)
    covariance_relative_error = float(np.sqrt(np.sum((measured-expected)**2)/np.sum(expected**2)))
    assert covariance_relative_error<.08
    constant = np.full((32,32),3.25)
    assert np.allclose(circle_average(constant,np.array([[10.,15.],[19.,14.]]),4),3.25)
    return dict(zero_field_path=True, independent_heap=True,
                gff_covariance_relative_frobenius_error=covariance_relative_error,
                circle_average_constant=True)

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sizes',type=int,nargs='+',default=[128,256,512])
    parser.add_argument('--replicates',type=int,default=12)
    args=parser.parse_args()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10, 'Run at nice >=10'
    DATA.mkdir(exist_ok=True)
    started=time.time()
    checks=validate()
    rows,histograms=[],[]
    bins=np.linspace(-3,3,61)
    xis=[0.0,.2,1/np.sqrt(6),.8]
    seed=51053
    count_paths=0
    for n in args.sizes:
        for rep in range(args.replicates):
            rng=np.random.default_rng(np.random.SeedSequence([seed,n,rep]))
            h=gff(n,rng)
            lo,hi=n//8,7*n//8
            domain=h[lo:hi,lo:hi]
            start=(n//4-lo,n//2-lo)
            end=(3*n//4-lo,n//2-lo)
            line=np.column_stack((np.arange(n//4,3*n//4+1),np.full(n//2+1,n//2)))
            uniform=rng.integers(lo,hi,size=(1000,2))
            controls={'straight':line,'uniform':uniform}
            paths={}
            radii=[r for r in [n/16,n/32,n/64,n/128,n/256] if r>=2]
            coarse_radius=n/8-1
            cached={key:([circle_average(h,pts,r) for r in radii],circle_average(h,pts,coarse_radius))
                    for key,pts in controls.items()}
            for xi in xis:
                path,path_weights,cost=shortest(domain,xi,start,end)
                path=path+lo
                paths[f'path_xi_{xi:.8f}']=path
                count_paths+=1
                points={'geodesic':path,**controls}
                for kind,pts in points.items():
                    if kind=='geodesic':
                        averages=[circle_average(h,pts,r) for r in radii]
                        coarse=circle_average(h,pts,coarse_radius)
                        weight_options={'vertices':np.ones(len(pts)),'lfpp_length':path_weights}
                    else:
                        averages,coarse=cached[kind]
                        weight_options={'vertices':np.ones(len(pts))}
                        if kind=='straight':
                            weight_options['lfpp_length']=vertex_length_weights(h[pts[:,0],pts[:,1]],xi)
                    for r,average in zip(radii,averages):
                        log_scale=float(np.log((n+1)/r))
                        for estimator,values in [('raw',average/log_scale),
                                                  ('increment',(average-coarse)/np.log(coarse_radius/r))]:
                            for measure,weights in weight_options.items():
                                base=dict(N=n,replicate=rep,xi=xi,radius_pixels=r,
                                          radius_physical=r/(n+1),log_inverse_radius=log_scale,
                                          sample=kind,measure=measure,estimator=estimator,
                                          points=len(pts),cost_grid=cost if kind=='geodesic' else '')
                                rows.append({**base,**describe(values,weights)})
                                hist,_=np.histogram(values,bins=bins,weights=weights/weights.sum())
                                for j,mass in enumerate(hist):
                                    histograms.append({**{k:base[k] for k in ['N','replicate','xi','radius_pixels','sample','measure','estimator']},
                                                       'left':bins[j],'right':bins[j+1],'mass':mass})
                                # Overflow is recorded explicitly rather than renormalized away.
                                histograms.append({**{k:base[k] for k in ['N','replicate','xi','radius_pixels','sample','measure','estimator']},
                                                   'left':'overflow','right':'overflow',
                                                   'mass':float(np.sum(weights[(values<bins[0])|(values>bins[-1])])/weights.sum())})
                if xi==0:
                    assert np.array_equal(path,line)
            np.savez_compressed(DATA/f'field_N{n}_rep{rep:02d}.npz',h=h.astype(np.float32),**paths)
            write_csv(DATA/'path_statistics.csv',rows)
            print(json.dumps({'N':n,'replicate':rep,'paths_so_far':count_paths,'elapsed_seconds':round(time.time()-started,2)}),flush=True)
    write_csv(DATA/'histograms.csv',histograms)
    metadata=dict(seed=seed,sizes=args.sizes,replicates=args.replicates,xis=xis,
                  nice=os.getpriority(os.PRIO_PROCESS,0),thread_limit=1,
                  numpy=np.__version__,scipy=scipy.__version__,
                  elapsed_seconds=time.time()-started,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  path_count=count_paths,checks=checks,
                  timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  covariance='2*pi*(4I-adjacency)^-1, zero exterior Dirichlet',
                  path_domain='central [N/8,7N/8)^2 of the sampled field',
                  edge_weights='(exp(xi*h[u])+exp(xi*h[v]))/2; omitted global mesh factor does not change paths',
                  circle_average='uniform angular quadrature, bilinear interpolation',
                  raw_estimator='h_r / log((N+1)/radius_pixels)',
                  increment_estimator='(h_r-h_R)/log(R/r), R=N/8-1 pixels',
                  sampling='vertex uniform and incident-half-edge LFPP length; each replicate separately normalized',
                  limitations=['finite mesh','lattice anisotropy','constrained path domain','few decades of scale',
                               'histogram modes are not Hausdorff-spectrum maximisers'])
    (DATA/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata),flush=True)

if __name__=='__main__': main()
