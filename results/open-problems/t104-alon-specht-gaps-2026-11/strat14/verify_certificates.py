"""Exact replay of the constrained Bernstein bank and its box partition.

No SciPy, numerical LP, float conversion or floating sign decision is used.
Wall-clock timing and resource readings are reported as NUMERICAL metadata.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json,hashlib,time,multiprocessing as mp,resource
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import prod
from exact_bernstein import verify_certificate,volume,data,conversion

HERE=Path(__file__).resolve().parent


def verify_basis():
    # Independently expand every Bernstein representation used by the
    # converter. All polynomial coefficients are rational, never floats.
    from math import comb
    for n in range(9):
        scale,mat=conversion(n)
        assert all(abs(c)<=scale for row in mat for c in row)
        for k in range(n+1):
            coeff=[F(0)]*(n+1)
            for i in range(n+1):
                for j in range(n-i+1):
                    coeff[i+j]+=F(mat[i][k],scale)*comb(n,i)*comb(n-i,j)*(-1)**j
            expected=[F(comb(k,j)*2**j*(-1)**(k-j)) if j<=k else F(0)
                      for j in range(n+1)]
            assert coeff==expected


def visit(tree,box,depth=0,path=''):
    kind=tree['kind']
    if kind=='split':
        axis=tree['axis'];assert type(axis) is int and 0<=axis<6
        assert axis==max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
        lo,hi=box[axis];mid=(lo+hi)/2
        left=box.copy();right=box.copy();left[axis]=(lo,mid);right[axis]=(mid,hi)
        assert len(tree['children'])==2
        a=visit(tree['children'][0],left,depth+1,path+'0')
        b=visit(tree['children'][1],right,depth+1,path+'1')
        a['counts'].update(b['counts']);a['volumes'].update(b['volumes'])
        a['split_nodes']+=b['split_nodes']+1;a['max_depth']=max(a['max_depth'],b['max_depth'])
        a['open_leaves'].extend(b['open_leaves'])
        return a
    assert kind in ('exclusion','positivity','open')
    assert [tuple(map(F,x)) for x in tree['box']]==box
    assert tree['depth']==depth and tree['path']==path
    if kind!='open':
        lo,method=verify_certificate(tree)
        assert lo==F(tree['lower']) and method==tree['verification']
    return dict(counts=Counter({kind:1}),volumes=Counter({kind:volume(box)}),
                split_nodes=0,max_depth=depth,open_leaves=[tree] if kind=='open' else [])


def work(record):
    box=[tuple(map(F,x)) for x in record['box']]
    result=visit(record['tree'],box)
    assert sum(result['volumes'].values())==volume(box)
    kinds=set(result['counts'])
    original=('open' if 'open' in kinds else
              'closed_after_splitting' if result['split_nodes'] else next(iter(kinds)))
    result.update(node=record['node'],box=record['box'],original=original)
    return result


def main():
    start=time.monotonic();verify_basis()
    source=HERE/'STRAT8/open_boxes.json'
    bank=json.loads((HERE/'certificates.json').read_text())
    assert bank['schema']==1
    assert bank['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    inputs=json.loads(source.read_text())['boxes'];byid={b['node']:b['box'] for b in inputs}
    assert len(byid)==len(inputs)==5272
    before=sum((volume(b['box']) for b in inputs),F(0))
    assert before==F(30937023,262144)
    records=bank['records'];ids=[r['node'] for r in records]
    assert len(ids)==len(set(ids)) and set(ids)<=set(byid)
    assert all(byid[r['node']]==r['box'] for r in records)
    counts=Counter();volumes=Counter();original=Counter();splits=0;depth=0;opens=[]
    # Exactly four CPU workers, with the same request for nice 5 as discovery.
    # The sandbox rejection is metadata; it is never a mathematical premise.
    from exact_bernstein import data
    initialize=data
    with mp.get_context('spawn').Pool(2,initializer=initialize) as pool:
        for n,result in enumerate(pool.imap_unordered(work,records,chunksize=1),1):
            counts.update(result['counts']);volumes.update(result['volumes'])
            original[result['original']]+=1;splits+=result['split_nodes'];depth=max(depth,result['max_depth'])
            for leaf in result['open_leaves']:
                opens.append(dict(node=result['node'],**leaf))
            if n%500==0:print('PROVED partial (verify_certificates.py): exact replay',n,'original boxes',flush=True)
    missing=set(byid)-set(ids)
    unprocessed=sum((volume(byid[n]) for n in missing),F(0))
    assert sum(volumes.values())+unprocessed==before
    discovery=bank['summary']
    assert dict(counts)==discovery['leaf_counts']
    assert dict(original)==discovery['original_classification']
    assert splits==discovery['split_nodes'] and depth==discovery['max_depth']
    assert str(volumes['open']+unprocessed)==discovery['open_volume_after']
    assert {k:str(v) for k,v in volumes.items()}==discovery['volumes']
    summary=dict(label='PROVED (verify_certificates.py): exact certificate and input-leaf subdivision replay; OPEN: remaining sign',
                 original_boxes=len(inputs),processed=len(ids),unprocessed=len(missing),
                 original_classification=dict(original),leaf_counts=dict(counts),split_nodes=splits,
                 max_depth=depth,volumes={k:str(v) for k,v in volumes.items()},
                 open_volume_before=str(before),open_volume_after=str(volumes['open']+unprocessed),
                 elapsed_seconds_NUMERICAL=time.monotonic()-start,
                 parent_peak_rss_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (HERE/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (HERE/'remaining_open_boxes.json').write_text(json.dumps(dict(label='OPEN',boxes=opens),indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)
    with (HERE/'LOG.md').open('a') as f:f.write('\nPROVED (verify_certificates.py): all retained new certificates and subdivision volumes replayed. NUMERICAL elapsed '+str(summary['elapsed_seconds_NUMERICAL'])+' seconds.\n')


if __name__=='__main__':main()
