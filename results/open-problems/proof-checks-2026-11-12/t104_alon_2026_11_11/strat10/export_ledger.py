"""PROVED partition geometry/counts/volumes; signs replay separately in verify_cover."""
import json
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
from cover_face import ROOT,split_box

def export():
    data=json.load(open('global_cover.json'));nodes=data['nodes'];counts=Counter();volumes=Counter();seen=set();opens=[];positive=[];alln=[]
    stack=[(0,[tuple(map(F,p))for p in ROOT])]
    while stack:
        i,box=stack.pop();assert i not in seen;seen.add(i);n=nodes[i];counts[n['kind']]+=1
        if n['kind']=='split':
            left,right=split_box(box,n['axis']);stack.extend([(n['children'][1],right),(n['children'][0],left)]);continue
        volume=F(1)
        for lo,hi in box:volume*=hi-lo
        volumes[n['kind']]+=volume
        entry=dict(node=i,box=[[str(a),str(b)]for a,b in box],volume=str(volume))
        if n['kind']=='open':opens.append(entry)
        elif n['kind']=='positive':
            positive.append(entry)
            if n['all_N']:alln.append(entry);volumes['all_N_subset']+=volume
    assert len(seen)==len(nodes)and counts==Counter(data['counts'])
    assert sum(volumes[k]for k in ('positive','excluded','open'))==1152
    result=dict(label='PROVED partition and accepted leaves; OPEN sign on open leaves',counts=dict(counts),volumes={k:str(v)for k,v in volumes.items()},root_volume='1152',all_N_positive_leaves=len(alln))
    for name,entries,label in [('open_boxes',opens,'OPEN'),('positive_partition_boxes',positive,'PROVED'),('allN_partition_boxes',alln,'PROVED')]:Path(name+'.json').write_text(json.dumps(dict(label=label,boxes=entries),separators=(',',':'))+'\n')
    Path('cover_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PROVED partial: exact ledger geometry/counts/volumes',result,flush=True)
    return result
if __name__=='__main__':export()
