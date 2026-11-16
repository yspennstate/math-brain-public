"""PROVED exact partition/exclusions/accepted leaves; OPEN remaining leaves.
NUMERICAL work ordering has no role in accepted exact signs.
"""
import json,time,math,os
from fractions import Fraction as F
from collections import Counter,deque
from pathlib import Path
from face_intervals import Interval as I
from centered_bounds import box_analysis,box_bound
from axis_bernstein import box_bound as bernstein_bound
from zero_face import construct
ROOT=[('1','4'),('-1','0'),('-4','4'),('-1','1/2'),('-4','4'),('0','4')]

def polynomials():
    p=construct()[-1]
    result=[{}for _ in range(3)]
    for mon,c in p.terms():
        assert c.denominator==1 and int(c)%8==0
        result[mon[-1]][mon[:6]]=int(c)//8
    return result

def sqrt_enclosure(x,scale=10**9):
    assert x>=0
    k=math.isqrt(x.numerator*scale*scale//x.denominator)
    return F(k,scale),F(k+1,scale)

def lower_ceiling(lo,hi):
    bank=json.load(open('moment_cells.json'))+json.load(open('fine_cells.json'))
    lo,hi=max(F(3,20),lo),min(F(1),hi)
    if hi<lo:return F(14,25)
    cuts=sorted({lo,hi}|{F(c[k])for c in bank for k in ('rlo','rhi')if lo<=F(c[k])<=hi})
    points=cuts+[(a+b)/2 for a,b in zip(cuts,cuts[1:])]
    return min(max([F(14,25)]+[F(c['ahi'])for c in bank if F(c['rlo'])<=r<=F(c['rhi'])])for r in points)

def necessary(box):
    t,v1,z1,v2,z2,z=[I(*v)for v in box]
    xs=[v1,v2,1-t-v1-v2,t,I(-1)];ys=[z1,z2,-z-z1-z2,I(0),z]
    result={'orientation':t.square()-1-z.square(),'order12':v2-v1,'order23':xs[2]-v2,'x3bound':xs[2]+1}
    for i in range(5):result['row'+str(i)]=4*t-xs[i].square()-ys[i].square()
    for i in range(5):
        for j in range(i+1,5):
            if(i,j)!=(3,4):result['g'+str(i)+str(j)]=t+xs[i]*xs[j]+ys[i]*ys[j]
    M00=sum(x.square()for x in xs);M11=sum(y.square()for y in ys);M01=sum(x*y for x,y in zip(xs,ys))
    delta=M00*M11-M01.square();tau=M00+M11
    result.update(spectral00=5*t-M00,spectral11=5*t-M11,connected=(5*t-M00)*(5*t-M11)-M01.square(),rank=delta,ratio=529*delta-60*tau.square())
    strict={'connected','rank','ratio'}
    for key,value in result.items():
        if value.hi<0 or(key in strict and value.hi==0):return key,value.hi
    D=20*t-tau;H=tau.square()-4*delta;c=F(14,25)
    if tau.lo>0 and H.hi>=0:
        sl,sh=sqrt_enclosure(max(F(0),H.lo))[0],sqrt_enclosure(H.hi)[1]
        rl=(tau.lo-sh)/(tau.hi+sh);rh=(tau.hi-sl)/(tau.lo+sl)
        c=lower_ceiling(rl,rh)
    X=c*D-tau
    if D.lo>0 and X.lo>=0 and X.square().lo>=H.hi:return 'scale:'+str(c),X.square().lo-H.hi
    return None

def split_box(box,axis):
    lo,hi=box[axis];mid=(lo+hi)/2;left=box.copy();right=box.copy();left[axis]=(lo,mid);right[axis]=(mid,hi)
    return left,right

def prove_box(polys,box,try_bernstein=False):
    lower,upper,_,_,impact=box_analysis(polys[0],box)
    record=None
    if lower>=0:record=dict(kind='positive',method='centered',lower=str(8*lower))
    elif try_bernstein:
        for axis in sorted(range(6),key=lambda i:impact[i],reverse=True)[:2]:
            lo,controls=bernstein_bound(polys[0],box,axis)
            if lo>=0:
                record=dict(kind='positive',method='bernstein',axis=axis,lower=str(8*lo),controls=list(map(lambda v:str(8*v),controls)));break
    if record:
        more=[box_bound(p,box)[0]for p in polys[1:]]
        record['all_N']=min(more)>=0
        record['other_lowers']=[str(8*v)for v in more]
    return record,impact

def discover(limit=30000):
    polys=polynomials();queue=deque([(0,[tuple(map(F,p))for p in ROOT],0)]);nodes=[None];counts=Counter();start=time.monotonic()
    for examined in range(limit):
        if not queue:break
        index,box,depth=queue.popleft();exc=necessary(box)
        if exc:nodes[index]=dict(kind='excluded',reason=exc[0],bound=str(exc[1]));counts['excluded']+=1
        else:
            record,impacts=prove_box(polys,box,try_bernstein=(depth>=20))
            if record:nodes[index]=record;counts['positive']+=1
            else:
                # Width bisection guarantees shrinking every dimension. The
                # Bernstein axis choice affects acceptance, never exclusions.
                axis=max(range(6),key=lambda i:(box[i][1]-box[i][0],-i));left,right=split_box(box,axis)
                a=len(nodes);nodes.extend([None,None]);nodes[index]=dict(kind='split',axis=axis,children=[a,a+1]);queue.extend([(a,left,depth+1),(a+1,right,depth+1)]);counts['split']+=1
        if(examined+1)%1000==0:
            msg=f'PROVED partial exact ledger: {examined+1} face boxes examined; {dict(counts)}; {len(queue)} OPEN frontier boxes. Full replay pending.'
            print(msg,flush=True)
            with open('LOG.md','a')as f:f.write('\n'+msg+'\n')
            time.sleep(.1)
    for i,box,depth in queue:assert nodes[i]is None;nodes[i]=dict(kind='open')
    counts['open']=len(queue)
    Path('global_cover.json').write_text(json.dumps(dict(label='PROVED partition; OPEN sign on open leaves',root=ROOT,nodes=nodes,counts=dict(counts)),separators=(',',':'))+'\n')
    with open('LOG.md','a')as f:f.write('\nPROVED (global_cover.json; verify_cover.py): face partition assembled; '+str(dict(counts))+'. OPEN leaves are retained. NUMERICAL elapsed seconds '+str(time.monotonic()-start)+'.\n')
    print('PROVED: partition saved',dict(counts),flush=True)
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=30000);discover(p.parse_args().limit)
