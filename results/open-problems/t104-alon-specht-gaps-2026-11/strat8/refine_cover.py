"""NUMERICAL priorities only; PROVED exact leaf acceptance and partition."""
import heapq,json,math,time,resource,argparse
from fractions import Fraction as F
from collections import Counter
from cover_face import ROOT,necessary,split_box,axis_for
from zero_face import construct
from centered_bounds import integer_polynomial,box_analysis


def run(limit,source_path):
    source=json.load(open(source_path))
    nodes=source['nodes']; poly=integer_polynomial(construct()[-1],80)
    heap=[];counter=Counter();checked=0;start=time.time()
    def classify(index,box,depth):
        nonlocal checked
        checked+=1
        exc=necessary(box)
        if exc:
            nodes[index]={'kind':'excluded','reason':exc[0],'bound':str(exc[1])}
            counter['excluded']+=1;return
        lo,hi,c0,lower,impact=box_analysis(poly,box)
        if lo>=0:
            nodes[index]={'kind':'positive','lower_Cface':str(80*lo)}
            counter['positive']+=1;return
        nodes[index]={'kind':'open'}
        if depth>=40:return
        ratio=float(F(c0,max(1,c0-lower))) if c0>0 else -1.
        logvolume=sum(math.log2(float(h-l))for l,h in box)
        priority=logvolume+14*ratio
        axis=max(range(6),key=lambda i:impact[i]) if c0>0 else axis_for(box)
        heapq.heappush(heap,(-priority,index,box,depth,axis))
    initial=[]
    def walk(index,box,depth):
        node=nodes[index]
        if node['kind']=='split':
            l,r=split_box(box,node['axis'])
            walk(node['children'][0],l,depth+1);walk(node['children'][1],r,depth+1)
        elif node['kind']=='open':initial.append((index,box,depth))
    walk(0,[tuple(map(F,v))for v in ROOT],0)
    # Analyze every old open leaf; this costs about one minute, and does not
    # depend on the floating subdivision order.
    for ix,box,depth in initial:
        classify(ix,box,depth)
    print('PROVED: initialized',len(initial),'open leaves; exact new counts',dict(counter),flush=True)
    checkpoints=0
    while heap and checked<limit+len(initial):
        priority,ix,box,depth,axis=heapq.heappop(heap)
        left,right=split_box(box,axis);a=len(nodes);nodes.extend([None,None])
        nodes[ix]={'kind':'split','axis':axis,'children':[a,a+1]}
        classify(a,left,depth+1);classify(a+1,right,depth+1)
        if checked//1000>checkpoints:
            checkpoints=checked//1000
            msg='Adaptive refinement examined '+str(checked)+' boxes; new leaves '+str(dict(counter))+'.'
            print('PROVED:',msg,'seconds',round(time.time()-start,1),flush=True)
            with open('LOG.md','a')as f:f.write('\nPROVED: '+msg+' The unsolved frontier remains OPEN.\n')
            time.sleep(.1)
    counts=Counter(n['kind']for n in nodes)
    out=dict(status='PROVED partition, OPEN positivity on residual',root=ROOT,nodes=nodes,
             counts=dict(counts),seconds=time.time()-start,maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with open('global_cover.json','w')as f:json.dump(out,f,separators=(',',':'))
    print('PROVED: saved full root partition',dict(counts),'elapsed',out['seconds'],'maxrss',out['maxrss'],flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=20000);ap.add_argument('--source',default='global_cover.json');args=ap.parse_args();run(args.limit,args.source)
