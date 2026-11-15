"""Exact overlay on STRAT10's OPEN leaves; all outputs stay in STRAT11."""
import json,os,sys,time,hashlib
from pathlib import Path
from collections import Counter,deque
from fractions import Fraction as F
sys.dont_write_bytecode=True
ROOTDIR=Path(__file__).resolve().parent
from corner_boxes import corner_record,SOURCE
from cover_face import necessary,split_box,polynomials,prove_box


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def discover(limit=12000):
    # The imported read-only helpers resolve their certificate banks by cwd.
    os.chdir(SOURCE)
    source=json.load(open('global_cover.json'))
    rootbox=[tuple(map(F,p)) for p in source['root']]
    pending=[(0,rootbox)];roots=[]
    while pending:
        i,b=pending.pop();n=source['nodes'][i]
        if n['kind']=='split':
            l,r=split_box(b,n['axis']);pending.extend([(n['children'][1],r),(n['children'][0],l)])
        elif n['kind']=='open':roots.append((i,b))
    assert len(roots)==5244
    roots.sort()
    queue=deque();nodes=[];rootmap=[]
    for old,b in roots:
        i=len(nodes);nodes.append(None);rootmap.append(dict(source_node=old,overlay_node=i));queue.append((i,b,0))
    polys=polynomials();counts=Counter();start=time.monotonic()
    for examined in range(limit):
        if not queue:break
        i,b,depth=queue.popleft()
        exc=necessary(b)
        if exc:nodes[i]=dict(kind='excluded',reason=exc[0],bound=str(exc[1]));counts['excluded']+=1
        else:
            rec=corner_record(b)
            if rec:nodes[i]=rec;counts['corner']+=1
            else:
                rec,imp=prove_box(polys,b,try_bernstein=True)
                if rec:nodes[i]=rec;counts['positive']+=1
                else:
                    # Exact integer impact chooses the axis; periodically use width.
                    axis=max(range(6),key=lambda j:((b[j][1]-b[j][0]) if depth%4==3 else imp[j],-j))
                    l,r=split_box(b,axis);a=len(nodes);nodes.extend([None,None]);nodes[i]=dict(kind='split',axis=axis,children=[a,a+1]);queue.extend([(a,l,depth+1),(a+1,r,depth+1)]);counts['split']+=1
        if (examined+1)%500==0:
            msg=f'OPEN: overlay {examined+1} visits; {dict(counts)}; frontier {len(queue)}.'
            print(msg,flush=True)
            with (ROOTDIR/'LOG.md').open('a')as f:f.write('\n'+msg+'\n')
    for i,b,depth in queue:
        assert nodes[i]is None;nodes[i]=dict(kind='open')
    counts['open']=len(queue)
    data=dict(label='OPEN sign; exact partition overlay, replay verify_overlay.py',
              source='STRAT10/global_cover.json',source_sha256=sha(SOURCE/'global_cover.json'),
              inherited_counts=source['counts'],roots=rootmap,nodes=nodes,counts=dict(counts),
              examined=sum(v for k,v in counts.items() if k!='open'))
    (ROOTDIR/'corner_cover.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
    print('OPEN: saved overlay',dict(counts),'NUMERICAL seconds',time.monotonic()-start,flush=True)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=12000);discover(p.parse_args().limit)
