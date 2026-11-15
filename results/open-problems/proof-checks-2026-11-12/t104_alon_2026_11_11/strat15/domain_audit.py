"""Audit inherited exclusions under the all-N residual premises."""
import sys,json,csv,time
from fractions import Fraction as F
from pathlib import Path
import exact_bernstein as ex
from inventory import S10,S12,S13,flat_leaves,tree_leaves,HERE
sys.path.append(str(S10))
from face_intervals import Interval as I
from cover_face import sqrt_enclosure
from centered_bounds import box_bound

def scale_exclusion(box):
    t,v1,z1,v2,z2,z=[I(*v)for v in box]
    xs=[v1,v2,1-t-v1-v2,t,I(-1)];ys=[z1,z2,-z-z1-z2,I(0),z]
    m00=sum(x.square()for x in xs);m11=sum(y.square()for y in ys);m01=sum(x*y for x,y in zip(xs,ys))
    delta=m00*m11-m01.square();tau=m00+m11;D=20*t-tau;H=tau.square()-4*delta
    c=F(129,250)
    if tau.lo>0 and H.hi>=0:
        sl=sqrt_enclosure(max(F(0),H.lo))[0];sh=sqrt_enclosure(H.hi)[1]
        rl=max(F(3,25),(tau.lo-sh)/(tau.hi+sh));rh=min(F(1),(tau.hi-sl)/(tau.lo+sl))
        if rl<=rh:
            rows=list(csv.DictReader((S10/'ceiling_table.csv').open()))
            cuts=sorted({rl,rh}|{F(row[k])for row in rows for k in ('rlo','rhi')if rl<=F(row[k])<=rh})
            points=cuts+[(a+b)/2 for a,b in zip(cuts,cuts[1:])]
            c=min(max([c]+[F(row['new_allN'])for row in rows if F(row['rlo'])<=r<=F(row['rhi'])])for r in points)
    X=c*D-tau
    if D.lo>0 and X.lo>=0 and X.square().lo>H.hi:
        return dict(method='allN-ceiling',ceiling=str(c),margin=str(X.square().lo-H.hi))
    return None

def transfer(r):
    box=[tuple(map(F,x))for x in r['box']]
    n=r['old']
    if n['kind']=='excluded':
        reason=n['reason']
        if reason.startswith('scale:'):return scale_exclusion(box)
        if reason=='ratio':
            lo,hi=box_bound(ex.chart_data()[1]['ratio'],box)
            if hi<0:return dict(method='weaker-ratio',upper=str(hi))
            return scale_exclusion(box)
        return dict(method='unchanged-common-interval',reason=reason)
    assert n['kind']=='exclusion'
    proposal=dict(kind='exclusion',box=r['box'],**{'lambda':n['lambda']})
    if 'bernstein_degrees'in n:proposal['bernstein_degrees']=n['bernstein_degrees']
    try:
        lo,method=ex.verify_certificate(proposal)
        if lo>0:return dict(method='weaker-Farkas',certificate=proposal,lower=str(lo),verification=method)
    except (AssertionError,KeyError):pass
    return scale_exclusion(box)

def main():
    start=time.monotonic();records=[]
    old=json.loads((S10/'global_cover.json').read_text())
    for i,b,n in flat_leaves(old):
        if n['kind']=='excluded':records.append(dict(source='STRAT10-exclusion',node=i,box=b,old=n))
    oldopens={i:b for i,b,n in flat_leaves(old)if n['kind']=='open'}
    overlay=json.loads((S12/'STRAT11/corner_cover.json').read_text())
    roots=[(r['overlay_node'],oldopens[r['source_node']])for r in overlay['roots']]
    for i,b,n in flat_leaves(overlay,roots):
        if n['kind']=='excluded':records.append(dict(source='STRAT11-exclusion',node=i,box=b,old=n))
    for source,path in [('STRAT12-exclusion',S12/'certificates.json'),('STRAT13-exclusion',S13/'collar_cover.json')]:
        for r in json.loads(path.read_text())['records']:
            for p,n in tree_leaves(r['tree']):
                if n['kind']=='exclusion':records.append(dict(source=source,node=r['node'],path=p,box=n['box'],old=n))
    good=[];bad=[]
    for i,r in enumerate(records):
        cert=transfer(r)
        if cert:good.append(dict(source=r['source'],node=r['node'],path=r.get('path',''),box=r['box'],transfer=cert))
        else:bad.append(r)
        if(i+1)%1000==0:print('exclusion audit',i+1,'transfers',len(good),'need new sign',len(bad),flush=True)
    (HERE/'domain_audit.json').write_text(json.dumps(dict(transferred=good,need_new_sign=bad),separators=(',',':'))+'\n')
    print('PROVED (domain_audit.py): exact audit',len(good),'transfers;',len(bad),'OPEN for new certificates; seconds',time.monotonic()-start)
if __name__=='__main__':main()
