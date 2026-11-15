"""NUMERICAL LP discovery, followed by exact certificate acceptance.

Four multiprocessing workers; checkpoint every 500 original boxes. A failed
LP is never an exclusion proof. Exact replay is verify_certificates.py.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse,json,time,multiprocessing as mp,resource,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations_with_replacement
from collections import Counter
import numpy as np
from scipy.optimize import linprog
from exact_bernstein import (data,normal,controls,degree,active_constraints,
                             verify_certificate,multiply,volume)

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'STRAT11/remaining_open_boxes.json'
TARGET_DEG=(6,)*6


def initialize():
    # macOS refuses priority changes in this sandbox. Record the actual result.
    try:
        os.setpriority(os.PRIO_PROCESS,0,5)
        priority='nice 5'
    except PermissionError:
        priority='OPEN: sandbox denied nice 5'
    # A per-worker 600 MiB address-space cap on Linux; macOS RLIMIT_AS is
    # unreliable, so the parent also measures aggregate actual RSS.
    if sys_platform_linux():
        resource.setrlimit(resource.RLIMIT_AS,(600*1024**2,600*1024**2))
    global PRIORITY
    PRIORITY=priority
    data()


def sys_platform_linux():
    import sys
    return sys.platform.startswith('linux')


def floats(poly,box):
    tr,den=normal(poly,box)
    return {m:float(F(c,den)) for m,c in tr.items()}


def tensor(tr,degrees):
    return controls(tr,degrees,False)[0].ravel()


def matrix(gs,box,degrees,normalized=None):
    vals=np.empty((len(gs),int(np.prod([n+1 for n in degrees]))),dtype=float)
    names=[];scales=[];normals={} if normalized is None else normalized
    for i,(key,p) in enumerate(gs.items()):
        tr=normals.get(key)
        if tr is None:
            tr=normals[key]=floats(p,box)
        row=tensor(tr,degrees)
        scale=max(float(np.max(np.abs(row))),1e-20)
        vals[i]=row/scale;scales.append(scale);names.append(key)
    return vals,names,np.array(scales),normals


def corner_indices(degrees):
    return np.ravel_multi_index(np.array(list(product(*[(0,n) for n in degrees]))).T,
                                tuple(n+1 for n in degrees))


def solve(G, b, degrees, exclusion=False, rounds=12):
    """Cutting-plane LP; all omitted rows are checked before returning."""
    n=len(G)
    indices=set(map(int,corner_indices(degrees)))
    indices.update(map(int,np.argsort(b)[:16]))
    objective=np.r_[np.zeros(n),-1.0]
    # Unit mass removes the homogeneous exclusion scaling ambiguity.
    equality=np.r_[np.ones(n),0.0][None,:] if exclusion else None
    for iteration in range(rounds):
        ids=np.array(sorted(indices),dtype=int)
        A=np.column_stack((G[:,ids].T,np.ones(len(ids))))
        result=linprog(objective,A_ub=A,b_ub=b[ids],
                       A_eq=equality,b_eq=[1.] if exclusion else None,
                       bounds=[(0,None if exclusion else 1000)]*n+[(None,1.)],
                       method='highs',options={'dual_feasibility_tolerance':1e-8,
                                               'primal_feasibility_tolerance':1e-8,
                                               'threads':1})
        if not result.success or result.x[-1]<=1e-8:
            return None
        lam=result.x[:-1]
        # Elementwise reduction avoids macOS Accelerate's spurious floating
        # status warnings in matrix-vector multiplication on these tiny LPs.
        residual=b.copy()
        for v,row in zip(lam,G):
            if v:residual-=v*row
        lower=float(residual.min())
        if lower>1e-8:
            return lam,lower
        bad=np.argpartition(residual,min(31,len(residual)-1))[:32]
        before=len(indices);indices.update(map(int,bad))
        if len(indices)==before:
            return None
    return None


def candidate(box, kind, lam, names, scales, tscale=1, degrees=None):
    for maxden in (10**6,10**9,10**12):
        weights={name:str(F(float(v*tscale/s)).limit_denominator(maxden))
                 for name,v,s in zip(names,lam,scales) if v>1e-10}
        record=dict(box=[[str(a),str(b)] for a,b in box],kind=kind,**{'lambda':weights})
        if degrees is not None:record['bernstein_degrees']=list(degrees)
        try:
            lo,method=verify_certificate(record)
        except AssertionError:
            continue
        record.update(lower=str(lo),verification=method)
        return record
    return None


def attempt(box, products=False):
    target,_=data()
    gs=active_constraints(box)
    if products:
        # Products of weakly nonnegative row and edge constraints are valid.
        # Exclude quartics here to keep the tensor coordinate degrees <=6.
        base={k:p for k,p in gs.items() if k.startswith('g') or k.startswith('row')}
        for a,b in combinations_with_replacement(base,2):
            gs[a+'*'+b]=multiply(base[a],base[b])
    deg=tuple(max(degree(p)[i] for p in gs.values()) for i in range(6))
    G,names,scales,normals=matrix(gs,box,deg)
    answer=solve(G,np.zeros(G.shape[1]),deg,True)
    if answer:
        cert=candidate(box,'exclusion',answer[0],names,scales,degrees=deg)
        if cert:
            return cert
    del G
    t=tensor(floats(target,box),TARGET_DEG)
    tscale=max(float(np.max(np.abs(t))),1e-20)
    if float(t.min())>1e-8*tscale:
        cert=candidate(box,'positivity',[],[],[],tscale,degrees=TARGET_DEG)
        if cert:
            return cert
    G,names,scales,_=matrix(gs,box,TARGET_DEG,normals)
    answer=solve(G,t/tscale,TARGET_DEG)
    if answer:
        return candidate(box,'positivity',answer[0],names,scales,tscale,degrees=TARGET_DEG)
    return None


def work(item):
    source,maxdepth,use_products=item
    start=time.monotonic();box=[tuple(map(F,x)) for x in source['box']]
    # Leave the strict-certificate obstruction in the ordinary ledger. It is
    # not treated as an exclusion or as a counterexample.
    def visit(box,depth,path):
        cert=attempt(box)
        if cert is None and use_products and depth==maxdepth:
            cert=attempt(box,True)
        if cert:
            cert.update(depth=depth,path=path)
            return cert
        if depth==maxdepth:
            return dict(kind='open',box=[[str(a),str(b)] for a,b in box],
                        depth=depth,path=path)
        axis=max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
        a,b=box[axis];mid=(a+b)/2
        left=box.copy();right=box.copy();left[axis]=(a,mid);right[axis]=(mid,b)
        return dict(kind='split',axis=axis,children=[visit(left,depth+1,path+'0'),
                                                     visit(right,depth+1,path+'1')])
    result=dict(node=source['node'],box=source['box'],tree=visit(box,0,''),
                seconds=time.monotonic()-start,priority=PRIORITY,
                peak_worker_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys_platform_linux():result['peak_worker_rss_bytes']*=1024
    return result


def leaves(tree):
    if tree['kind']=='split':
        for c in tree['children']:yield from leaves(c)
    else:yield tree


def summarize(records,total):
    counts=Counter();volumes=Counter();original=Counter();depth=0;split=0
    for r in records:
        ls=list(leaves(r['tree']));kinds={x['kind'] for x in ls}
        if 'open' in kinds:original['open']+=1
        elif len(ls)>1:original['closed_after_splitting']+=1
        else:original[ls[0]['kind']]+=1
        split+=len(ls)-1
        for x in ls:
            counts[x['kind']]+=1;volumes[x['kind']]+=volume(x['box']);depth=max(depth,x['depth'])
    unprocessed=total-len(records)
    inputboxes=json.loads(SOURCE.read_text())['boxes']
    done={r['node'] for r in records}
    unprocessedvol=sum((volume(x['box']) for x in inputboxes if x['node'] not in done),F(0))
    return dict(label='OPEN: discovery ledger; independent exact replay pending',
                original_boxes=total,processed=len(records),unprocessed=unprocessed,
                original_classification=dict(original),leaf_counts=dict(counts),split_nodes=split,
                max_depth=depth,volumes={k:str(v) for k,v in volumes.items()},
                open_volume_before='3333609/32768',
                open_volume_after=str(volumes['open']+unprocessedvol),
                unprocessed_volume=str(unprocessedvol),
                peak_worker_rss_bytes=max((r['peak_worker_rss_bytes'] for r in records),default=0))


def checkpoint(records,options,total,elapsed):
    summary=summarize(records,total)
    parent_peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys_platform_linux():parent_peak*=1024
    summary['parent_peak_rss_bytes_NUMERICAL']=parent_peak
    summary['conservative_process_peak_bound_bytes_NUMERICAL']=4*summary['peak_worker_rss_bytes']+parent_peak
    summary['elapsed_seconds_NUMERICAL']=elapsed
    bank=dict(schema=1,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              options=options,summary=summary,records=records)
    tmp=HERE/'certificates.tmp.json';tmp.write_text(json.dumps(bank,separators=(',',':'))+'\n')
    tmp.replace(HERE/'certificates.json')
    (HERE/'discovery_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    line=f"OPEN: discovery checkpoint {len(records)}/{total}; original {summary['original_classification']}; leaves {summary['leaf_counts']}; max depth {summary['max_depth']}; remaining chart volume {summary['open_volume_after']}. NUMERICAL elapsed {elapsed:.2f} seconds."
    print(line,flush=True)
    with (HERE/'LOG.md').open('a') as f:f.write('\n'+line+'\n')
    (HERE/'RESULT.md').write_text('OPEN: Search in progress; independent replay pending.\n\n'+line+'\n\nOPEN: nice 5 and shared mesh/checklist writes denied by sandbox. STRAT11 inherited verification scripts are absent.\n')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--depth',type=int,default=0)
    parser.add_argument('--products',action='store_true');parser.add_argument('--limit',type=int)
    parser.add_argument('--resume',action='store_true')
    args=parser.parse_args();options=dict(depth=args.depth,products=args.products,workers=4)
    inputs=json.loads(SOURCE.read_text())['boxes'];records=[]
    if args.resume and (HERE/'certificates.json').exists():
        old=json.loads((HERE/'certificates.json').read_text())
        assert old['options']==options
        assert old['source_sha256']==hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        records=old['records']
    done={r['node'] for r in records}
    todo=[b for b in inputs if b['node'] not in done]
    if args.limit is not None:todo=todo[:args.limit]
    started=time.monotonic()
    with mp.get_context('spawn').Pool(4,initializer=initialize) as pool:
        for result in pool.imap_unordered(work,[(b,args.depth,args.products) for b in todo],chunksize=1):
            records.append(result)
            if len(records)%500==0:
                checkpoint(records,options,len(inputs),time.monotonic()-started)
    checkpoint(records,options,len(inputs),time.monotonic()-started)


if __name__=='__main__':main()
