"""PROVED: exact replay of partition coverage, exclusions and sign bounds.

OPEN leaves are retained; verification success does not mean full positivity.
Every rational box is reconstructed from the root and its path of bisections.
"""
import json,time,resource
from fractions import Fraction as F
from collections import Counter
from cover_face import ROOT,necessary,split_box
from centered_bounds import integer_polynomial,box_bound
from zero_face import construct
from axis_bernstein import box_bound as bernstein_bound


def replay():
    data=json.load(open('global_cover.json'));assert data['root']==[list(x)for x in ROOT]
    nodes=data['nodes'];poly=integer_polynomial(construct()[-1],80)
    seen=set();counts=Counter();volumes=Counter();open_boxes=[];positive_boxes=[]
    start=time.time()
    def walk(index,box):
        assert isinstance(index,int)and 0<=index<len(nodes)and index not in seen
        seen.add(index);node=nodes[index];kind=node['kind'];counts[kind]+=1
        if kind=='split':
            axis=node['axis'];assert isinstance(axis,int)and 0<=axis<6
            children=node['children'];assert len(children)==2 and all(j>index for j in children)
            left,right=split_box(box,axis)
            walk(children[0],left);walk(children[1],right)
            return
        vol=F(1)
        for lo,hi in box:assert lo<hi;vol*=hi-lo
        volumes[kind]+=vol
        if kind=='excluded':
            exc=necessary(box)
            assert exc is not None and exc[0]==node['reason']and exc[1]==F(node['bound'])
        elif kind=='positive':
            if node.get('method')=='axis_bernstein':
                lower,controls=bernstein_bound(poly,box,node['axis'])
                assert [str(80*x)for x in controls]==node['control_lowers']
            else:
                assert node.get('method')is None
                lower,upper=box_bound(poly,box)
            assert 80*lower==F(node['lower_Cface'])>=0
            positive_boxes.append(dict(node=index,box=[[str(l),str(h)]for l,h in box],lower_Cface=str(80*lower)))
        else:
            assert kind=='open'
            open_boxes.append(dict(node=index,box=[[str(l),str(h)]for l,h in box]))
        if len(seen)%1000==0:
            print('PROVED: replay visited',len(seen),'nodes; counts',dict(counts),'seconds',round(time.time()-start,1),flush=True)
            if len(seen)%5000==0:
                with open('LOG.md','a')as f:f.write('\nPROVED: Final exact replay has checked '+str(len(seen))+' tree nodes; verified counts so far '+str(dict(counts))+'. Full replay is still running.\n')
    root=[tuple(map(F,p))for p in ROOT]
    walk(0,root)
    assert len(seen)==len(nodes)and counts==Counter(data['counts'])
    rootvolume=F(1)
    for lo,hi in root:rootvolume*=hi-lo
    assert sum(volumes.values())==rootvolume
    assert counts['split']+1==counts['positive']+counts['excluded']+counts['open']
    # Files list every terminal rational box for direct use in the residual set.
    with open('open_boxes.json','w')as f:json.dump(dict(status='OPEN',boxes=open_boxes),f,separators=(',',':'))
    with open('positive_partition_boxes.json','w')as f:json.dump(dict(status='PROVED',boxes=positive_boxes),f,separators=(',',':'))
    result=dict(status='PROVED partition and accepted leaves; OPEN residual positivity',
                counts=dict(counts),coordinate_volumes={k:str(v)for k,v in volumes.items()},
                root_volume=str(rootvolume),seconds=time.time()-start,
                maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    assert result['maxrss_bytes']<4*1024**3
    with open('cover_verification.json','w')as f:json.dump(result,f,indent=2)
    print('PROVED: complete rational root partition replayed:',dict(counts),flush=True)
    print('OPEN:',len(open_boxes),'terminal boxes retain the residual positivity problem.',flush=True)
    return result

if __name__=='__main__':replay()
