"""NUMERICAL discovery on retained leaves; preserve all accepted certificates."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import json,time,copy,multiprocessing as mp,argparse
from pathlib import Path
from discover import work,initialize,leaves,checkpoint

HERE=Path(__file__).resolve().parent

def adjust(tree,depth,prefix):
    if tree['kind']=='split':
        for child in tree['children']:adjust(child,depth,prefix)
    else:
        tree['depth']+=depth;tree['path']=prefix+tree['path']

def replace(tree,path,new):
    if not path:return new
    assert tree['kind']=='split'
    i=int(path[0]);tree['children'][i]=replace(tree['children'][i],path[1:],new)
    return tree

def refine_work(item):
    node,path,depth,box,maxdepth,products=item
    result=work((dict(node=node,box=box),maxdepth-depth,products))
    adjust(result['tree'],depth,path)
    result['replace_path']=path
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--depth',type=int,default=10)
    p.add_argument('--products',action='store_true');args=p.parse_args()
    bank=json.loads((HERE/'certificates.json').read_text())
    records=bank['records'];assert len(records)==5272
    before=copy.deepcopy(bank)
    # Keep the first stage as a reviewable independent checkpoint.
    snapshot=HERE/('certificates_depth'+str(bank['summary']['max_depth'])+'.json')
    if not snapshot.exists():snapshot.write_text(json.dumps(before,separators=(',',':'))+'\n')
    byid={r['node']:r for r in records}
    jobs=[(r['node'],leaf['path'],leaf['depth'],leaf['box'],args.depth,args.products)
          for r in records for leaf in leaves(r['tree']) if leaf['kind']=='open' and leaf['depth']<args.depth]
    options=dict(bank['options'],depth=args.depth,products=args.products,
                 refinement_from_depth=bank['summary']['max_depth'])
    started=time.monotonic()
    print('OPEN: refining',len(jobs),'retained leaves to total depth',args.depth,'products',args.products,flush=True)
    with mp.get_context('spawn').Pool(2,initializer=initialize) as pool:
        for n,result in enumerate(pool.imap_unordered(refine_work,jobs,chunksize=1),1):
            old=byid[result['node']]
            old['tree']=replace(old['tree'],result['replace_path'],result['tree'])
            old['seconds']+=result['seconds']
            old['peak_worker_rss_bytes']=max(old['peak_worker_rss_bytes'],result['peak_worker_rss_bytes'])
            if n%25==0:
                print('OPEN: refined',n,'of',len(jobs),'retained leaves',flush=True)
                checkpoint(records,options,5272,time.monotonic()-started)
    checkpoint(records,options,5272,time.monotonic()-started)
    with (HERE/'LOG.md').open('a') as f:
        f.write('\nOPEN: refinement complete; exact acceptance performed per certificate, independent replay pending. NUMERICAL additional elapsed '+str(time.monotonic()-started)+' seconds.\n')

if __name__=='__main__':main()
