"""PROVED partition: reuse STRAT8 split geometry, reclassify every sign at N=6."""
import json,time
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from cover_face import ROOT,necessary,prove_box,split_box,polynomials

def main():
    data=json.load(open('strat8_partition.json'));assert data['root']==[list(p)for p in ROOT]
    old=data['nodes'];polys=polynomials();nodes=[];counts=Counter();examined=0;start=time.monotonic()
    def walk(i,box):
        nonlocal examined
        index=len(nodes);nodes.append(None);examined+=1;node=old[i];exc=necessary(box)
        if exc:rec=dict(kind='excluded',reason=exc[0],bound=str(exc[1]));counts['excluded']+=1
        elif node['kind']=='split':
            axis=node['axis'];left,right=split_box(box,axis);a=walk(node['children'][0],left);b=walk(node['children'][1],right);rec=dict(kind='split',axis=axis,children=[a,b]);counts['split']+=1
        else:
            rec,_=prove_box(polys,box,True)
            if rec:counts['positive']+=1
            else:rec=dict(kind='open');counts['open']+=1
        nodes[index]=rec
        if examined%1000==0:
            msg=f'PROVED partial reused-geometry N=6 ledger: {examined} visits; {dict(counts)}. OPEN signs retained.'
            print(msg,flush=True)
            with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
        return index
    walk(0,[tuple(map(F,p))for p in ROOT])
    counts=Counter(n['kind']for n in nodes)
    Path('global_cover.json').write_text(json.dumps(dict(label='PROVED partition, OPEN sign on open leaves',root=ROOT,nodes=nodes,counts=dict(counts)),separators=(',',':'))+'\n')
    msg=f'PROVED: N=6 reclassification of inherited split geometry completed: {dict(counts)}. NUMERICAL seconds {time.monotonic()-start}.'
    print(msg,flush=True)
    with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
if __name__=='__main__':main()
