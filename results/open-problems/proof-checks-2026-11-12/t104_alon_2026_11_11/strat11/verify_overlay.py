"""Exact topology and new accepted leaves, without writing to source folders.

Inherited positive and excluded nodes retain their STRAT10 certificates. This
script checks their partition topology; it does not relabel them as new proofs.
"""
import json,os,sys,hashlib
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
from corner_boxes import corner_record,SOURCE,permutations
from cover_face import necessary,split_box,polynomials,prove_box


def replay():
    data=json.loads((HERE/'corner_cover.json').read_text())
    assert hashlib.sha256((SOURCE/'global_cover.json').read_bytes()).hexdigest()==data['source_sha256']
    old=json.loads((SOURCE/'global_cover.json').read_text())
    os.chdir(SOURCE)
    old_counts=Counter();old_seen=set();old_open={}
    stack=[(0,[tuple(map(F,b)) for b in old['root']])]
    while stack:
        i,b=stack.pop();assert i not in old_seen;old_seen.add(i)
        n=old['nodes'][i];old_counts[n['kind']]+=1
        if n['kind']=='split':
            l,r=split_box(b,n['axis']);a,c=n['children'];assert a>i and c>i
            stack.extend([(a,l),(c,r)])
        elif n['kind']=='open':old_open[i]=b
        else:assert n['kind'] in ('positive','excluded')
    assert len(old_seen)==len(old['nodes']) and old_counts==Counter(old['counts'])==Counter(data['inherited_counts'])
    assert set(old_open)=={r['source_node'] for r in data['roots']}
    assert len(data['roots'])==5244
    counts=Counter();seen=set();volumes=Counter();open_leaves=[]
    polys=polynomials()
    for root in data['roots']:
        stack=[(root['overlay_node'],old_open[root['source_node']])]
        while stack:
            i,b=stack.pop();assert 0<=i<len(data['nodes']) and i not in seen;seen.add(i)
            n=data['nodes'][i];kind=n['kind'];counts[kind]+=1
            if kind=='split':
                l,r=split_box(b,n['axis']);a,c=n['children'];assert a>i and c>i
                stack.extend([(a,l),(c,r)]);continue
            vol=F(1)
            for lo,hi in b:assert lo<hi;vol*=hi-lo
            volumes[kind]+=vol
            if kind=='excluded':assert necessary(b)==(n['reason'],F(n['bound']))
            elif kind=='positive':
                got,_=prove_box(polys,b,try_bernstein=n['method']=='bernstein');assert got==n
            elif kind=='corner':assert corner_record(b)==n
            else:
                assert kind=='open'
                open_leaves.append(dict(node=i,box=[[str(a),str(c)] for a,c in b]))
    assert len(seen)==len(data['nodes']) and counts==Counter(data['counts'])
    assert counts['split']+5244==sum(counts[k] for k in ('positive','corner','excluded','open'))
    oldvol=F(0)
    for b in old_open.values():
        vol=F(1)
        for lo,hi in b:vol*=hi-lo
        oldvol+=vol
    assert oldvol==F(15467841,131072)==sum(volumes.values())
    assert len({tuple(p) for p in permutations()})==15
    total=dict(old_counts)
    for k in ('positive','excluded','split'):total[k]=old_counts[k]+counts[k]
    total['corner']=counts['corner'];total['open']=counts['open']
    result=dict(label='PROVED partition and new accepted leaves; OPEN full sign',
                overlay_counts=dict(counts),combined_counts=total,
                overlay_volumes={k:str(v) for k,v in volumes.items()},source_open_volume=str(oldvol))
    print('PROVED: exact overlay partition and all new accepted leaves.',dict(counts),flush=True)
    print('OPEN: remaining leaves',counts['open'],flush=True)
    return result,open_leaves

if __name__=='__main__':
    result,leaves=replay()
    (HERE/'cover_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'remaining_open_boxes.json').write_text(json.dumps(dict(label='OPEN',boxes=leaves),separators=(',',':'))+'\n')
