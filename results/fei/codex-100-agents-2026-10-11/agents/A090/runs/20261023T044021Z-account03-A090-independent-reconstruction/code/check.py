from exact import *
import exact as engine

def actual(k,r):
    return [(1 if (z>>r).bit_count()<=1 else -1) if z%(2**r)==0 else (1 if z&((1<<k)-1)==0 else -1) for z in range(2**(r+3))]

def source(k,r,z,edited=True):
    s=F(1,2**k); t=F(1,2**r); mu=1-2*s
    g=[-1 if x&((1<<k)-1)==0 else 1 for x in range(2**r)]
    pg=spectrum(g)
    V=[mu**2]+[(1-mu**2)/(2**r-1)]*(2**r-1)
    R=[(1-z)*a+z*b for a,b in zip(pg,V)]
    check(sum(R)==1)
    if not edited:return R+[F(0)]*(7*2**r)
    p=spectrum(actual(k,r))
    q=[sum(p[T+(S<<r)] for S in range(8)) for T in range(2**r)]
    rp=[(1-t/s)*a+(t/s)*mu*(T==0)+2*t/2**r for T,a in enumerate(R)]
    check(sum(rp)==1 and min(q)>0 and min(rp)>0)
    if z==0:check(rp==q)
    Q=[rp[T]*p[T+(S<<r)]/q[T] for S in range(8) for T in range(2**r)]
    check(sum(Q)==1 and all(not a or b>0 for a,b in zip(p,Q)))
    return Q

root=actual(3,6); P=spectrum(root); H=entropy(P)
children,ps,m,B0,c0=query(root,P,3)
check(not c0)
on,off=children
check(on==actual(3,5))
Rold=[F(7,8)*x+F(1,8*len(m)) for x in m]
old=combine((1,B0),(F(1,2),ce(ps[0],Rold)),(F(1,2),ce(ps[1],Rold)))
Qon=source(3,5,F(1)); Qfar0=source(3,5,F(3,4),False); Qfar=source(3,5,F(1),False)
reset_initial=combine((F(1,2),ce(ps[0],Qon)),(-F(1,2),ce(ps[0],Rold)),(F(1,2),ce(ps[1],Qfar0)),(-F(1,2),ce(ps[1],Rold)))
incoming=combine((1,old),(1,reset_initial))
check(bounds(combine((3,{2:F(1)}),(-1,incoming)))[0]>F(42173,10**6))
rows=[]
for active in range(3):
    ac,pa,ra,B1,c1=query(on,Qon,active)
    a,d=ac
    check(a==actual(2,4) and len(set(d))==1)
    Qa=source(2,4,F(1)); Qd=[F(1)]+[F(0)]*(len(pa[1])-1)
    Ea=combine((1,ce(pa[0],Qa)),(-1,ce(pa[0],ra)))
    Ed=combine((1,ce(pa[1],Qd)),(-1,ce(pa[1],ra)))
    Efar=combine((1,ce(ps[1],Qfar)),(-1,ce(ps[1],Qfar0)))
    base=combine((1,incoming),(-F(1,2),c1),(F(1,4),Ea),(F(1,4),Ed),(F(1,2),Efar))
    direct=combine((1,B0),(F(1,2),B1),(F(1,4),ce(pa[0],Qa)),(F(1,2),ce(ps[1],Qfar)))
    check(not combine((1,base),(-1,direct)))
    check(bounds(combine((3,{2:F(1)}),(-1,base)))[0]>F(107981,10**6))
    for dummy in [2,3]:
        cc,pc,rc,B2,c2=query(a,Qa,dummy)
        check(cc[0]==actual(2,3))
        for u in [F(0),F(1)]:
            for v in [F(0),F(1)]:
                Q0=source(2,3,u); Q1=source(2,3,v,False)
                E0=combine((1,ce(pc[0],Q0)),(-1,ce(pc[0],rc)))
                E1=combine((1,ce(pc[1],Q1)),(-1,ce(pc[1],rc)))
                ledger=combine((1,base),(-F(1,4),c2),(F(1,8),E0),(F(1,8),E1))
                direct=combine((1,B0),(F(1,2),B1),(F(1,4),B2),(F(1,8),ce(pc[0],Q0)),(F(1,8),ce(pc[1],Q1)),(F(1,2),ce(ps[1],Qfar)))
                check(not combine((1,ledger),(-1,direct)))
                margin=combine((3,{2:F(1)}),(-1,ledger))
                check(bounds(margin)[0]>F(248210,10**6))
                if u==v==1:check(bounds(margin)[1]<F(248211,10**6))
                changed_on=any(x/(1-rc[0])!=y/(1-Q0[0]) for x,y in zip(rc[1:],Q0[1:]))
                changed_off=any(x/(1-rc[0])!=y/(1-Q1[0]) for x,y in zip(rc[1:],Q1[1:]))
                rows.append({'active':active,'dummy_after_active':dummy,'new_on_spread':str(u),'new_off_spread':str(v),'margin_interval':display(margin),'margin_log_linear':{str(k):str(x) for k,x in margin.items()},'weighted_refund':display(combine((F(1,4),c2))),'weighted_signed_reset':display(combine((F(1,8),E0),(F(1,8),E1))),'on_weighted_signed_reset':display(combine((F(1,8),E0))),'off_weighted_signed_reset':display(combine((F(1,8),E1))),'conditional_nonempty_shape_changed':[changed_on,changed_off]})
                check(time.perf_counter()-start<60)
worst=min(rows,key=lambda row:row['margin_interval'][0])
out={'status':'PASS','assertions':engine.assertions,'rows':rows,'worst':worst,'elapsed_seconds':time.perf_counter()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(Path(engine.__file__).read_bytes()).hexdigest(),'certified_margin_lower':'248210/1000000','source_frontier_margin':display(combine((3,{2:F(1)}),(-1,base))),'source_read_scope':'Source definitions and producer proof visible; no statement-only independence claimed for A004; new mixed-dummy extension independently constructed.'}
(run/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','elapsed_seconds','worst','source_frontier_margin']},indent=2))
