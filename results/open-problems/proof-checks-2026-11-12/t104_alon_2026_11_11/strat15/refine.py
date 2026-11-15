"""Refine only unresolved input boxes; LP proposals require exact acceptance."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,resource,hashlib
from fractions import Fraction as F
from pathlib import Path
from discover import attempt,old
import exact_bernstein as ex
from verify_new import collar_replay,key

def closed(r):return not r['failed'] or any(c['kind']=='exclusion'for c in r['certificates'].values())

def visit(source,box,depth,maxdepth):
    r=dict(source,box=[[str(a),str(b)]for a,b in box])
    ok,certs,failed=attempt(r)
    if not ok and not any(c['kind']=='exclusion'for c in certs.values()):
        for coeff in ('c2','d1','C1'):
            if coeff in certs:continue
            ex.select(coeff);cert=old.attempt(box,True)
            if cert is None:break
            cert['coefficient']=coeff;certs[coeff]=cert
            if cert['kind']=='exclusion':break
    if len(certs)==3 or any(c['kind']=='exclusion'for c in certs.values()):
        return dict(kind='certificates',box=r['box'],certificates=certs)
    import collar_boxes as cb
    for node in cb.point_bank():
        for method in ('plane_chart','matrix_ball'):
            cert=cb.collar_record(box,node,method)
            if cert is not None:return dict(kind='collar',box=r['box'],point_node=node,certificate=cert)
    if depth==maxdepth:return dict(kind='open',box=r['box'],certificates=certs)
    axis=max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))
    a,b=box[axis];mid=(a+b)/2;left=box.copy();right=box.copy();left[axis]=(a,mid);right[axis]=(mid,b)
    return dict(kind='split',box=r['box'],axis=axis,children=[visit(source,left,depth+1,maxdepth),visit(source,right,depth+1,maxdepth)])

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('depth',type=int,nargs='?',default=10)
    parser.add_argument('--partial',action='store_true');args=parser.parse_args();maxdepth=args.depth
    collar_replay(json.loads((ex.HERE/'local_uniform.json').read_text()))
    inputs=json.loads((ex.HERE/'inventory.json').read_text())['records']
    inputs+=json.loads((ex.HERE/'domain_audit.json').read_text())['need_new_sign']
    byid={key(r):r for r in inputs}
    bank=json.loads((ex.HERE/'certificates.json').read_text())
    assert bank['total']==9370
    if not args.partial:assert bank['processed']==9370
    failed=[r for r in bank['records']if not closed(r)]
    print('OPEN: refining',len(failed),'boxes',flush=True)
    output=ex.HERE/'refinements.json'
    results=json.loads(output.read_text())['records']if output.exists()else []
    def complete(t):return all(complete(c)for c in t['children'])if t['kind']=='split'else t['kind']!='open'
    done={key(r)for r in results if complete(r['tree'])};results=[r for r in results if key(r)in done]
    start=time.monotonic()
    for r in failed:
        if key(r)in done:continue
        source=byid[key(r)];tree=visit(source,[tuple(map(F,x))for x in r['box']],0,maxdepth)
        results.append(dict(source=r['source'],node=r['node'],path=r.get('path',''),box=r['box'],tree=tree))
        print('refined',key(r),time.monotonic()-start,flush=True)
        (ex.HERE/'refinements.json').write_text(json.dumps(dict(records=results),separators=(',',':'))+'\n')
    if not failed:(ex.HERE/'refinements.json').write_text('{"records":[]}\n')
    from collections import Counter
    counts=Counter()
    def count(t):
        counts[t['kind']]+=1
        for child in t.get('children',[]):count(child)
    for r in results:count(r['tree'])
    previous=json.loads((ex.HERE/'refinement_summary.json').read_text())if(ex.HERE/'refinement_summary.json').exists()else {}
    summary=dict(label='PROVED partial (refine.py): exact accepted refinements; independent replay pending',
        input_boxes=len(results),counts=dict(counts),seconds_NUMERICAL=time.monotonic()-start,
        peak_bytes_NUMERICAL=max(previous.get('peak_bytes_NUMERICAL',0),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    (ex.HERE/'refinement_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    if not args.partial and not counts['open']:
        assert {key(r)for r in results}=={key(r)for r in failed}
        ready={n:hashlib.sha256((ex.HERE/n).read_bytes()).hexdigest()for n in ('certificates.json','refinements.json')}
        (ex.HERE/'READY.json').write_text(json.dumps(ready,indent=2)+'\n')
    with(ex.HERE/'LOG.md').open('a')as f:f.write('\n'+summary['label']+'; '+str(summary['counts'])+'.\n')
    print(summary,flush=True)
if __name__=='__main__':main()
