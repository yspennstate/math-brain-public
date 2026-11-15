"""PROVED exports / OPEN residual: exact adaptive partition of the whole chart.

Every terminal node is either excluded by a necessary domain inequality,
positive by exact centered inclusion, or explicitly OPEN. No sample is used
for coverage or exclusion. The tree is a partition even when work is stopped.
"""
import argparse,json,time,resource
from fractions import Fraction as F
from collections import Counter,deque
from face_intervals import Interval as I
from zero_face import construct
from centered_bounds import integer_polynomial,box_bound

ROOT=[('1','4'),('-1','0'),('-4','4'),('-1','1/2'),('-4','4'),('0','4')]


def necessary(box):
    t,v1,z1,v2,z2,z=[I(*v)for v in box]
    xs=[v1,v2,1-t-v1-v2,t,I(-1)]
    ys=[z1,z2,-z-z1-z2,I(0),z]
    result={}
    # Choose the larger-diagonal endpoint as vertex 4 and reflect z>=0.
    result['orientation']=t.square()-1-z.square()
    # Sort the first three vertices by their first coordinate.
    result['order12']=v2-v1
    result['order23']=xs[2]-v2
    result['x3bound']=xs[2]+1
    for i in range(5):
        result['row'+str(i)]=4*t-xs[i].square()-ys[i].square()
    for i in range(5):
        for j in range(i+1,5):
            if (i,j)!=(3,4):
                result['g'+str(i)+str(j)]=t+xs[i]*xs[j]+ys[i]*ys[j]
    M00=sum(x.square()for x in xs);M11=sum(y.square()for y in ys)
    M01=sum(x*y for x,y in zip(xs,ys))
    delta=M00*M11-M01.square(); N=M00+M11
    result['spectral00']=5*t-M00
    result['spectral11']=5*t-M11
    result['connected']=(5*t-M00)*(5*t-M11)-M01.square()
    result['rank']=delta
    result['ratio']=784*delta-75*N.square()
    # These three inequalities are strict on the residual domain.
    strict={'connected','rank','ratio'}
    for key,value in result.items():
        if value.hi<0 or (key in strict and value.hi==0):
            return key,value.hi
    # If this condition holds, the largest gap is <=103/200,
    # a region already proved in STRAT6. This exclusion is optional.
    D=20*t-N; c=F(103,200)
    X=c*D-N
    disc=N.square()-4*delta
    if D.lo>0 and X.lo>=0 and X.square().lo>=disc.hi:
        return 'old_small_scale',X.square().lo-disc.hi
    return None


def split_box(box,axis):
    lo,hi=box[axis]; mid=(lo+hi)/2
    left=box.copy();right=box.copy()
    left[axis]=(lo,mid);right[axis]=(mid,hi)
    return left,right


def axis_for(box):
    # Use absolute coordinate widths; all variables are in the same chart scale.
    return max(range(6),key=lambda i:(box[i][1]-box[i][0],-i))


def discover(limit):
    poly=integer_polynomial(construct()[-1],80)
    root=[tuple(map(F,v))for v in ROOT]
    queue=deque([(0,root)])
    nodes=[None];counts=Counter(); start=time.time()
    examined=0
    while queue and examined<limit:
        index,box=queue.popleft(); examined+=1
        excluded=necessary(box)
        if excluded:
            key,hi=excluded
            nodes[index]={'kind':'excluded','reason':key,'bound':str(hi)}
            counts['excluded']+=1
        else:
            lo,hi=box_bound(poly,box)
            if lo>=0:
                nodes[index]={'kind':'positive','lower_Cface':str(80*lo)}
                counts['positive']+=1
            else:
                axis=axis_for(box); left,right=split_box(box,axis)
                a=len(nodes);nodes.extend([None,None])
                nodes[index]={'kind':'split','axis':axis,'children':[a,a+1]}
                queue.extend([(a,left),(a+1,right)]);counts['split']+=1
        if examined%1000==0:
            elapsed=time.time()-start
            print('PROVED: nodes',examined,'counts',dict(counts),'frontier',len(queue),'seconds',round(elapsed,1),flush=True)
            with open('LOG.md','a')as f:
                f.write('\nPROVED: Adaptive global chart partition: '+str(examined)+' nodes examined, '+str(dict(counts))+'; '+str(len(queue))+' boxes still OPEN. Exact certificates are being assembled; no full-cover claim.\n')
            time.sleep(0.1)
    for index,box in queue:
        assert nodes[index]is None
        nodes[index]={'kind':'open'}
    result=dict(status='PROVED partition, OPEN positivity on residual',root=ROOT,nodes=nodes,
                counts=dict(counts,open=len(queue)),seconds=time.time()-start,
                maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with open('global_cover.json','w')as f:json.dump(result,f,separators=(',',':'))
    print('PROVED: partition saved',result['counts'],'seconds',result['seconds'],'maxrss',result['maxrss'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=10000)
    discover(p.parse_args().limit)
