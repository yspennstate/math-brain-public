"""Checkpointed rational bisection with an outward interval sufficient bound.

The default root is a specified compact seven-dimensional gauge box. It is not
the entire feasible domain. A bounded run on the global containing box is also
available, and unresolved cells are always retained, never counted as proved.
Each accepted cell proves the full nine-dimensional Hessian inequality.
"""
import argparse,json,time,resource,os
from pathlib import Path
from fractions import Fraction as F
from interval_core import iv,interval,poly,matrix,det3,tr,matmul,pos,neg,bounds,full_certificate

ORDER=['q11','q22','q33','Q12','Q13','Re Q23','Im Q23']
LOCAL=[['9/20','11/20']]*3+[['9/100','11/100']]*2+[['-1/50','1/50'],['9/100','11/100']]
SMALL=[['49/100','51/100']]*3+[['99/1000','101/1000']]*2+[['-1/1000','1/1000'],['99/1000','101/1000']]
GLOBAL=[['0','1']]*3+[['0','1/2']]*2+[['-1/2','1/2'],['0','1/2']]

def enclosure(cell,delta=None,full_hessian=False):
    a,b,c,x,y,z,t=[interval(lo,hi) for lo,hi in cell]
    xx=[a,b,c,x,iv.mpf(0),y,iv.mpf(0),z,t]
    # Infeasibility rejection uses only necessary conditions with outward bounds.
    u=x*x;v=y*y;w=z**2+t**2
    dq=a*b*c-a*w-b*v-c*u+2*x*y*z
    dc=(1-a)*(1-b)*(1-c)-(1-a)*w-(1-b)*v-(1-c)*u-2*x*y*z
    necessary=[a,b,c,1-a,1-b,1-c,a*b-u,a*c-v,b*c-w,
               (1-a)*(1-b)-u,(1-a)*(1-c)-v,(1-b)*(1-c)-w,dq,dc]
    if delta is not None:
        dd=interval(delta,delta)
        aa,bb,cc=a-dd,b-dd,c-dd
        aaa,bbb,ccc=1-a-dd,1-b-dd,1-c-dd
        truncated=[aa,bb,cc,aaa,bbb,ccc,aa*bb-u,aa*cc-v,bb*cc-w,
                   aaa*bbb-u,aaa*ccc-v,bbb*ccc-w,
                   aa*bb*cc-aa*w-bb*v-cc*u+2*x*y*z,
                   aaa*bbb*ccc-aaa*w-bbb*v-ccc*u-2*x*y*z,w-dd**2]
        if any(map(neg,truncated)):return 'infeasible',None
    if any(map(neg,necessary)):return 'infeasible',None
    if not all(map(pos,necessary)):return 'split',None
    # Keep diagonal shifts factored. Expanding, e.g., (a-1)(b-1)(c-1)
    # creates very large dependency overestimates around a=b=c=1/2.
    p=[]
    for s in range(8):
        aa=a-(0 if s&1 else 1);bb=b-(0 if s&2 else 1);cc=c-(0 if s&4 else 1)
        p.append((-1)**(3-s.bit_count())*(aa*bb*cc-aa*w-bb*v-cc*u+2*x*y*z))
    if not all(map(pos,p)):return 'split',None
    q=matrix(xx)
    # Conditional log-odds via log(1+nonnegative rational). This gives sharper
    # enclosures than subtracting four logarithms of atom intervals.
    ell0=[];ell1=[]
    for i,j,k in ((1,2,0),(0,2,1),(0,1,2)):
        si,sj,sk=1<<i,1<<j,1<<k;prod=q[i][k]*q[k][j]
        v0=(1-q[k][k].real)*q[i][j]+prod;v1=q[k][k].real*q[i][j]-prod
        n0=v0.real**2+v0.imag**2;n1=v1.real**2+v1.imag**2
        ell0.append(iv.log(1+n0/(p[0]*p[si|sj])))
        ell1.append(iv.log(1+n1/(p[sk]*p[7])))
    # Intersect the three interval evaluations of the same gamma.
    gs=[ell0[i]-ell1[i] for i in range(3)]
    from interval_core import endpoint
    low=max(endpoint(g._mpi_[0]) for g in gs);high=min(endpoint(g._mpi_[1]) for g in gs)
    if low>high:raise AssertionError('disjoint gamma enclosures')
    gamma=interval(low,high)
    R=[[-gamma*q[i][j] for j in range(3)] for i in range(3)]
    for i in range(3):R[i][i]=iv.mpc((1-q[i][i].real)*ell0[i]+q[i][i].real*ell1[i])
    d=det3(R).real
    # Use the expanded real expression to reduce interval dependency.
    diag=[R[i][i].real for i in range(3)]
    off=sum(R[i][j].real**2+R[i][j].imag**2 for i,j in ((0,1),(0,2),(1,2)))
    variance=a*(1-a)+b*(1-b)+c*(1-c)-2*(u+v+w)
    sufficient=2*(diag[0]*diag[1]+diag[0]*diag[2]+diag[1]*diag[2])-sum(r*r for r in diag)-4*off-2*d*variance
    # R>0 is inherited for connected strict kernels; the root has x,y>0.
    if pos(sufficient):
        denom=sum(r**2 for r in diag)+2*off+d*variance
        if pos(denom):return 'certified',dict(method='cardinality',sufficient=bounds(sufficient,24),margin_lower_bound=bounds(sufficient/denom,24))
    if full_hessian:
        try:
            cert=full_certificate(xx,criterion_too=False)
            return 'certified',dict(method='full_hessian',ldl_pivots=cert['negative_hessian_pivots'])
        except ArithmeticError:pass
    return 'split',bounds(sufficient,24)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--global-box',action='store_true')
    ap.add_argument('--small-box',action='store_true')
    ap.add_argument('--interior',help='Truncated domain delta I <= Q <= (1-delta)I, all moduli >=delta')
    ap.add_argument('--full-hessian',action='store_true',help='Try the actual full interval Hessian after the sufficient test fails')
    ap.add_argument('--max-nodes',type=int,default=200000);ap.add_argument('--resume',action='store_true')
    ap.add_argument('--file',default='data/bnb_local.json');args=ap.parse_args()
    path=Path(args.file);iv.dps=45;start=time.monotonic()
    if args.resume:
        out=json.loads(path.read_text());stack=out.pop('pending');out['resumed']=out.get('resumed',0)+1
    else:
        root=GLOBAL if args.global_box else (SMALL if args.small_box else LOCAL)
        if args.interior:
            dd=F(args.interior)
            root=[[str(dd),str(1-dd)]]*3+[[str(dd),'1/2']]*2+[['-1/2','1/2'],['0','1/2']]
        out=dict(coordinate_order=ORDER,root=root,precision_decimal=iv.dps,
                 interior_delta=args.interior,full_hessian=args.full_hessian,nodes=0,certified=[],infeasible=[],splits=0,seconds=0,priority=os.getpriority(os.PRIO_PROCESS,0))
        stack=[root]
    elapsed=out['seconds'];base=out['nodes'];root=out['root'];rootwidth=[F(h)-F(l) for l,h in root]
    def save():
        out['pending']=stack;out['complete']=not stack
        out['seconds']=elapsed+time.monotonic()-start
        out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(path)
        del out['pending']
    while stack and out['nodes']-base<args.max_nodes:
        cell=stack.pop();status,bound=enclosure(cell,out.get('interior_delta'),out.get('full_hessian',False));out['nodes']+=1
        if status=='certified':out['certified'].append(dict(box=cell,**bound))
        elif status=='infeasible':out['infeasible'].append(cell)
        else:
            # Longest fractional side; exact bisection and no discarded slivers.
            widths=[(F(h)-F(l))/rootwidth[i] for i,(l,h) in enumerate(cell)]
            i=max(range(7),key=lambda j:widths[j]);mid=str((F(cell[i][0])+F(cell[i][1]))/2)
            left=[v[:] for v in cell];right=[v[:] for v in cell]
            left[i][1]=mid;right[i][0]=mid
            stack.extend([right,left]);out['splits']+=1
        if out['nodes']%1000==0:
            save();print(out['nodes'],len(out['certified']),len(stack),time.monotonic()-start,flush=True)
    save();print('complete',out['complete'],'nodes',out['nodes'],'certified',len(out['certified']),'pending',len(stack),flush=True)
if __name__=='__main__':main()
