"""Exact input frontier inventory; no sign certificates are transferred here."""
import sys,json,hashlib
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
S13=HERE/'STRAT14/STRAT13'; S12=S13/'STRAT12'; S10=S12/'STRAT10'

def tree_leaves(t,path=''):
    if t['kind']=='split':
        for i,c in enumerate(t['children']):yield from tree_leaves(c,path+str(i))
    else:yield path,t

def flat_leaves(bank,roots=None):
    nodes=bank['nodes']; seen=set(); stack=roots or [(0,bank.get('root',[['1','4'],['-1','0'],['-4','4'],['-1','1/2'],['-4','4'],['0','4']]))]
    while stack:
        i,box=stack.pop();assert i not in seen;seen.add(i);n=nodes[i]
        if n['kind']=='split':
            a=n['axis'];lo,hi=map(F,box[a]);mid=str((lo+hi)/2)
            left=[list(x)for x in box];right=[list(x)for x in box]
            left[a][1]=mid;right[a][0]=mid
            stack.extend([(n['children'][1],right),(n['children'][0],left)])
        else:yield i,box,n
    assert len(seen)==len(nodes)

def collect():
    records=[];counts=Counter();exclusions=Counter()
    old=json.loads((S10/'global_cover.json').read_text())
    for node,box,n in flat_leaves(old):
        if n['kind']=='positive':
            if n['all_N']:counts['STRAT10 all-N positivity']+=1
            else:records.append(dict(source='STRAT10',node=node,box=box,old=n));counts['STRAT10 N6-only positivity']+=1
        elif n['kind']=='excluded':exclusions[n['reason']]+=1
    overlay=json.loads((S12/'STRAT11/corner_cover.json').read_text())
    oldopens={i:b for i,b,n in flat_leaves(old)if n['kind']=='open'}
    roots=[(r['overlay_node'],oldopens[r['source_node']])for r in overlay['roots']]
    for i,box,n in flat_leaves(overlay,roots):
        if n['kind']=='positive':
            if n.get('all_N'):counts['STRAT11 all-N positivity']+=1
            else:records.append(dict(source='STRAT11',node=i,box=box,old=n));counts['STRAT11 N6-only positivity']+=1
        elif n['kind']=='excluded':exclusions['STRAT11:'+n['reason']]+=1
    for source,file in [('STRAT12',S12/'certificates.json'),('STRAT13',S13/'collar_cover.json')]:
        bank=json.loads(file.read_text())
        for r in bank['records']:
            for path,n in tree_leaves(r['tree']):
                counts[source+' '+n['kind']]+=1
                if n['kind']in ('positivity','collar'):
                    records.append(dict(source=source,node=r['node'],path=path,box=n['box'],old=n))
                elif n['kind']=='exclusion':exclusions[source+':Farkas']+=1
    assert counts['STRAT10 all-N positivity']==24458
    assert counts['STRAT10 N6-only positivity']==250
    assert counts['STRAT12 positivity']==7702
    assert counts['STRAT13 positivity']==366 and counts['STRAT13 collar']==17
    return dict(label='PROVED (inventory.py): structural inventory, not all-N signs',counts=dict(counts),
                excluded_reasons=dict(exclusions),records=records,
                independent_local_regions=['STRAT11 corner ball, all fifteen permutations'],
                warning='N6-only ratio/scale exclusions also require audit for all N; they are not automatically transferable.')

if __name__=='__main__':
    result=collect();(HERE/'inventory.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    hashes={str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted((HERE/'STRAT14').rglob('*'))if p.is_file()}
    (HERE/'source_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()if k!='records'},indent=2))
