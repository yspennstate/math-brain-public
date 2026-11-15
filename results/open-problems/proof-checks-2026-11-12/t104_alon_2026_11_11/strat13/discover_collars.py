"""NUMERICAL LP proposals; every accepted certificate is checked exactly."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys,json,time,resource,argparse,multiprocessing as mp
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from collar_boxes import collar_record,point_bank
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'STRAT12'))
from discover import attempt

def worker(item):
    source,maxdepth=item;node=source['node'];start=time.monotonic();count=0
    try:os.setpriority(os.PRIO_PROCESS,0,10)
    except PermissionError:pass
    # Memoize the exact local certificates before traversing boxes.
    point_bank()
    def visit(box,depth,path):
        nonlocal count
        count+=1
        cert=collar_record(box,node)
        if cert is None:cert=attempt(box)
        if cert is not None:
            cert.update(box=[[str(a),str(b)]for a,b in box],depth=depth,path=path)
            return cert
        if depth==maxdepth:
            return dict(kind='open',box=[[str(a),str(b)]for a,b in box],depth=depth,path=path)
        axis=max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
        a,b=box[axis];mid=(a+b)/2;left=box.copy();right=box.copy()
        left[axis]=(a,mid);right[axis]=(mid,b)
        return dict(kind='split',axis=axis,children=[visit(left,depth+1,path+'0'),visit(right,depth+1,path+'1')])
    tree=visit([tuple(map(F,x))for x in source['box']],0,'')
    return dict(node=node,box=source['box'],tree=tree,visited=count,
                seconds_NUMERICAL=time.monotonic()-start,peak_rss_bytes_NUMERICAL=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

def leaves(tree):
    if tree['kind']=='split':
        for c in tree['children']:yield from leaves(c)
    else:yield tree

def main():
    p=argparse.ArgumentParser();p.add_argument('--depth',type=int,default=100)
    p.add_argument('--workers',type=int,default=2);p.add_argument('--node',type=int)
    args=p.parse_args();assert 1<=args.workers<=4
    inputs=json.loads((HERE/'STRAT12/remaining_open_boxes.json').read_text())['boxes']
    if args.node:inputs=[b for b in inputs if b['node']==args.node]
    records=[];start=time.monotonic()
    with mp.get_context('spawn').Pool(args.workers) as pool:
        for r in pool.imap_unordered(worker,[(b,args.depth)for b in inputs],chunksize=1):
            records.append(r);counts=Counter(x['kind']for x in leaves(r['tree']))
            print('OPEN: candidate partition',r['node'],dict(counts),'visited',r['visited'],'seconds',r['seconds_NUMERICAL'],flush=True)
            name='collar_cover.json' if not args.node else 'collar_cover_'+str(args.node)+'.json'
            (HERE/name).write_text(json.dumps(dict(label='OPEN: independent replay pending',records=records,
                       seconds_NUMERICAL=time.monotonic()-start),separators=(',',':'))+'\n')
            with (HERE/'LOG.md').open('a')as f:f.write('\nOPEN: candidate partition node '+str(r['node'])+': '+str(dict(counts))+'. NUMERICAL elapsed '+str(r['seconds_NUMERICAL'])+' seconds; exact replay pending.\n')

if __name__=='__main__':main()
