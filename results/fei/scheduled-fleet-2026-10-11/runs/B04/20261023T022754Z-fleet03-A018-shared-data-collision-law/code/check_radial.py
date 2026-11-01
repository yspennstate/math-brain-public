from pathlib import Path
import sys,importlib.util,time,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261022T202507Z-fleet03-A018-shared-data-collision-law/code/check_equal_mean.py'
spec=importlib.util.spec_from_file_location('arithmetic',OLD);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
F=c.F;add=c.add;sc=c.sc;lg=c.lg;ck=c.ck;nonneg=c.nonneg
def Dempty(b0,b1,Q0,Q1):
    r=(b0*b0+b1*b1)/2;a=(Q0[0]+Q1[0])/2
    return add(*(sc(v*v/2,lg(v*v/q)) for v,q in [(b0,Q0[0]),(b1,Q1[0])] if v),sc(-r,lg(r/a)) if r else {})
def Kplus(pb,zb):
    p=sum(pb)/2;z=sum(zb)/2
    return add(*(sc((1+x)/2,lg((1+x)/(1+y))) for x,y in zip(pb,zb)),sc(-(1+p),lg((1+p)/(1+z))))
def bernref(P):return (c.refs(P)[1],c.refs(P)[2])
def run(pilot=False):
    start=time.perf_counter();count=dominated=positive=equal=0;witness=None
    masks=[(c.walsh((-1,1,1,1)),0),(c.walsh((1,-1,-1,-1)),0),(c.walsh((-1,1,1,1)),1)]
    for dim in ([1] if pilot else [1,2]):
        N=2**dim
        data=[]
        for v in range(2**N):
            tt=tuple(1-2*((v>>i)&1) for i in range(N));data.append((tt,c.walsh(tt)))
        for i,(t0,a0) in enumerate(data):
            for j,(t1,a1) in enumerate(data):
                if time.perf_counter()-start>235:raise RuntimeError('Frozen internal deadline reached; no domain escalation')
                beta=(a0[0]+a1[0])/2;r=(a0[0]**2+a1[0]**2)/2;nu=beta*beta/r if r else F(1)
                ck(0<=nu<=1)
                for Q0 in bernref(c.probs(a0)):
                    for Q1 in bernref(c.probs(a1)):
                        ah,Qh=c.lift(a0,a1,Q0,Q1);ck(ah==c.walsh(tuple(v for pair in zip(t0,t1) for v in pair)))
                        a=(Q0[0]+Q1[0])/2;ck(Qh[0]==nu*a)
                        dc=add(sc(F(1,2),add(c.kl(c.probs(a0),Q0),c.kl(c.probs(a1),Q1))),sc(-1,c.kl(c.probs(ah),Qh)))
                        E=Dempty(a0[0],a1[0],Q0,Q1);rest=add(dc,sc(-1,E));ck(nonneg(E));ck(nonneg(rest))
                        for ss,kind in masks:
                            PP=c.probs(ss);Qs=PP if kind==0 else c.refs(PP)[2]
                            m=ss[0]**2;t=Qs[0];p=m*r;z=t*a
                            C,D=c.activation(ah,Qh,ss,Qs);C0,D0=c.activation(a0,Q0,ss,Qs);C1,D1=c.activation(a1,Q1,ss,Qs)
                            L=add(sc(F(1,2),add(D0,D1)),sc(-1,D),sc(-F(1,2),dc))
                            G=add(c.refund(p,z),sc(-1,c.refund(nu*p,nu*z)))
                            K=Kplus((m*a0[0]**2,m*a1[0]**2),(t*Q0[0],t*Q1[0]));ck(nonneg(K));ck(nonneg(G))
                            exact=add(G,sc(-F(1,2),add(sc(1-m,E),rest,K)));ck(L==exact)
                            ck(nonneg(add(G,sc(-1,L))))
                            # Actual full CE insertion retains profile curvature and both terminals.
                            DH=add(c.ent(c.probs(ah)),sc(-F(1,2),add(c.ent(c.probs(a0)),c.ent(c.probs(a1)))))
                            curvature=add(c.psi(beta*ss[0]),sc(-F(1,2),add(c.psi(a0[0]*ss[0]),c.psi(a1[0]*ss[0]))))
                            ck(add(C,sc(-F(1,2),add(C0,C1)))==add(sc(F(1,2),DH),curvature,L))
                            # Natural-unit Bregman upper bound avoids numerical 1/ln2.
                            raw=add(sc(p,lg(p/z)) if p else {},sc(z-p,lg(F(2))))
                            # Above lg(2) represents constant bits; check the natural-unit bound separately.
                            loG,hiG=c.interval(G)
                            bvec=sc((1-nu)*p/2,lg(p/z)) if p else {}
                            lob,hib=c.interval(bvec); bconst=(1-nu)*(z-p)/2
                            ck(lob+bconst>=hiG or G=={} and lob+bconst==0)
                            if p<=z:
                                B=sc(F(1,2),lg((1+z)/(1+nu*z)))
                                ck(nonneg(add(B,sc(-1,G))))
                                linear=sc((1-nu)/2,lg(1+z));ck(nonneg(add(linear,sc(-1,B))))
                                dominated+=1
                            if c.interval(L)[0]>0:positive+=1
                            if a0[0]==a1[0]:ck(nonneg(sc(-1,L)));equal+=1
                            if witness is None and nu==F(1,2) and c.interval(L)[0]>0:
                                witness={'dim':dim,'tables':[i,j],'means':[str(a0[0]),str(a1[0])],'nu':str(nu),'Lambda':{str(k):str(v) for k,v in L.items()},'G':{str(k):str(v) for k,v in G.items()}}
                            count+=1
        (ROOT/'out/CHECKPOINT.json').write_text(json.dumps({'dim_completed':dim,'cases':count,'assertions':c.checks}),encoding='utf-8')
    result={'status':'PASS','pilot':pilot,'cases':count,'dominated_cases':dominated,'positive_Lambda_cases':positive,'equal_mean_cases':equal,'assertions':c.checks,'seconds':time.perf_counter()-start,'witness':witness,'arithmetic_source_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
