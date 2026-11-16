"""Exact final partition, including physical collars on the nine limits."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json,hashlib,time,multiprocessing as mp,resource
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from exact_bernstein import verify_certificate,volume,data
from verify_certificates import verify_basis
from collar_boxes import collar_record,point_bank

HERE=Path(__file__).resolve().parent

def visit(tree,box,node,depth=0,path=''):
    kind=tree['kind']
    if kind=='split':
        axis=tree['axis'];assert type(axis)is int and 0<=axis<6
        assert axis==max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
        a,b=box[axis];mid=(a+b)/2;left=box.copy();right=box.copy()
        left[axis]=(a,mid);right[axis]=(mid,b)
        assert len(tree['children'])==2
        x=visit(tree['children'][0],left,node,depth+1,path+'0')
        y=visit(tree['children'][1],right,node,depth+1,path+'1')
        x['counts'].update(y['counts']);x['volumes'].update(y['volumes'])
        x['splits']+=y['splits']+1;x['depth']=max(x['depth'],y['depth'])
        x['opens'].extend(y['opens'])
        return x
    assert tree['box']==[[str(a),str(b)]for a,b in box]
    assert tree['depth']==depth and tree['path']==path
    assert kind in ('positivity','exclusion','collar','open')
    if kind in ('positivity','exclusion'):
        lo,method=verify_certificate(tree)
        assert lo==F(tree['lower']) and method==tree['verification']
    elif kind=='collar':
        assert node in point_bank()
        cert=collar_record(box,node,tree['method']);assert cert is not None
        assert {k:tree[k]for k in cert}==cert
    return dict(counts=Counter({kind:1}),volumes=Counter({kind:volume(box)}),
                splits=0,depth=depth,opens=[dict(node=node,**tree)]if kind=='open'else [])

def work(record):
    result=visit(record['tree'],[tuple(map(F,x))for x in record['box']],record['node'])
    assert sum(result['volumes'].values())==volume(record['box'])
    result['rss']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return result

def main():
    start=time.monotonic();verify_basis()
    source=HERE/'STRAT8/open_boxes.json'
    bank=json.loads((HERE/'certificates.json').read_text())
    assert bank['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
    inputs=json.loads(source.read_text())['boxes'];byid={x['node']:x['box']for x in inputs}
    assert len(byid)==len(inputs)==5272
    # Reconstruct the original OPEN frontier from the whole STRAT8 tree;
    # a separate exported list is never accepted on trust.
    original=json.loads((HERE/'STRAT8/global_cover.json').read_text())
    found={};seen=set()
    def original_visit(index,box):
        assert index not in seen;seen.add(index);node=original['nodes'][index]
        if node['kind']=='split':
            axis=node['axis'];a,b=box[axis];mid=(a+b)/2
            left=box.copy();right=box.copy();left[axis]=(a,mid);right[axis]=(mid,b)
            assert len(node['children'])==2
            original_visit(node['children'][0],left);original_visit(node['children'][1],right)
        elif node['kind']=='open':found[index]=[[str(a),str(b)]for a,b in box]
    original_visit(0,[tuple(map(F,x))for x in original['root']])
    assert len(seen)==len(original['nodes']) and found==byid
    records=bank['records'];assert len(records)==5272
    assert {r['node']:r['box']for r in records}==byid
    assert len({r['node']for r in records})==len(records)
    counts=Counter();volumes=Counter();splits=depth=rss=0;opens=[]
    with mp.get_context('spawn').Pool(2,initializer=data)as pool:
        for n,result in enumerate(pool.imap_unordered(work,records,chunksize=1),1):
            counts.update(result['counts']);volumes.update(result['volumes']);splits+=result['splits']
            depth=max(depth,result['depth']);rss=max(rss,result['rss']);opens.extend(result['opens'])
            if n%1000==0:print('PROVED partial (verify_partition.py):',n,'original leaves replayed',flush=True)
    before=sum((volume(x['box'])for x in inputs),F(0))
    assert before==F(30937023,262144) and sum(volumes.values())==before
    assert sum(counts.values())==splits+5272
    assert sum(F(x['lower_Cface'])==0 for x in original['nodes']if x['kind']=='positive'and 'lower_Cface'in x)==0
    combined=dict(positive=24702+counts['positivity'],excluded=10208+counts['exclusion'],
                  collar=counts['collar'],open=counts['open'],split=40181+splits)
    assert sum(v for k,v in combined.items()if k!='split')==combined['split']+1
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result=dict(label='PROVED (verify_partition.py): exact partition and every new leaf replayed',
                original_boxes=5272,leaf_counts=dict(counts),volumes={k:str(v)for k,v in volumes.items()},
                input_volume=str(before),split_nodes=splits,max_depth=depth,combined_counts=combined,
                combined_chart_volume='1152',open_leaves=len(opens),
                seconds_NUMERICAL=time.monotonic()-start,worker_peak_bytes_NUMERICAL=rss,
                parent_peak_bytes_NUMERICAL=peak,conservative_peak_bytes_NUMERICAL=2*rss+peak)
    assert result['conservative_peak_bytes_NUMERICAL']<2400000000
    (HERE/'partition_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'remaining_open_boxes.json').write_text(json.dumps(dict(label='OPEN'if opens else 'PROVED (verify_partition.py): zero OPEN leaves',boxes=opens),indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    return result

if __name__=='__main__':main()
