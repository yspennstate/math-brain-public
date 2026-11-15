"""PROVED: exact tree coverage and rational accepted leaves. OPEN is retained."""
import json,time,resource,sys
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from cover_face import ROOT,necessary,split_box,polynomials,prove_box

def replay(path='global_cover.json',prefix=''):
    data=json.load(open(path));assert data['root']==[list(p)for p in ROOT]
    nodes=data['nodes'];seen=set();counts=Counter();volumes=Counter();opens=[];positives=[];allN=[];polys=polynomials();start=time.monotonic()
    stack=[(0,[tuple(map(F,p))for p in ROOT])]
    while stack:
        i,box=stack.pop();assert type(i)is int and 0<=i<len(nodes)and i not in seen;seen.add(i);node=nodes[i];kind=node['kind'];counts[kind]+=1
        if kind=='split':
            axis=node['axis'];assert type(axis)is int and 0<=axis<6
            children=node['children'];assert len(children)==2 and all(type(j)is int and j>i for j in children)
            left,right=split_box(box,axis);stack.extend([(children[1],right),(children[0],left)]);continue
        vol=F(1)
        for lo,hi in box:assert lo<hi;vol*=hi-lo
        volumes[kind]+=vol
        entry=dict(node=i,box=[[str(a),str(b)]for a,b in box],volume=str(vol))
        if kind=='excluded':assert necessary(box)==(node['reason'],F(node['bound']))
        elif kind=='positive':
            cert,_=prove_box(polys,box,node['method']=='bernstein');assert cert==node and F(node['lower'])>=0
            positives.append(entry)
            if node['all_N']:allN.append(entry);volumes['all_N_subset']+=vol
        else:assert kind=='open';opens.append(entry)
        if len(seen)%4000==0:
            msg=f'PROVED partial replay: {len(seen)} nodes, {dict(counts)}.';print(msg,flush=True)
            with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
    assert len(seen)==len(nodes)and counts==Counter(data['counts'])
    rootvolume=F(1)
    for lo,hi in ROOT:rootvolume*=F(hi)-F(lo)
    assert rootvolume==1152 and sum(volumes[k]for k in ('positive','excluded','open'))==rootvolume
    assert counts['split']+1==sum(counts[k]for k in ('positive','excluded','open'))
    result=dict(label='PROVED partition and accepted leaves; OPEN sign on open leaves',counts=dict(counts),volumes={k:str(v)for k,v in volumes.items()},root_volume=str(rootvolume),all_N_positive_leaves=len(allN))
    for name,entries,label in [('open_boxes',opens,'OPEN'),('positive_partition_boxes',positives,'PROVED'),('allN_partition_boxes',allN,'PROVED')]:Path(prefix+name+'.json').write_text(json.dumps(dict(label=label,boxes=entries),separators=(',',':'))+'\n')
    Path(prefix+'cover_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PROVED: complete partition replay',result,flush=True)
    with open('LOG.md','a')as f:f.write('\nPROVED: full face ledger replay passed, counts '+str(dict(counts))+', exact coordinate volumes '+str(result['volumes'])+'. OPEN leaves are not sign-certified.\n')
    return result
if __name__=='__main__':replay()
